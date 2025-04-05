# ☁️ AKS Microservices Deployment with Helm, Terraform, and CI/CD

This project demonstrates a full end-to-end DevOps pipeline using **Azure Kubernetes Service (AKS)**. It automates infrastructure provisioning with **Terraform**, containerizes a Python Flask app with **Docker**, and uses **Helm** for Kubernetes deployments. Monitoring is handled via **Prometheus + Grafana**, and CI/CD is implemented using **Azure DevOps Pipelines**.


---

## 🧱 Architecture & Tools Used

| Layer               | Tools/Services                                                  |
|--------------------|------------------------------------------------------------------|
| 🚀 Infrastructure   | Terraform, Azure AKS                                             |
| 📦 App Container    | Python Flask, Docker, Azure Container Registry (ACR)             |
| 📈 Monitoring       | Prometheus, Grafana, Node Exporter                               |
| 🔐 Secrets Mgmt     | Azure Key Vault via CSI Driver                                   |
| 🛠 Deployment       | Helm, Kubernetes YAMLs                                           |
| 🔄 CI/CD            | Azure DevOps Pipelines                                           |

---

## 🔧 Diagram

![Diagram](https://raw.githubusercontent.com/mermaid-js/mermaid-live-editor/main/public/img/architecture-example.png)

_(Optional: Replace with your own if you want something custom)_

