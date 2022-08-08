## How to:

1. Read [the blog post](https://pratikluitel.com.np/2022/08/06/tensorflow-serving/){:target="_blank"}.
2. [Install docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/). If are on Windows, please install [Docker for Windows](https://docs.docker.com/docker-for-windows/install/), and remember to use WSL (also remember that docker on Windows sucks). If you are on a M1 Mac, pray to your overlords at Apple, because [tensorflow does not work with Docker on M1](https://github.com/tensorflow/tensorflow/issues/52845).
3. Install [python3](https://www.python.org/downloads/), [jupyter notebook](https://jupyter.org/) or [an equivalent](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) and the requirements (a venv is highly recommended):

    ```bash
    pip install -r requirements.txt
    ```

4. Serve your models,
    use
    ```bash
    ./serve_multiple_models.sh
    ```
    to serve both the models behind the same host:port,
    or 
    ```bash
    ./serve_stylization_model.sh && ./serve_super_resolution_model.sh
    ```
    to serve one model on port 8502 and another on port 8501.
    (You might have to `chmod +x *.sh` to make the scripts executable.)

4. Run the notebook: `stylization_and_enhancement.ipynb`, and enjoy the results!