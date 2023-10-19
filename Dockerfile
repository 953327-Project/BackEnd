FROM python:3.10-slim

# Set the working directory
WORKDIR .
# Install the required packages
COPY requirements.txt ./
RUN pip install -r requirements.txt
# Copy your project files into the container
COPY . .
# Expose port 5000
EXPOSE 5000

# Start the Flask application
CMD ["gunicorn", "Application.Main:app", "--bind", "0.0.0.0:80"]
