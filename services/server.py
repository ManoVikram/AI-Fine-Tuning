import grpc
from concurrent import futures
from proto import service_pb2_grpc, service_pb2

class GeneralService(service_pb2_grpc.GeneralServiceServicer):
    def __init__(self):
        super().__init__()

def serve():
    # Step 1 - Initialize the gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Step 2 - Add the service to the server
    service_pb2_grpc.add_GeneralServiceServicer_to_server(servicer=GeneralService(), server=server)

    # Step 3 - Bind the server to a port
    server.add_insecure_port("[::]:50051")

    # Step 4 - Start the server
    server.start()
    print("gRPC server started on port 50051...")

    # Step 5 - Keep the server running until terminated
    server.wait_for_termination()

if __name__ == "__main__":
    serve()