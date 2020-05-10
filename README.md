# icavtech-challenge
This repo consists of code for icavtech challenge 

Below are the list of files which consists of the piece of code
1. app.py
2. Dockerfile
3. manifest.yml
4. azure-pipelines.yml
5. Jenkinsfile

# app.py
 
 This file consists of the Python code which prints the Hostname where the Python script wil be executed. Here we are using `Flask`, a web framework to run the Python script as a web application.
 Steps to run the python script.
 
 `$ py app.py`
 
 > Note: Since `Flask` framework was used, it should be downloaded up-front. It can be downloaded using pip.
 > `$ pip install flask`
 
 # Dockerfile
  This file consists of steps how `app.py` file is dockerized so the Python webapplication will run inside the Docker container.
  Steps to run the docker build manually (below command should be run under the path where `Dockerfile` is present)
  
  `$ docker build -t webapp:v1.0 .`
   > This creates the Docker image on your local machine and tags it with v1.0 as mentioned in the above command.
   
   `$ docker run -it -p 5000:5000 webapp:v1.0`
   > This start the Python application running inside a newly created container and that application can be access from our local machine (browser) using the URL htttp://localhost:5000
   
 # manifest.yml
   This file consists of the code by which deploys the above docker image on Kubernets. Here we are cloning the Docker image from the ACR (Azure Container Registry), so before executing the manifest.yml file below pre-requestis needs to be satisfied.
   
   `kubectl apply -f manifest.yml`
   
   To run the this script on local, Azure login is required since it pulls the code from ACR and kubectl secert needs to be run - which will be used in `manifest.yml` script.
   
   ###### Prerequisites
   > Azure login `$az login`  -> Should have login to Microsoft Azure
   
   > Login to  ACR `$az acr login -n icavtechicontainer` -> Should have access to ACR
   
   > Generate secert `kubectl create secret docker-registry icavtechicontainer --docker-server=icavtechicontainer.azurecr.io  --docker-username=icavtechicontainer --docker-password=32wxxxxxxxxkxZxxxxxxxxxxKbFAD5l/ --docker-email=rajesh.matta712@gmail.com`
 
 # azure-pipelines.yml
   This is the final `Build-Deployment` script which does the Docker build, push the generated Docker image to ACR and finally deploys the same Docker image on AKS (Azure Kubernetes Services) which is end-to-end automated which was tested on AzureDevops pipeline.
   
   ###### Prerequisites
   > Need to generate the connection strings from AzureDevops Pipeline to ACR (Azure Container Registry) and AzureDevops to AKS (Azure Kubernetes Services)
   `AzureDevops` -> `Project Settings` -> `Service connections` -> `New Service Connection`
   
   So this names which are configured under Service Connections will be used in `azure-pipeline.yml` file as below :
       `ICAV_Azure_Container_Registry` is the connection string name used to connect ACR.
       `ICAV_Azure_K8` is the connection string name used to connect AKS.
   
 # Jenkinsfile 
   This file can be ignored, since are already using `azure-pipelines.yml` for CI/CD pipeline and can be used under AzureDevOps so we may not be required to use Jenkinsfile as no scope of using Jenkins tool here. It can be achived by AzureDevOps
