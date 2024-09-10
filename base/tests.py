import tempfile  # Import tempfile for creating temporary files

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TextCreateTests(APITestCase):
    def test_create_text_with_plain_text(self):
        """
        Ensure we can create a new Text object using plain text.
        """
        url = reverse("text-list")
        data = {
            "title": "Shakespeare Sonnet",
            "content": "Shall I compare thee to a summer's day...",
        }

        response = self.client.post(
            url, data, format="json"
        )  # Explicitly set the format to 'json'

        print(response.data)  # Add this to debug if the test still fails
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], data["title"])
        self.assertEqual(response.data["content"], data["content"])

    def test_create_text_with_file_upload(self):
        """
        Ensure we can create a new Text object by uploading a .txt file.
        """
        url = reverse("text-list")

        # Create a temporary file to simulate file upload
        with tempfile.NamedTemporaryFile(suffix=".txt") as temp_file:
            temp_file.write(
                b"Shall I compare thee to a summer's day..."
            )  # Write content to the file
            temp_file.seek(0)  # Move the pointer to the start of the file

            response = self.client.post(
                url, {"file": temp_file}, format="multipart"
            )  # Perform the file upload
            print(response.data)  # Debugging to check response
            self.assertEqual(
                response.status_code, status.HTTP_201_CREATED
            )  # Ensure it's successful
            self.assertIn(
                "Shall I compare thee", response.data["content"]
            )  # Ensure file content is saved
