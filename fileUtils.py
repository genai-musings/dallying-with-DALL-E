"""fileUtils class."""
import os
import requests

def save_image(response_data, save_directory):
    """
    Save images from the provided response data to the specified directory.

    Args:
        response_data (list): List of image data obtained from the API response.
        save_directory (str): Directory path where the images will be saved.

    Returns:
        list: A list of boolean values indicating the success of each image save operation.
    """
    save_results = []  # List to store the results of save operations

    for i, img_data in enumerate(response_data):
        url = img_data["url"]
        filename = f"image_{i}.png"
        filepath = os.path.join(save_directory, filename)

        try:
            response = requests.get(url,timeout=20)
            response.raise_for_status()  # Raise an exception for non-2xx status codes

            print(url, filename, filepath)

            with open(filepath, "wb") as f:
                f.write(response.content)
            save_results.append(True)  # Save operation successful
        except Exception as e:
            print(f"Error saving image {filename}: {str(e)}")
            save_results.append(False)  # Save operation failed

    return save_results
