# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy all the source code to the container
COPY . .

# Expose the port that the Flask app will run on
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
