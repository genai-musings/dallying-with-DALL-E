"""dalleImage class."""
import openai

class dalleImage:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_image(self, prompt, n=2, size="256x256"):
        # Create the image using the OpenAI API
        response = openai.Image.create(
            prompt=prompt,
            n=n,
            size=size
            )
        return response
