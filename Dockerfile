# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy necessary files to keep the image size small
COPY ./requirements.txt /app/requirements.txt
COPY ./src /app/src
COPY ./model /app/model
COPY ./config /app/config
COPY ./data /app/data  

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Command to run your application (example)
CMD ["python", "/app/src/pipeline/train_model.py"]
