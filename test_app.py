import unittest
import json
from app import app


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_process_and_store_data(self):
        mock_data = {
            "products": [
                {"id": 1, "name": "Product 1", "price": 100},
                {"id": 2, "name": "Product 2", "price": 200},
                {"id": 3, "name": "Product 3", "price": 300}
            ]
        }
        response = self.app.post('/process-data', data=json.dumps(mock_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Data processed and stored successfully", response.data)

    def test_get_processed_data(self):
        # First, process and store the data
        mock_data = {
            "products": [
                {"id": 1, "name": "Product 1", "price": 100},
                {"id": 2, "name": "Product 2", "price": 200},
                {"id": 3, "name": "Product 3", "price": 300}
            ]
        }
        self.app.post('/process-data', data=json.dumps(mock_data), content_type='application/json')

        # Then, retrieve the processed data
        response = self.app.get('/get-processed-data')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        print(data)  # Debugging statement
        self.assertEqual(data['products'][0]['name'], 'PRODUCT 1')


if __name__ == '__main__':
    unittest.main()
