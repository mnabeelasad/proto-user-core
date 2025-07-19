import grpc
from user_service import user_pb2
from user_service import user_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = user_pb2_grpc.UserServiceStub(channel)
response = stub.GetUser(user_pb2.UserRequest(id=1))
print(f"ID: {response.id}, Name: {response.name}, Email: {response.email}")
