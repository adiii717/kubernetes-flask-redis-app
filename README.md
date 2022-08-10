# kubernetes-flask-redis-app

## Deploy redis from the official documentation

```sh

kubectl apply -f https://k8s.io/examples/application/guestbook/redis-leader-deployment.yaml
kubectl apply -f https://k8s.io/examples/application/guestbook/redis-leader-service.yaml
# follower-deploy
kubectl apply -f https://k8s.io/examples/application/guestbook/redis-follower-deployment.yaml
kubectl apply -f https://k8s.io/examples/application/guestbook/redis-follower-service.yaml
```


### Build docker image

```sh
# for linux/platform
docker build --platform linux/x86-64 -t adiii717/demo-app:flask-redis-demo-app .
```


### Deploy Flas application

```sh
kubectl apply -f guestbook-deployment.yaml
kubectl get pods
```