```markdown
# 🍪 Easy Windows Server Setup on AWS (For Beginners)

## 🌟 What You’ll Learn

This guide walks you through building a reusable, pre-configured Windows Server on AWS with:

✅ IIS (Web Server) pre-installed  
✅ Automatic setup — no manual steps after launch  
✅ A reusable Amazon Machine Image (AMI) for future use

---

## 🧰 What You’ll Need

- A Windows PC  
- An AWS account (Free Tier is fine)  
- About 30 minutes  

---

## 🔧 Step 1: Install Required Tools

### 1️⃣ Install Packer

- [Download Packer](https://developer.hashicorp.com/packer/downloads)  
- Extract `packer.exe` to `C:\packer`  
- Add `C:\packer` to your system **PATH**:
  - Press `Windows + R`, type `sysdm.cpl`, hit Enter  
  - Go to **Advanced → Environment Variables**  
  - Under **System Variables**, edit the `Path` and add `C:\packer`

### 2️⃣ Install AWS CLI

- Download the installer from the [AWS CLI page](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html)  
- Run the installer (click Next through the steps)

### 3️⃣ Set Up AWS CLI Credentials

Open PowerShell and run:

```powershell
aws configure
```

Enter:
- **AWS Access Key ID**  
- **AWS Secret Access Key**  
- **Default Region Name**: `us-east-1`  
- **Output Format**: `json`

---

## 📝 Step 2: Create Your Server Recipe

### 📄 Create a file: `windows-server-recipe.pkr.hcl`

```hcl
packer {
  required_plugins {
    amazon = {
      source  = "github.com/hashicorp/amazon"
      version = ">= 1.0.0"
    }
  }
}

source "amazon-ebs" "windows-server" {
  ami_name      = "my-windows-server-{{timestamp}}"
  instance_type = "t2.large"
  region        = "us-east-1"
  source_ami_filter {
    filters = {
      name = "Windows_Server-2022-English-Full-Base-*"
    }
    owners = ["amazon"]
  }
  communicator    = "winrm"
  winrm_username  = "Administrator"
}

build {
  sources = ["source.amazon-ebs.windows-server"]

  provisioner "powershell" {
    script = "setup.ps1"
  }
}
```

### 📄 Create a PowerShell script: `setup.ps1`

```powershell
# Enable IIS (Web Server)
Install-WindowsFeature -Name Web-Server -IncludeAllSubFeature

# Add a basic welcome page
Add-Content -Path "C:\inetpub\wwwroot\index.html" -Value "<h1>Welcome to your auto-configured Windows Server!</h1>"
```

---

## 🚀 Step 3: Build Your Custom AMI

In the folder with both files, open PowerShell and run:

```powershell
packer init .
packer validate windows-server-recipe.pkr.hcl
packer build windows-server-recipe.pkr.hcl
```

This will:
- Launch a temporary Windows instance on AWS  
- Automatically install IIS  
- Save the final setup as a reusable AMI image

---

## 🖥️ Step 4: Launch and Use Your Server

1. Log in to your [AWS EC2 Console](https://console.aws.amazon.com/ec2)  
2. Go to **Images → AMIs** in the left sidebar  
3. Select your custom AMI and click **Launch Instance**  
4. Choose your instance type (e.g., `t2.large`) and complete the wizard  
5. Connect via RDP (Remote Desktop Protocol) using the instance’s public IP  
6. Visit your server in the browser:  
   ```
   http://<your-server-ip>
   ```

You should see your custom welcome message!

---

## ✅ Done!

You've successfully created a Windows Server on AWS that configures itself — ready for any future deployment.

---
```

