# Using Docker *Portable*

## How to use?

1. `docker` should be installed on machine.
2. edit docker config files (`/etc/docker/daemon.json`) in host machine and client machine:
    ```json
    {
        "experimental": false,
        "insecure-registries": ["192.168.1.103:5000"]
    }
    ```
4. run in terminal:
    ```bash
    sudo docker compose up
    ```
5. go to [Link](http://192.168.1.103:5000/v2/_catalog) to see available images.
6. pull and push your images on registry:
    ```bash
    sudo docker pull 192.168.1.103:5000/<image-name>
    ```
7. it's done!

> ***you should restart your docker after new configs***.


## Docs

- pull registry image from `Dockerub`
    ```bash
    sudo docker pull registry
    ```
    
- store pulled images on your machine in file for transfering
    ```bash
    docker save -o <save-location>/<file-name>.tar <image-name>
    ```

- load image from file to machine
    ```bash
    docker load -i <image-file-path>.tar
    ```

- run image to specific volume (for read and write)
    ```bash
    sudo docker run --rm -v ./regvol:/var/lib/registry --name hooshan-registry -p 5000:5000 registry
    ```

- add image to registry:
    ```bash
    sudo docker tag <image-name> <your-registry-address>/<image-name>
    sudo docker push <your-registry-address>/<image-name>
    ```

- remove all docker images:
    ```bash
    sudo docker rmi -f $(sudo docker images -aq)
    ```

- remove all docker containers:
    ```bash
    sudo docker rm -vf $(sudo docker ps -aq)
    ```
    ```
    sudo docker container prune 
    ```

> in docker volume mounting it is possible that 
> does not work correctly and you lose your data!
> because default mode in docker volume plugging 
> is `:mrw` that contains `mknod` that cause unauthorized not accessible,
> so you should specify `:rw` to remove `mknod` mode.