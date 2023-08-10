"""fileUtils class tests."""
import unittest
from unittest.mock import patch, Mock
from unittest import mock
import os
import sys
import requests

# Add the root folder to the Python module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fileUtils import save_image

class TestSaveImage(unittest.TestCase):
    def test_save_image_success(self):
        # Test saving images successfully

        # Mocked response data
        response_data = [
            {"url": "http://example.com/image_0.png"},
            {"url": "http://example.com/image_1.png"}
        ]
        save_directory = os.path.join(os.getcwd(), "testdata")

        # Create the directory if it doesn't exist
        os.makedirs(save_directory, exist_ok=True)

        # Create a mock response for the requests.get method
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"image content"

        # Mock the requests.get method to return the mock response
        with patch.object(requests, "get", return_value=mock_response) as mock_get:
            save_results = save_image(response_data, save_directory)

            # Check if images are saved successfully
            self.assertEqual(save_results, [True, True])

            # Check if the correct file paths are used
        self.assertEqual(
            mock_get.call_args_list,
            [mock.call(r["url"], timeout=30) for r in response_data]
        )

    def test_save_image_failure(self):
        # Test handling failure while saving images

        # Mocked response data
        response_data = [
            {"url": "http://example.com/image_0.png"},
            {"url": "http://example.com/image_1.png"}
        ]
        save_directory = os.path.join(os.getcwd(), "testdata")

        # Create the directory if it doesn't exist
        os.makedirs(save_directory, exist_ok=True)

        # Create a mock response for the requests.get method
        mock_response = Mock()
        mock_response.status_code = 404

        # Mock the requests.get method to return the mock response
        with patch.object(requests, "get", return_value=mock_response) as mock_get:
            save_results = save_image(response_data, save_directory)

            # Check if the save operation fails for both images
            self.assertEqual(save_results, [False, False])

            # Check if the correct file paths are used
        self.assertEqual(
            mock_get.call_args_list,
            [mock.call(r["url"], timeout=30) for r in response_data]
        )

if __name__ == '__main__':
    unittest.main()
