#!/bin/bash

docker pull tensorflow/serving && \
docker run -t -p 8501:8501 \
    -v "$(pwd)/models/esrgan_super_resolution:/models/super_resolution/" \
    -e MODEL_NAME=super_resolution \
    tensorflow/serving