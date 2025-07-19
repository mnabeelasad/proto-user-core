# ProtoUserCore

ProtoUserCore is a Python-based microservice using gRPC, designed to handle basic user operations. The service is containerized using Docker and supports monitoring through Prometheus and Grafana. Kubernetes manifests and a CI/CD pipeline (Jenkins) are also included for deployment automation.

---

## Features

- gRPC-based user service with Protobuf
- Exposes basic user data via RPC
- Dockerized for consistent environments
- Monitoring setup using Prometheus and Grafana
- Kubernetes deployment ready (YAML)
- Jenkins pipeline for CI/CD

---

## Tech Stack

- Python 3.9
- gRPC
- Docker / Docker Compose
- Prometheus & Grafana
- Kubernetes
- Jenkins (CI/CD)

---

## Folder Structure

ProtoUserCore/
├── user_service/ # gRPC server code
├── client/ # gRPC test client
├── proto/ # .proto file(s)
├── monitoring/ # Prometheus + Grafana setup
├── k8s/ # Kubernetes deployment files
├── Jenkinsfile # Jenkins pipeline
├── Dockerfile # gRPC service Docker image
├── requirements.txt
└── README.md



---

## How to Run

### 1. Start Monitoring Stack (Prometheus + Grafana)

```bash
cd monitoring
docker-compose up

2. Run the gRPC Server
gRPC server runs at localhost:50051, metrics exposed at localhost:8000

cd user_service
python server.py

3. Kubernetes Deployment
kubectl apply -f k8s/deployment.yaml
