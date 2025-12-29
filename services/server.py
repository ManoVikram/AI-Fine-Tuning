import os
from dotenv import load_dotenv
import grpc
from concurrent import futures

from openai import OpenAI
from proto import service_pb2_grpc, service_pb2

class GeneralService(service_pb2_grpc.GeneralServiceServicer):
    def __init__(self):
        super().__init__()

    def answer_query(self, query):
        client = OpenAI()
        
        response = client.responses.create(
            model="ft:gpt-4o-mini-2024-07-18:personal::CrqMnjE8",
            input=[
                {"role": "developer", "content": "You are a helpful assistant you helps with user queries."},
                {"role": "user", "content": query}
            ]
        )
        
        return response.output_text


    def Ask(self, request, context):
        query = request.query
        
        response = self.answer_query(query)

        return service_pb2_grpc.GeneralServiceResponse(answer=response)

def serve():
    # Step 0 - Load the environment variables
    load_dotenv()
    assert os.getenv("OPENAI_API_KEY"), "OPENAI_API_KEY is not set in the environment variables."

    # Step 1 - Initialize the gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Step 2 - Add the service to the server
    service_pb2_grpc.add_GeneralServiceServicer_to_server(servicer=GeneralService(), server=server)

    # Step 3 - Bind the server to a port
    grpc_server_port = {os.getenv('GRPC_SERVER_PORT', '50051')}
    server.add_insecure_port(f"[::]:{grpc_server_port}")

    # Step 4 - Start the server
    server.start()
    print(f"gRPC server started on port {grpc_server_port}...")

    # Step 5 - Keep the server running until terminated
    server.wait_for_termination()

if __name__ == "__main__":
    serve()