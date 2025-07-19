import grpc
from concurrent import futures
from prometheus_client import start_http_server, Counter
import user_pb2
import user_pb2_grpc


REQUEST_COUNTER = Counter('get_user_requests_total', 'Total number of GetUser requests')


class UserService(user_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        REQUEST_COUNTER.inc()
        return user_pb2.UserResponse(id=request.id, name="Nabeel", email="mnabeelasad@gmail.com")

def serve():
    start_http_server(8000)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started at port 50051")
    print("gRPC Server started at port 50051 with /metrics on 8000")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
