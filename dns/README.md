Simple Practical to understand Kubernetes DNS

1. Deploy the Deployment and Service with `kubectl apply -f <file.yml>`
2. Run a simple pod with,
   
```
apiVersion: v1 
kind: Pod 
metadata:
  name: test-dns
  namespace: default
spec:
  containers:
  - name: alpine
    image: alpine
    command: ["sh", "-c", "tail -f /dev/null"]

```
Then,

`kubectl apply -f <pod.yml>`

3. Enter the pod `kubernetes exec -it <pod-name> -- /bin/sh`
4. try `nslookup <service-name>`

You will find the FQDN which shows the work of internal DNS of kubernetes 
