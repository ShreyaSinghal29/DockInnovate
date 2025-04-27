

---

# 📦 Dockerized Deployment of Streamlit App with PostgreSQL Integration

## ✨ Introduction
This project showcases how to containerize a **Streamlit application** that connects seamlessly with a **PostgreSQL database**, using **Docker** for a complete deployment setup.  
The app fetches user data from the database and displays it in an interactive UI.

---

## 📂 Folder Structure
```
Streamlit-Postgres-Deployment/
│── Dockerfile
│── main.py
```

### 🧩 About the Files:
- **main.py** — Streamlit script that interacts with PostgreSQL and displays the data.
- **Dockerfile** — Instructions to containerize and run the Streamlit application.

---

## ⚙️ Setting Up PostgreSQL with Docker

### Step 1: Pull PostgreSQL Image
```bash
docker pull postgres
```

### Step 2: Create a Custom Docker Network
```bash
docker network create streamlit_postgres_network
```
This private network allows isolated communication between containers.

### Step 3: Launch PostgreSQL Container
```bash
docker run --name postgres_container --network streamlit_postgres_network -e POSTGRES_USER=shreya -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=testdb -p 5432:5432 -d postgres
```
This spins up the database container with a predefined user and database.

---

## 🗃️ Setting Up the Database

### Step 4: Connect to PostgreSQL
```bash
docker exec -it postgres_container psql -U shreya -d testdb
```

### Step 5: Create a Table for Passenger Data
```sql
CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100)
);
```

### Step 6: Insert Sample Records
```sql
INSERT INTO passengers (name, location) VALUES
('Shreya', 'New Delhi'),
('Anuj', 'Mumbai'),
('Priya', 'Chennai');
```

---

## 🎨 Developing the Streamlit App (`main.py`)

The Streamlit app connects to PostgreSQL, fetches data, and presents it in a user-friendly layout with custom styles.

### 🛠 Features:
- Database connectivity using **psycopg2**.
- Real-time data fetching and rendering.
- Modern, polished UI with embedded CSS.

---

## 🐳 Containerizing the Streamlit Application

### Step 7: Write the Dockerfile
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY main.py .
RUN pip install streamlit psycopg2
CMD ["streamlit", "run", "main.py", "--server.port=8502", "--server.address=0.0.0.0"]
```

---

## 🚀 Building and Running the Containers

### Step 8: Build the Streamlit Docker Image
```bash
docker build -t streamlit_app .
```

### Step 9: Run the Streamlit Container
```bash
docker run --name streamlit_container --network streamlit_postgres_network -p 8502:8502 -d streamlit_app
```
Both the app and the database will now communicate through the shared network.

---

## 🌐 Accessing the Application

Open your web browser and go to:
👉 **[http://localhost:8502](http://localhost:8502)**

You should now see the dynamic list of passengers displayed beautifully!

---

## 📝 Conclusion
- ✅ PostgreSQL container holds the backend data.
- ✅ Streamlit container fetches and displays the data live.
- ✅ Both services are connected over a Docker network.
- ✅ Application is accessible locally via **http://localhost:8502**.

This setup offers a **clean, portable, and scalable** solution for full-stack data-driven apps using **Streamlit** and **PostgreSQL** with **Docker**. 🚀

---

