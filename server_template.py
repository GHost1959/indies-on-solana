import grpc
from concurrent import futures
import time
from cryptography.fernet import Fernet
import base64
import command_pb2
import command_pb2_grpc

key = Fernet.generate_key()
cipher = Fernet(key)

class CommandServiceServicer(command_pb2_grpc.CommandServiceServicer):
    def CommandStream(self, request_iterator, context):
        for request in request_iterator:
            client_id = request.client_id
            report = request.report
            print(f"Report from {client_id}: {report}")

            command = f"echo Command for {client_id} at {time.time()}"
            encrypted_data = cipher.encrypt(command.encode())
            yield command_pb2.CommandResponse(
                command=command,
                encrypted_data=base64.b64encode(encrypted_data)
            )
            time.sleep(5)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    command_pb2_grpc.add_CommandServiceServicer_to_server(CommandServiceServicer(), server)
    server.add_secure_port('[::]:443', grpc.ssl_server_credentials(
        [(open('server.crt', 'rb').read(), open('server.key', 'rb').read())]
    ))
    print("Server streaming on port 443...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()