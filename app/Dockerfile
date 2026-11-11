### Aaron King ####

FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY app.py .

# Expose the port the app runs on
EXPOSE 8080

# Set the command to run the application
CMD ["python", "app.py"]