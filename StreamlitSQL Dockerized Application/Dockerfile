FROM python:3.9

# Set working directory
WORKDIR /app

# Copy app files
COPY main.py .

# Install required Python packages
RUN pip install streamlit psycopg2

# Expose the port your app will run on
EXPOSE 8502

# Run the Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=8502", "--server.address=0.0.0.0"]
