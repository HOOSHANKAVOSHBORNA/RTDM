#!/bin/bash

# start message
echo "Lesse Abow"

# load `registry` image from file!
sudo docker load -i registry-image.tar

# run docker from prepared volume
sudo docker run -v ./regvol:/var/lib/registry --restart=always --name hooshanreg -p 5000:5000 registry



