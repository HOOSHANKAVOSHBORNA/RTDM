# Kubernetes

- install kubectl

  - go steps official documentation with very good VPN :/
  - also we have `kubectl` folder downloaded in this path

    - check file is ok
      ```shell
      echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
      ```
    - move files in root and user

      ```shell
      sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

      sudo install -o root -g root -m 0755 kubectl /home/$USER/.local/bin/kubectl
      ```

- install minikube

---

## Courses

### Kubernetes Explained in 100 Seconds

- automating containrized cloud
- we need a manager to manage our containers
  that is kubernetes or k8s
- a system deployed on k8s called **cluster**
- the brain of this system called **control plane**
  - control plane handles internal and external api requests
  - it has **etcd** a key-value database
    - stores data about the cluster
- workers machines called **nodes**
- each nodes running **kubelet**
- kubelets are connected to the **control plane**
- inside of each nodes we have multiple **pods**
- pods are smallest deployable unit of kubernetes
- pods are containers running togethers
- kubernetes can automatically scale the app horizontally
  by adding more nodes to the cluster and handles
  - networking
  - security
  - system storage
  - ...
- kubernetes is for high availability
- **replica set** is the pods set
- we define all of configs of our cluster on a yaml file

- End

---

### FCC - Full Beginners tutorial

- open-source, free to use
- automatic deployment of containerized applications
  across different servers
- servers can be bare metal or virtual (more common nowadays)
- k8s does:
  - distribution of loads
  - auto scaling
  - monitoring and health check
  - replacement failed containers
- supported containers for k8s:
  - docker
  - cri-o
  - containerd
- pod is the smallest unit in k8s world
- in docker world container is
- inside pod we have multiple containers
- inside pod we have shared volums of containers and
  shared ip addresses!
- the most common usecase of k8s is to have one
  container per pod!
- k8s cluster is set of nodes
- each node is a server (bare metal or virtual)
- each node has pods
- each pod has containers
- we have a master node
- and so worker nodes
- master node just can handle worker nodes
  not any additional work also called control plane
- in each node we have
  - kubelet
    - a service that communicate with api server
      in master node
  - kube-proxy
    - responsible for network between nodes
  - container-runtime
    - run containers inside each nodes
- in master node we have
  - api server service
  - scheduler service
    - responsible for distribution load between different nodes
      in the cluster
  - kube controller manager service
    - controls everything in the cluster
  - cloud controller manager service
    - communicate k8s with cloud provider
  - etcd
    - simple database stores logs related to operation of the cluster
  - dns
    - name resolution for entire cluster networking
- kubectl
  - sperate cli tool
  - allows you to connect and manage cluster remotely
  - communicate by REST api (HTTPS) with api service on master node
- each pod make a namespace and containers in it have same namespace
- pods are toys of master node not you

- starting practical part of the course

- for using the kubernetes we should use from
  distributions not the kubernetes itself because it
  is not practical so much
- some distros contains:
  - k3s (open-source)
  - microk8s (free)
- one distro for learning and developing purpose is:

  - **minikube**

- install kubectl

  - go steps official documentation with very good VPN :/
  - also we have `kubectl` folder downloaded in this path go to it

    - move files in root and user

      ```shell
      sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

      sudo install -o root -g root -m 0755 kubectl /home/$USER/.local/bin/kubectl
      ```

- install minikube

  - go steps official documentation with very good VPN :/
  - also we have `minikube` folder downloaded in this path go to it
    ```shell
    sudo install minikube-linux-amd64 /usr/local/bin/minikube
    ```

- see minikube status:
  ```shell
  minikube status
  ```
- see minikube profiles:
  ```shell
  minikube profile list
  ```
- running minikube:
  ```shell
  minikube start --driver=<your-driver>
  ```
  > if you don't choose driver it finds and selects automatically
- drivers can be:
  - linux
    - docker (it also pull required images)
  - windows
    - hyperv
    - virtualbox
  - macos
    - virtualbox
- after that you should login to minikube:
  ```shell
  ssh -i $(minikube ssh-key) docker@$(minikube ip)
  ```
- in default we have many runned docker containers
  that are noted services for control plane node

- see nodes
  ```shell
  kubectl get nodes
  ```
- see pods
  ```shell
  kubectl get pods --namespace=<your-namespace>
  ```
- for finding ips of pods you can add `-o wide` flag.
-
- see namespaces
  ```shell
  kubectl get namespaces
  ```
- if you don't say your namespace for your running pods it
  runs on the `default` namespace.

- run pods on a node

  ```shell
  kubectl run <arbitary-pod-name> --image=<image-name>
  ```

- see details of a pod

  ```shell
  kubectl describe pod <pod-name>
  ```

- it is possible to make just one pod with `kubectl run` command

- delete pod

  ```shell
  kubectl delete pod <pod-name>
  ```

- new deployment

  ```shell
  kubectl create deployment <dep-name> --image=<image-name>
  ```

- see deployments

  ```shell
  kubectl get deployments
  ```

- deployment manages pods

- see details of deployment

  ```shell
  kubectl describe deployment <dep-name>
  ```

- each pod maps to a deployment with label as a key
  and deployment selector as value

- replicaset show pods count in one deployment
  the default count is 1

- each pod start with replicaset name

- see details of object

  ```shell
  kubectl describe <object-type> <object-name>
  ```

- increasing/descreasing pods on deployment

  ```shell
  kubectl scale deployment <dep-name> --replicas=<arbitary-pods-count>
  ```

- for using deployments we should
  define services that expose a port but also now
  we cannot connect from cluster outside just in cluster is possible

- create new service

  ```shell
  kubectl expose deployment <dep-name> --port=<port> --target-port=<t-port>
  ```

- here is k8s magic that loads balance on servers (nodes) with one port
  actually multiple pods in multiple nodes ips assign to a single ip of
  deployment.

- delete deployment

  ```shell
  kubectl delete deployment <dep-name>
  ```

- delete service

  ```shell
  kubectl delete svc <svc-name>
  ```

- making accessible deployment from cluster outside with port

  ```shell
  kubectl expose deployment <dep-name> --type=NodePort --port=<port> --target-port=<t-port>
  ```

- see running service accissble

  ```shell
  minikube service <service-name>
  ```

- create loadbalancer type service

  ```shell
  kubectl expose deployment <dep-name> --type=NodePort --port=<port> --target-port=<t-port>
  ```

- update kuber image

  ```shell
  kubectl set image deployment <dep-name> <image-name>=<new-image-name>
  ```

- watching rollout statuses

  ```shell
  kubectl rollout status deploy <dep-name>
  ```

- when you create a deployment with
  a replica number you can't remove
  a pod totally if your remove it
  it restart after some times!

- now see some ui

  ```shell
  minikube dashboard
  ```

- remove all things of all things

  ```shell
  kubectl delete all --all
  ```

- all of the things to now was
  commands by commands and we can
  do all in just one config file!

- it is recommended to install kubernetes
  plugin for vscode to write config
  files of kubernetes

- `deployment.yaml`
  ```shell
  kubectl apply -f deployment.yaml
  ```
- `service.yaml`
  ```shell
  kubectl apply -f service.yaml
  ```
- delete applies

  ```shell
  kubectl delete -f deployment.yaml -f service.yaml
  ```

- End

---

### How to run Spark on Kubernetes like a pro (youtube)

- spark deployment modes
  - hadoop yarn
  - apache mesos
  - kubernetes
  - standalone
