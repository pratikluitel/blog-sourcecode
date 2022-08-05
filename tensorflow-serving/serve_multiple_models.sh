#!/bin/bash

docker pull tensorflow/serving && \
docker run -t --rm -p 8501:8501 \
    -v "$(pwd)/models/:/models/" \
    tensorflow/serving \
    --model_config_file=/models/models.config