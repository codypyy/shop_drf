from typing import Any
from django.core import checks
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class OrderField(models.PositiveIntegerField):
    description = "ordering field for uniqe product"

    def __init__(self, unique_for_field=None, *args, **kwargs):
        self.unique_for_field = unique_for_field
        super().__init__(*args, **kwargs)
    

    def check(self, **kwargs):
        return [
            *super().check(**kwargs),
            *self._check_unique_for_field(**kwargs)
        ]
    

    def _check_unique_for_field(self, **kwargs):
        field_object = self.model._meta.get_fields()
        field_list = []

        for obj in field_object:
            field_list.append(obj.name)

        if self.unique_for_field is None:
            return [
                checks.ERROR(
                    "OrderField attribute 'unique_for_field' must defined",
                    obj=self,
                    id="product.E001",
                )
            ]
        elif self.unique_for_field not in field_list:
            return [
                checks.ERROR(
                    "OrderField attribute 'unique_for_field' not found",
                    obj=self,
                    id="product.E002",
                )
            ]
        else:
            return []
        
    def pre_save(self, model_instance, add):

        if getattr(model_instance, self.attname) is None:
            try:
                all_pl = self.model.objects.all()
                filter_query = {
                    self.unique_for_field : getattr(model_instance, self.unique_for_field)
                }
                filter_pl = all_pl.filter(**filter_query)
                last_item = filter_pl.latest(self.attname)
                value = last_item.order + 1
            except ObjectDoesNotExist:
                value = 1

            return value

        else:
            return super().pre_save(model_instance, add)