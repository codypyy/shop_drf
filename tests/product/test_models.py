import pytest
from django.core.exceptions import ValidationError


pytestmark = pytest.mark.django_db

class TestCategoryModel:
    def test_str_method(self, category_factory):

        new_object = category_factory(name = "category_test")

        assert new_object.__str__() == "category_test"


class TestBrandModel:
    def test_str_method(self, brand_factory):

        obj = brand_factory(name = "brand_test")

        assert obj.__str__() == "brand_test"


class TestProductModel:
    def test_str_method(self, product_factory):

        obj = product_factory(name = "product_test")

        assert obj.__str__() == "product_test"


class TestProductLineModel:
    def test_str_method(self, product_line_factory):

        obj = product_line_factory(sku = "xl")

        assert obj.__str__() == "xl"
    

    def test_duplicate_order(self, product_line_factory, product_factory):
        prd = product_factory()
        product_line_factory(order=1, product=prd)
        with pytest.raises(ValidationError):
            product_line_factory(order=1, product=prd).clean_fields(None)
