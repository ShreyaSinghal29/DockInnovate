

---

# 🚀 Docker Networking: Achieving Isolation with Custom Bridges

## 🎯 Goal
This exercise focuses on demonstrating **network isolation** in Docker environments. We'll learn how containers within a **custom bridge network** can easily communicate, while containers on different networks remain **segregated**.  
Mastering this behavior is essential for designing secure and scalable microservices architectures.

---

## 🌐 Quick Overview of Docker Networking

Docker enables seamless communication between containers through different networking modes, while maintaining **security** and **control**.

### 📚 Types of Docker Networks:
- **Default Bridge** — Basic container-to-container communication using IPs.
- **Custom Bridge** — Offers advanced control like container name resolution.
- **Host** — Shares the host’s network stack with the container.
- **Overlay** — Connects containers across multiple machines (used with Swarm).
- **Macvlan** — Assigns MAC addresses to containers, treating them like physical devices.
- **None** — No network connectivity at all.

In this project, we'll focus on using a **Custom Bridge Network**.

---

## 🔥 Why Create a Custom Bridge Network?

Benefits of using a custom bridge:
- 🔒 **Enhanced Isolation** — Different bridge networks are isolated by default.
- ⚡ **Efficient Communication** — Internal DNS support for service discovery.
- 🛠️ **Custom Subnets & IP Ranges** — Fine-grained network control.
- 🚀 **Performance** — Bypasses NAT routing used in default bridge mode.

---

## 🛠️ Step 1: Set Up a Custom Bridge Network

Let's create a new network called `shreya-bridge`:

```bash
docker network create \
  --driver bridge \
  --subnet 172.20.0.0/16 \
  --ip-range 172.20.240.0/20 \
  shreya-bridge
```

### 📖 What This Command Does:
- `--driver bridge` — Uses the bridge driver.
- `--subnet` — Sets the CIDR block for the network.
- `--ip-range` — Defines a range of dynamic IPs for containers.

---

## 🛠️ Step 2: Deploy Containers into the Custom Network

### Start a **Redis** instance as `shreya-database`:

```bash
docker run -itd --net=shreya-bridge --name=shreya-database redis
```

### Launch a **BusyBox** container as `shreya-server-A`:

```bash
docker run -itd --net=shreya-bridge --name=shreya-server-A busybox
```

✅ **Note:** Both containers are attached to the `shreya-bridge` network.

---

## 🛠️ Step 3: Check IP Assignments

Inspect the network to view container IPs:

```bash
docker network inspect shreya-bridge
```

Example output:
```
shreya-database: 172.20.240.1
shreya-server-A: 172.20.240.2
```

---

## 🛠️ Step 4: Test Inter-Container Communication

### Ping test from **Redis** to **BusyBox**:

```bash
docker exec -it shreya-database ping 172.20.240.2
```

### Ping test from **BusyBox** to **Redis**:

```bash
docker exec -it shreya-server-A ping 172.20.240.1
```

✅ Both pings should succeed because they share the same custom network.

---

## 🛠️ Step 5: Prove Network Isolation with a New Container

Spin up a container **outside** the custom network:

```bash
docker run -itd --name=shreya-server-B busybox
```
(Uses the **default bridge network**.)

Check its IP address:

```bash
docker inspect -format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' shreya-server-B
```

Example output: `172.17.0.2`

---

## 🛠️ Step 6: Attempt Cross-Network Communication

Try pinging `shreya-server-B` from `shreya-database`:

```bash
docker exec -it shreya-database ping 172.17.0.2
```

🚨 **Expected Result:** **Ping fails** — no communication between containers on different networks by default.

---

## 🛠️ Step 7: Validate Network Membership

Inspect the networks individually:

```bash
docker network inspect shreya-bridge
docker network inspect bridge
```

- `shreya-bridge` ➔ should list `shreya-database` and `shreya-server-A`.
- `bridge` ➔ should list `shreya-server-B`.

---

## 🧠 Summary

- Containers on the **same custom network** can reach each other effortlessly.
- Containers across **different networks** remain **isolated** unless explicitly connected.
- **Custom bridge networks** enhance control, security, and internal DNS-based communication in Docker deployments.

🎯 **You’ve now mastered Docker custom bridge networking principles!**

---

