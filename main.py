"""main program entry point"""
import os
import sys
import logging
import openai

from dalleImage import dalleImage
from fileUtils import save_image

def main():

    # Check if the OPENAI_API_KEY environment variable is set
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("Error: The environment variable 'OPENAI_API_KEY' is not set, please set it before continuing.")
        print("       Refer to the README.md for instructions on how to create an OpenAI API Key.")
        sys.exit(1)  # Exit the application with a non-zero status code

    # Configure logging
    logging.basicConfig(filename="error.log", level=logging.ERROR)

    while True:
        # Prompt for the image description
        print ("\n\nEnter a description of the image you want to generate?")
        print ("Leave input empty and press 'Return' to exit.\n\n")
        prompt = str(input())

        if prompt == "":
            sys.exit(0)

        try:
            response = client.generate_image(prompt, 2, "256x256")
            print(response)
            response = save_image(response_data = response["data"],
                                  save_directory = os.path.join(os.getcwd(), "testdata"))
            print(response)
        except openai.OpenAIError as exp:
            # Handle the exception
            # Log the error message and exception type
            logging.error(f"OpenAIError: {exp}", exc_info=True)
            print(f"Error: {exp}")
        except Exception as exp:
            # Handle the exception
            # Log the error message and exception type
            logging.error(f"Error: {exp}", exc_info=True)
            print("An error occurred, please try again.")

if __name__ == "__main__":
    main()
