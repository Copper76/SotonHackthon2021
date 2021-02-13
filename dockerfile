FROM tensorflow/tensorflow:nightly-gpu-jupyter

RUN apt-get -y install python3-scipy

# Install python packages
RUN pip install --upgrade pip \
    && pip install \
        matplotlib \
        scipy \
    && rm -fr /root/.cache

