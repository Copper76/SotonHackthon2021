#!/bin/bash

sudo docker build -t custom-gpu-tf .
#sudo docker run -e DISPLAY=$DISPLAY -v $(pwd)/:/home -u $(id -u):$(id -g) --runtime=nvidia -it custom-gpu-tf bash
sudo docker run -p 8888:8888 -v $(pwd)/:/home -u $(id -u):$(id -g) --runtime=nvidia -it custom-gpu-tf bash
