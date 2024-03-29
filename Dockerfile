# Use a base Python image
FROM python:3.11

LABEL maintainer=“tom_halpin@hotmail.com,eoinhalpin99@gmail.com”
LABEL description="Sample Python application for dallying wit DALL-E via API."

# Set the working directory inside the container
WORKDIR /app

# Create the testdata directory to store the images generated
RUN mkdir ./testdata

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the Python scripts to the working directory
COPY main.py .
COPY dalleImage.py .
COPY fileUtils.py .

# Specify the command to run the Python script
CMD ["python", "main.py"]
