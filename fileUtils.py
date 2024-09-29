import os
import requests

def save_image(response_data, save_directory):
    """
    Save images from the provided response data to the specified directory.

    Args:
        response_data (list): List of image data obtained from the API response.
        save_directory (str): Directory path where the images will be saved.

    Returns:
        list: A list of filenames of the saved images. An empty list if all saves fail.
    """
    saved_images = []  # List to store the names of saved images

    #print(response_data)
    for i, img_data in enumerate(response_data):
        #print(img_data)
        url = img_data.url
        filename = f"image_{i}.png"
        filepath = os.path.join(save_directory, filename)

        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()  # Raise an exception for non-2xx status codes

            #print(url, filename, filepath)

            with open(filepath, "wb") as f:
                f.write(response.content)
            saved_images.append(filename)  # Append the saved filename
        except Exception as e:
            print(f"Error saving image {filename}: {str(e)}")
            # You can still append a boolean here if you want to track failures, 
            # but it should not affect the returned list.
    
    return saved_images  # Return the actual filenames saved
