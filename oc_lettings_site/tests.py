# oc_lettings_site/tests.py
from django.test import TestCase


class ErrorPageTests(TestCase):
    def test_404_page_loads_and_returns_404_status(self):
        # Access a URL that does not exist
        response = self.client.get('/definitely-not-a-real-url/')
        
        # Check if the correct HTTP status code is returned (This passed: 404 == 404)
        self.assertEqual(response.status_code, 404)
        
        # Check if the custom template content is present (e.g., the H2 title)
        # We MUST explicitly pass status_code=404 to assertContains.
        # It was failing because it expected status_code=200 by default.
        self.assertContains(response, 'Page Not Found', status_code=404)