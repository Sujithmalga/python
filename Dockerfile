# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install git
RUN apt-get update && apt-get install -y git
RUN  pip install --upgrade pip
# Set the working directory in the container
WORKDIR /app

# Clone the GitHub repository
RUN git clone https://github.com/Sujithmalga/python.git .

# Install any needed packages specified in requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "app.py"]
