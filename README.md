This is a simple FastAPI HelloWorld API.

Run `pip install -r requirements.txt` to install the dependencies.

To run the tests 
1. Run command `pytest` in the root folder.

To run the application locally
1. Run `fastapi run app/main.py` in the root folder. 
2. `You can access the APIs at `localhost:8000`

To run the application locally using docker
1. Build the docker image using `docker build . -t pyhelloworld`
2. Run the docker container using the above built image using `docker run -p 8000:8000 pyhelloworld`
3. You can access the APIs at `localhost:8000`

To run the application in a minikube cluster
1. Run `eval $(minikube docker-env)` to use docker daemon from minikube
2. Build the docker image using `docker build . -t pyhelloworld`
3. Run `docker login` to access the image
4. Run `kubectl apply -f k8s/deployment.yaml` to deploy the application in a minikube cluster
5. Run `kubectl port-forward <pod-name> 8000:8000` to expose the port locally 
6. You can access the APIs at `localhost:8000`