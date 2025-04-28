

---

```markdown
# ☸️ Microservices Orchestration with Minikube & Kubernetes

This project demonstrates a simple microservices setup using **Minikube** and **Kubernetes**, featuring an **API Gateway** and a **Backend Service**. It focuses on containerization and deploying applications within a Kubernetes cluster.

---

## 📋 Prerequisites

Make sure you have the following installed on your system:

- **Minikube** — Local Kubernetes cluster
- **kubectl** — Kubernetes command-line tool
- **Docker** — For building container images

---

## 📂 Project Structure

```
.
├── README.md
├── backend/
│   ├── Dockerfile
│   ├── backend.py
│   └── requirements.txt
├── api-gateway/
│   ├── Dockerfile
│   ├── api_gateway.py
│   └── requirements.txt
└── kubernetes/
    ├── backend-service.yaml
    └── api-gateway.yaml
```

---

## 🚀 Step-by-Step Deployment

All commands should be run in your bash terminal.

### 1️⃣ Start Minikube

Start a local Kubernetes cluster:

```bash
minikube start
```

---

### 2️⃣ Configure Docker to Use Minikube's Daemon

Connect Docker to Minikube’s internal Docker environment:

```bash
eval $(minikube -p minikube docker-env)
```

---

### 3️⃣ Build and Deploy the Microservices

#### 3.1 Backend Service

- Move into the backend directory:

  ```bash
  cd backend
  ```

- Build the Docker image:

  ```bash
  docker build -t backend-service .
  ```

- Deploy the backend service to Kubernetes:

  ```bash
  kubectl apply -f ../kubernetes/backend-service.yaml
  ```

---

#### 3.2 API Gateway

- Navigate to the API Gateway directory:

  ```bash
  cd ../api-gateway
  ```

- Build the Docker image:

  ```bash
  docker build -t api-gateway .
  ```

- Deploy the API Gateway to Kubernetes:

  ```bash
  kubectl apply -f ../kubernetes/api-gateway.yaml
  ```

---

### 4️⃣ Verify Deployments

Check the status of your services and deployments:

```bash
kubectl get deployments
kubectl get services
```

---

### 5️⃣ Access the Application

To open the API Gateway in your browser:

```bash
minikube service api-gateway
```

This will route you to the API Gateway endpoint, where you can interact with the backend service.

---

### 6️⃣ Monitoring and Debugging

Useful commands for troubleshooting:

```bash
# Check API Gateway logs
kubectl logs deployment/api-gateway

# Check Backend Service logs
kubectl logs deployment/backend-service

# Describe pods for more details
kubectl describe pods
```

---

### 7️⃣ Cleaning Up Resources

To remove deployments and stop the cluster:

```bash
# Delete the deployed services
kubectl delete -f kubernetes/api-gateway.yaml
kubectl delete -f kubernetes/backend-service.yaml

# Stop Minikube
minikube stop
```

---

## 🏛️ Architecture Overview

### 🔹 Components

- **API Gateway**
  - Serves as the single entry point for clients.
  - Routes requests to the backend service.
  - Exposes **port 8080**.

- **Backend Service**
  - Handles core business logic.
  - Sends responses to the API Gateway.
  - Listens on **port 5000**.

---

### 🔄 Communication Flow

```
Client → API Gateway (8080) → Backend Service (5000) → API Gateway → Client
```

---

## 🛠 Troubleshooting

- **Docker Images Not Found**  
  - Ensure you are building images using Minikube’s Docker environment.
  - Validate the image names in the Kubernetes YAML files.

- **Services Not Reachable**  
  - Confirm pods are running: `kubectl get pods`
  - Double-check service ports and types.
  - Inspect pod logs for errors.

- **Minikube Issues**  
  - Restart Minikube if necessary:

    ```bash
    minikube stop && minikube start
    ```

  - Reset Minikube:

    ```bash
    minikube delete && minikube start
    ```

---

## 📚 Additional Resources

- [Minikube Official Documentation](https://minikube.sigs.k8s.io/docs/)
- [Kubernetes Official Documentation](https://kubernetes.io/docs/)
- [Docker Official Documentation](https://docs.docker.com/)

---
```

---

