# Use an official Python runtime
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents
COPY . .

# Install Flask
RUN pip install flask

# Expose the app port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

