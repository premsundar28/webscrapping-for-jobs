# Use a lightweight official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy everything into the image
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the main Python file
CMD ["python3", "main.py"]
