FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies needed for psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy your app files
COPY main.py .

# Install required Python packages
RUN pip install streamlit psycopg2

# Expose the port your app will run on
EXPOSE 8502

# Run the Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=8502", "--server.address=0.0.0.0"]
