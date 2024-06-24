# Use a Python base image with version 3.8
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Expose the application port
EXPOSE 3111

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Initialize the database with predefined posts
RUN python init_db.py

# Command to run the application
CMD ["python", "app.py"]
