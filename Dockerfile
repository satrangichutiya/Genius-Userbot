FROM ubuntu:22.04

RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends git ffmpeg python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/

# Install requirements AND pytgcalls manually
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt \
 && pip3 install --no-cache-dir git+https://github.com/pytgcalls/pytgcalls

CMD python3 -m AdityaHalder
