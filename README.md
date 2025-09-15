PortfolioSite

PortfolioSite is a full-stack portfolio website showcasing projects, blogs, and professional experience.
It is built using Flask for the backend, Celery + RabbitMQ for asynchronous tasks, MongoDB for database, 
Nginx as a reverse proxy, and HTML/CSS/JS for frontend.
The application is deployed on Google Cloud Platform (GKE & Cloud Run) with a Load Balancer for high availability and scalability.

---

Features

- Dynamic portfolio pages for projects, blogs, and achievements
- Contact form with email notifications handled asynchronously via Celery + RabbitMQ
- MongoDB for storing project data, messages, and user submissions
- Nginx as reverse proxy for Flask backend
- Responsive frontend using HTML, CSS, and JavaScript
- Scalable deployment on GCP with GKE & Cloud Run
- Load Balancer configured for smooth traffic handling

---

Architecture

Frontend (HTML/CSS/JS)
        │
        ▼
     Nginx (Reverse Proxy)
        │
        ▼
     Flask Backend
        │
        ├── MongoDB (Database)
        └── Celery + RabbitMQ (Async Tasks)

Deployed on GCP:
- GKE: Manages containerized Flask + Celery services
- Cloud Run: For serving static frontend or lightweight backend services
- Load Balancer: Routes incoming traffic to appropriate backend services

---

Prerequisites

- Docker & Docker Compose
- Python 3.10+ (for local development)
- MongoDB (if not using Dockerized MongoDB)
- RabbitMQ (for Celery tasks)
- GCP account with access to GKE and Cloud Run

---

Local Setup

1. Clone the repository
   git clone https://github.com/<username>/PortfolioSite.git
   cd PortfolioSite

2. Build and start services using Docker Compose
   sudo docker compose up -d --build

3. Check running containers
   sudo docker ps

4. Stop containers
   sudo docker compose down

---

Deployment on GCP

1. GKE Cluster Setup
   - Create a GKE cluster and configure kubectl context

2. Deploy backend & frontend
   kubectl apply -f k8s/deployment.yaml
   kubectl apply -f k8s/service.yaml
   kubectl apply -f k8s/ingress.yaml

3. Cloud Run Deployment
   - Build and push Docker images to Google Container Registry
   - Deploy Flask backend or static frontend to Cloud Run

4. Configure Load Balancer
   - GCP Load Balancer routes traffic to GKE and Cloud Run services

---

API Endpoints (Backend)

- GET /projects – List all projects
- GET /projects/<id> – Get project details by ID
- POST /contact – Submit contact form (async via Celery)
- GET /messages – Retrieve messages from MongoDB

---

Celery Worker

- Handles asynchronous tasks such as sending email notifications, background processing, or batch updates
- Connects to RabbitMQ for task queue management

---

Nginx

- Serves as reverse proxy for backend API
- Handles SSL termination (optional)
- Routes frontend static assets efficiently

---

Contributing

Contributions, feedback, and suggestions are welcome! Please open an issue or submit a pull request.

---

PortfolioSite is a work-in-progress project designed for showcasing a full-stack deployment with modern backend, frontend, and cloud technologies.
