## AWS k3s installation

## Master node

### Update
```
sudo apt update  
  
sudo apt upgrade -y
```
### Install k3s
```
curl -sfL https://get.k3s.io | sh -
```
### Check service
```
sudo systemctl status k3s
```
### Configure Kubectl
```
mkdir -p ~/.kube  
  
sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config  
  
sudo chown $(id -u):$(id -g) ~/.kube/config
```
### Verify
`kubectl get nodes`

## Worker Node

### First get the token and IP from Master node

```
sudo cat /var/lib/rancher/k3s/server/node-token
hostname -I
```

### Update worker node
```
sudo apt update  
  
sudo apt upgrade -y
```

### Install worker
```
curl -sfL https://get.k3s.io | K3S_URL=https://<ip>:6443 K3S_TOKEN=<token> sh -
```

### Verify from master node
```
kubectl get nodes
```
---
**About Security Groups in aws**
Ports need to open
- 22
- 6443
- 80
- 443



