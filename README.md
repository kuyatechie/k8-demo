# k8-barona

Prerequisites
-------------
- Docker Desktop (https://www.docker.com/products/docker-desktop)
Docker Desktop is an application for MacOS and Windows machines, delivering the easiest and fastest way to build production-ready container applications for Kubernetes or Swarm, working with any framework and language and targeting any platform.

- Kubernetes Dashboard (https://github.com/kubernetes/dashboard)
Kubernetes Dashboard is a general purpose, web-based UI for Kubernetes clusters. It allows users to manage applications running in the cluster and troubleshoot them, as well as manage the cluster itself.

To install the kubernetes-dashboard in the kubernetes cluster
``` 
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v1.10.1/src/deploy/recommended/kubernetes-dashboard.yaml
```

To install the RBAC Auth to allow cluster-admin access to the UI
```
kubectl apply -f kubernetes-dashboard/dashboard-admin.yml
```

- Helm (https://github.com/helm/helm)
Helm is a tool for managing Kubernetes charts. Charts are packages of pre-configured Kubernetes resources.
``` 
brew install kubernetes-helm
helm init
```

Creating the Django web application
----------------------------
**Using venv to activate the source folder**
- Create and activate the virtual environment
``` 
virtualenv ~/.virtualenvironments/k8-barona
source ~/.virtualenvironments/k8-barona/bin/activate
```
**Install all required packages**
```
pip3 install -r requirements.txt
```
**Start Django project and Table app**
```
django-admin startproject web
cd web
python3 manage.py startapp table
```



