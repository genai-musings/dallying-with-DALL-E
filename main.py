"""main program entry point"""
import os
import logging
import openai

from dalleImage import dalleImage
from fileUtils import save_image

def main():

    client = dalleImage(os.getenv('OPENAI_KEY') )

    # Configure logging
    logging.basicConfig(filename="error.log", level=logging.ERROR)

    while True:
        # Prompt for the image description
        print ("\n\nEnter a description of the image you want to generate?")
        print ("Leave input empty and press 'Return' to exit.\n\n")
        prompt = str(input())

        if prompt == "":
            break

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
