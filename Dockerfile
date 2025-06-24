# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirement spec and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of project
COPY . .

# Default command to run the script
CMD ["python", "fund_forecast_engine.py"]
