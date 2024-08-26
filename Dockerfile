# Use an official lightweight Python image as a parent image
FROM python:3.9-slim

# Set the working directory to /app inside the container
WORKDIR /app

# Copy the requirements.txt file from your host to the current location (/app) in the container
COPY requirements.txt .

# Install core dependencies.
RUN apt-get update && apt-get install -y libpq-dev build-essential

# Install the Python dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from the current directory on the host to the /app directory in the container
COPY . .

# Command to run the gunicorn server with the specified host and port, and point it to the WSGI application
CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:app"]
