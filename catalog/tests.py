from django.test import TestCase


# Create your tests here.
class HomeViewTest(TestCase):
    def test_home_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_contacts_view(self):
        response = self.client.get("/contacts/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contacts.html")

    def test_contacts_post(self):
        response = self.client.post(
            "/contacts/",
            {
                "name": "Test Name",
                "phone": "Test Phone",
                "message": "Test Message",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contacts.html")
        self.assertContains(response, "Test Name")
        self.assertContains(response, "Test Phone")
        self.assertContains(response, "Test Message")
