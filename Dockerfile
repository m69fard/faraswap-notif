# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .


# Expose the application port
EXPOSE 8001

# Run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]