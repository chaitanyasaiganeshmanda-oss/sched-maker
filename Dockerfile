FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirement file and install deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the Flask port (default 5000)
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]

