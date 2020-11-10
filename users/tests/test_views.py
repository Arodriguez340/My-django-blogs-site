from django.test import TestCase
from django.urls import resolve
from users.views import dashboard

# Test cases for web views.

class DashBoardViewTest(TestCase):

    def test_dashboard_url_resolve_to_dashboard_view(self):
        found = resolve('dashboard/')
        self.assertEqual(found.func, dashboard)

    