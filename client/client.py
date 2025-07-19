import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../user_service')))

import grpc
import user_pb2
import user_pb2_grpc


channel = grpc.insecure_channel('localhost:50051')
stub = user_pb2_grpc.UserServiceStub(channel)
response = stub.GetUser(user_pb2.UserRequest(id=1))
print(f"ID: {response.id}, Name: {response.name}, Email: {response.email}")
