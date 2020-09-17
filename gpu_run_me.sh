#!/bin/bash
echo "Docker building GPU-enabled version..."
docker build -t devbox .

# Up time
docker run  \
        -it \
        --runtime=nvidia \
        --gpus all \
        --rm \
        -v ~/src/apps/devbox:/devbox \
       devbox
