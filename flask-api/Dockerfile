# Use an official Python image as base
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application
COPY . .

# Expose the port Flask will run on
EXPOSE 5001

# Run the Flask app
CMD ["python", "app.py"]
