from unittest import TestCase
from unittest.mock import Mock
from fastapi.testclient import TestClient
from main import app
from routers.v1.author_router import AuthorRouter
from services.author_service import AuthorService

class TestAuthorRouter(TestCase):
    def setUp(self):
        self.author_service = Mock(AuthorService)
        self.author_router = AuthorRouter
        self.client = TestClient(app)

    def test_index_endpoint(self):
        response = self.client.get("/v1/authors/")
        self.assertEqual(response.status_code, 200)

    def test_get_endpoint(self):
        author_id = 1
        response = self.client.get(f"/v1/authors/{author_id}")
        self.assertEqual(response.status_code, 200)

    def test_create_endpoint(self):
        author_data = {"name": "John Doe"}
        response = self.client.post("/v1/authors/", json=author_data)
        self.assertEqual(response.status_code, 201)

    def test_update_endpoint(self):
        author_id = 1
        updated_author_data = {"name": "Jane Doe"}
        response = self.client.patch(f"/v1/authors/{author_id}", json=updated_author_data)
        self.assertEqual(response.status_code, 200)

    def test_delete_endpoint(self):
        author_id = 1
        response = self.client.delete(f"/v1/authors/{author_id}")
        self.assertEqual(response.status_code, 204)