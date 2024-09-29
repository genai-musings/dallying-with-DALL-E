import unittest
from unittest.mock import patch, mock_open, MagicMock
import requests
import os
import sys

# Add the root folder to the Python module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the save_image function from your module
from fileUtils import save_image

class TestFileUtils:
    
    @patch("fileUtils.requests.get")
    @patch("fileUtils.os.path.join", side_effect=lambda d, f: f"{d}/{f}")  # Use simple path construction
    @patch("builtins.open", new_callable=mock_open)
    def test_save_image_success(self, mock_open_file, mock_os_path_join, mock_requests_get):
        """
        Test save_image function for successful image saving.
        """
        response_data = [
            MagicMock(url="http://example.com/image1.png"),
            MagicMock(url="http://example.com/image2.png"),
        ]
        save_directory = "/fake/directory"

        # Mock the response of requests.get
        mock_response = MagicMock()
        mock_response.content = b"fake_image_data"
        mock_requests_get.return_value = mock_response

        # Call the function
        results = save_image(response_data, save_directory)
        assert results == ["image_0.png", "image_1.png"]  # Adjust this based on your expected output

    @patch("fileUtils.requests.get")
    @patch("fileUtils.os.path.join", side_effect=lambda d, f: f"{d}/{f}")  # Use simple path construction
    @patch("builtins.open", new_callable=mock_open)
    def test_save_image_failure(self, mock_open_file, mock_os_path_join, mock_requests_get):
        """
        Test save_image function when there is an error during the image download.
        """
        response_data = [
            MagicMock(url="http://example.com/image1.png"),
            MagicMock(url="http://example.com/image2.png"),
        ]
        save_directory = "/fake/directory"

        # Mock the request.get response to raise an exception (e.g., timeout)
        mock_requests_get.side_effect = requests.exceptions.RequestException("Connection error")

        # Call the function
        results = save_image(response_data, save_directory)
        assert results == []  # Adjust based on how your function handles failures