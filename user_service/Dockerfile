FROM python:3.9
WORKDIR /app
COPY ../proto ./proto
COPY . .
COPY ../requirements.txt .
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/user.proto
CMD ["python", "server.py"]