import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.client.testing = True

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Retro Snake', response.data)
    
    def test_static_files(self):
        response = self.client.get('/static/game.js')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'const canvas', response.data)

    def test_score_text(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Check if the score is displayed on the page (assuming it’s visible in the HTML)
        self.assertIn(b'Score: 0', response.data)

if __name__ == '__main__':
    unittest.main()
