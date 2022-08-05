docker run -t -p 8502:8501 \
    -v "$(pwd)/models/magenta_image_stylization:/models/stylization/" \
    -e MODEL_NAME=stylization \
    tensorflow/serving