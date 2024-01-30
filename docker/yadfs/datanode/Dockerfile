# Use an official Python runtime as a parent image
FROM python:3


WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r /app/requirements.txt

# Make port 12345 available to the world outside this container
EXPOSE 12345

# Define the command to run the server script
CMD ["python", "/app/datanode.py"]
