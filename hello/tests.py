from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class AboutViewTest(TestCase):
    def test_about_route_exists(self):
        """Test that the about route exists and returns a 200 status code."""
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    
    def test_about_route_uses_correct_template(self):
        """Test that the about route uses the correct template."""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'About This Application')
        self.assertTemplateUsed(response, 'hello/about.html')
    
    def test_about_link_in_navigation(self):
        """Test that the about link appears in the navigation."""
        response = self.client.get('/')
        self.assertContains(response, 'href="/about/"')
        self.assertContains(response, 'About')
