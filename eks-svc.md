## eks
```
AWS Region

    |
    +------ VPC
             |
             +------ Public Subnets
             |
             +------ Private Subnets
                         |
                         +------ Worker Nodes (EC2)
                                      |
                                      +------ kubelet
                                      |
                                      +------ Pods

Control Plane
(API Server)
Scheduler
Controller Manager
etcd
Managed by AWS
```

### NodePort vs LoadBalancer

In the yaml file
```
ports:
- protocol: TCP
  port: 80  #this is the service port
  targetPort: 80 #this is the container port which should match with the service running in container
type: LoadBalancer
```

In LoadBalancer, you will get a external IP to reach to your service
```
Tue Jul 21:22:51:47:~/eks $ kubectl get svc
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP                                                               PORT(S)        AGE
kubernetes   ClusterIP      10.100.0.1      <none>                                                                    443/TCP        24m
nginx-svc    LoadBalancer   10.100.41.244   a15fd9a27087f4d33be0136834314846-138694366.ap-south-1.elb.amazonaws.com   80:30879/TCP   9m59s
```

[4 Types of k8s Service](https://bytebytego.com/guides/top-4-kubernetes-service-types-in-one-diagram/)

If you are using NodePort then the way is different how you use to reach the service. Click on above link to find out.

```
  ports:
  - protocol: TCP
    port: 8080 
    targetPort: 80  
  type: NodePort
```
Then you find the service on NodePublicIp:NortPort
```
Tue Jul 21:23:10:41:~/eks $ kubectl get svc
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
kubernetes   ClusterIP   10.100.0.1      <none>        443/TCP          43m
nginx-svc    NodePort    10.100.41.244   <none>        8080:30879/TCP   28m
```
so curl on `<node-public-ip>:30879` and you will reach the service

>Note : Remeber to add 30879 or any port which auto assigns to the nodeport to inbound of aws sercurity group 
