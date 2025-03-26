🍪 Easy Windows Server Setup on AWS for Beginners
🌟 What You'll Learn
How to create a pre-configured Windows server on AWS with:
✅ Web server (IIS) already installed
✅ Automatic setup - no manual configuration needed
✅ Reusable server template

🛠️ What You Need
A Windows computer

An AWS account (free tier works)

About 30 minutes

🧩 Step 1: Install the Tools
1. Install Packer (Our Server Builder)
Download from Packer's website

Unzip and move packer.exe to C:\packer

Add to PATH:

Press Windows + R, type sysdm.cpl

Go to Advanced → Environment Variables

Add C:\packer to Path

2. Install AWS CLI
Download from AWS CLI page

Run the installer (just click Next)

3. Set Up AWS Keys
powershell
Copy
aws configure
Enter:

Your AWS Access Key

Your AWS Secret Key

Region: us-east-1

Output: json

📝 Step 2: Create the Recipe File
Create windows-server-recipe.pkr.hcl:

hcl
Copy
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
  communicator = "winrm"
  winrm_username = "Administrator"
}

build {
  sources = ["source.amazon-ebs.windows-server"]

  provisioner "powershell" {
    script = "setup.ps1"
  }
}
Create setup.ps1:

powershell
Copy
# Install IIS (Web Server)
Install-WindowsFeature -Name Web-Server -IncludeAllSubFeature

# Create welcome page
Add-Content -Path "C:\inetpub\wwwroot\index.html" -Value "<h1>Hello from your new server!</h1>"
🚀 Step 3: Build Your Server
Open PowerShell

Run:

powershell
Copy
packer init .
packer validate windows-server-recipe.pkr.hcl
packer build windows-server-recipe.pkr.hcl
This will:
🔸 Create a temporary server on AWS
🔸 Install IIS automatically
🔸 Save it as a reusable image

🖥️ Step 4: Use Your New Server
Go to AWS EC2 Console

Find your AMI under "Images → AMIs"

Click "Launch instance"

Connect via Remote Desktop (RDP)

Visit http://[your-server-ip] to see your welcome page!
