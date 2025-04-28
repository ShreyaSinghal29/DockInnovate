

---

# 🚀 Deploying a Streamlit Application in Docker on AWS EC2

## 📜 Table of Contents
1. 🛠 Setting Up Virtual Networking  
2. 🖥️ Provisioning an EC2 Instance  
3. 🔗 Connecting to EC2 Instance via SSH  
4. 🔑 Configuring PEM Key Permissions  
5. 🐳 Installing and Configuring Docker on EC2  
6. 📂 Uploading Project Files to EC2  
7. 🏗️ Building and Running Docker Containers  
8. 🌐 Accessing the Streamlit Application  
9. 🔄 Managing Docker Containers  

---

## 1️⃣ Setting Up Virtual Networking

### 1.1 Create a New Virtual Network  
1. Go to **AWS Console → VPC Dashboard**.  
2. Click **Create VPC**.  
3. Set the following parameters:  
   - **VPC Name:** CustomVPC  
   - **IPv4 CIDR Block:** `192.168.0.0/16`  
4. Click **Create VPC**.

### 1.2 Create a Subnet  
1. Navigate to **VPC Dashboard → Subnets → Create Subnet**.  
2. Select **CustomVPC**.  
3. Fill in:  
   - **Subnet Name:** PublicSubnet  
   - **CIDR Block:** `192.168.1.0/24`  
   - **Availability Zone:** Choose a zone.  
4. Click **Create Subnet**.

### 1.3 Enable Auto-Assigning Public IPv4  
1. Go to **Subnets**.  
2. Select **PublicSubnet**.  
3. Click **Actions → Modify Subnet Settings**.  
4. Enable **Auto-assign Public IPv4 address**.  
5. Click **Save changes**.

### 1.4 Create an Internet Gateway  
1. Navigate to **VPC Dashboard → Internet Gateways**.  
2. Click **Create Internet Gateway**.  
3. Name it **IGateway** and click **Create**.  
4. Attach it to **CustomVPC**:  
   - Select **IGateway**.  
   - Click **Actions → Attach to VPC → Choose CustomVPC**.  
   - Click **Attach**.

### 1.5 Set Up a Route Table  
1. Go to **VPC Dashboard → Route Tables**.  
2. Click **Create Route Table**.  
3. Name it **PublicRouteTable**, select **CustomVPC**, and click **Create**.  
4. Select **PublicRouteTable**, navigate to the **Routes** tab.  
5. Click **Edit routes → Add route**:  
   - **Destination:** `0.0.0.0/0`  
   - **Target:** Choose **IGateway**.  
6. Click **Save changes**.

### 1.6 Associate Subnet with the Route Table  
1. Navigate to **Route Tables**.  
2. Select **PublicRouteTable**.  
3. Click **Subnet Associations → Modify Subnet Associations**.  
4. Select **PublicSubnet** and click **Save**.

---

## 2️⃣ Provisioning an EC2 Instance

### 2.1 Create an EC2 Instance  
1. Go to **EC2 Dashboard → Instances → Launch Instance**.  
2. Configure:  
   - **Instance Name:** StreamlitServer  
   - **AMI:** **Amazon Linux 2023**  
   - **Instance Type:** t2.micro (Free Tier)  
   - **Key Pair:** Use an existing key pair or create a new one.  
   - **Network Settings:**  
     - **VPC:** Select **CustomVPC**.  
     - **Subnet:** Select **PublicSubnet**.  
     - **Auto-assign Public IP:** Enabled.  
   - **Security Group:**  
     - Allow **SSH (port 22)**.  
     - Allow **HTTP (port 80, optional)**.  
     - Allow **Streamlit (port 8501)**.  
3. Click **Launch Instance**.

---

## 3️⃣ Connecting to EC2 Using SSH

1. Go to **EC2 Dashboard → Instances**.  
2. Select **StreamlitServer**.  
3. Click **Connect**.  
4. Choose **EC2 Instance Connect (browser-based SSH)**.  
5. Click **Connect** to open the terminal.

---

## 4️⃣ Configuring PEM Key Permissions

Move your `.pem` file to the working directory:
```sh
mv /path/to/your-key.pem ~/working-directory/
```

Set the proper permissions:
```sh
chmod 600 your-key.pem
```

---

## 5️⃣ Installing and Configuring Docker on EC2

1. Update the package list:
```sh
sudo yum update -y
```
2. Install Docker:
```sh
sudo yum install -y docker
```

3. Enable and start Docker:
```sh
sudo systemctl enable docker
```

```sh
sudo systemctl start docker
```

---

## 6️⃣ Uploading Project Files to EC2

Transfer the necessary project files using SCP:
```sh
scp -i your-key.pem app.py Dockerfile requirements.txt model.pkl ec2-user@your-ec2-public-ip:/home/ec2-user/
```

---

## 7️⃣ Building and Running Docker Containers

1. Navigate to the project directory:
```sh
cd /home/ec2-user/
```
2. Build the Docker image:
```sh
sudo docker build -t streamlit-app .
```
3. Run the container:
```sh
sudo docker run -d -p 8501:8501 --name streamlit_app_container streamlit-app
```

---

## 8️⃣ Accessing the Streamlit Application

1. Open a browser and enter:
```sh
http://your-ec2-public-ip:8501
```
You should now see the Streamlit application running.

---

## 9️⃣ Managing Docker Containers

1. Check the running containers:
```sh
sudo docker ps
```
2. Stop the container:
```sh
sudo docker stop streamlit_app_container
```
3. Remove the container:
```sh
sudo docker rm streamlit_app_container
```
4. Restart the container:
```sh
sudo docker start streamlit_app_container
```

---

## 🎯 Conclusion

In this guide, you learned how to:

- Set up a **custom VPC**, subnet, and **Internet Gateway**.
- Launch and configure an **EC2 instance**.
- Install **Docker** and run a **Streamlit application** inside a Docker container.
- Access the app via its **public IP**.

This setup ensures your application is **scalable, secure, and easy to manage**. 🚀

--- 

With these new names, the setup is functionally the same but gives everything a fresh perspective.