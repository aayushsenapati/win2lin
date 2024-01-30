# Use an official Python runtime as a parent image
FROM python:3

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r /app/requirements.txt

# Define the command to run the client script
CMD ["python", "/app/namenode.py"]
