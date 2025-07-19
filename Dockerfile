FROM python:3.9
WORKDIR /app
COPY ./proto ./proto
COPY ./user_service ./user_service
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I./proto --python_out=./user_service --grpc_python_out=./user_service ./proto/user.proto
CMD ["python", "user_service/server.py"]
