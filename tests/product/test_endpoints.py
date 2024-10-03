import json
import pytest

pytestmark = pytest.mark.django_db

class TestCategoryEndpoints:

    endpoint = '/api/category/'

    def test_category_get(self, category_factory, api_client):

        category_factory.create_batch(4)

        response = api_client().get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


class TestBrandEndpoints:

    endpoint = '/api/brand/'

    def test_brand_get(self, brand_factory, api_client):

        brand_factory.create_batch(3)

        response = api_client().get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3



class TestProductEndpoints:

    endpoint = '/api/product/'

    def test_get_all_product(self, product_factory, api_client):
        product_factory.create_batch(2)
        response = api_client().get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2

    def test_get_product_with_id(self, product_factory, api_client):
        obj = product_factory(name="test_product")
        response = api_client().get( f"{self.endpoint}{obj.id}/" )
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 6

    def test_get_product_with_category(self, product_factory, category_factory, api_client):
        obj = category_factory(name="cat_1")
        product_factory(category=obj)
        product_factory(category=obj)
        product_factory()
        response = api_client().get( f"{self.endpoint}category/{obj.name}/" )
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2