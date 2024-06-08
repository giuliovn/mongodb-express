## SETUP
1. Install `minikube`
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
```
2. Install `kubectl`
```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```
3. `minikube start`
4. `minikube addons enable ingress`
5. Simulate an external secret (with whatever credentials):
```bash
kubectl create secret generic cred --from-literal=user=mario --from-literal=password=mario
```
6. `helm install cluster ./k8s`
7. Get the minicluster IP with `minikube ip` and open in browser.
8. `minikube tunnel`
9. Access the IP from the `minikube ip` command from the browser
