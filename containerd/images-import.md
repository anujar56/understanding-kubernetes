## containerd images
If you build a image using docker build and wants to use it k8s deployment then you need to import that image into containerd image store
> Docker and containerd maintain **separate image stores**
### Save the Docker image

```
docker save -o simple-app-v1.tar simple-app:v1
```

### Import it into containerd

On the control plane:

```
ctr -n k8s.io images import simple-app-v1.tar
```

If `ctr` isn't in your PATH:

```
sudo ctr -n k8s.io images import simple-app-v1.tar
```

Verify:

```
ctr -n k8s.io images ls | grep simple-app
```

----------

### Important: 
The scheduler may place the Pod on `nodes`, which also needs the image.

Repeat the import on **nodes**
