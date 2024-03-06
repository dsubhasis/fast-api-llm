FROM nvidia/cuda:12.3.1-devel-ubuntu22.04

WORKDIR /llm-app
COPY start.py /llm-app/

RUN apt-get -y update 
RUN apt-get install --yes --no-install-recommends python3.9 python3-pip 
RUN apt-get install --yes --no-install-recommends  git wget curl
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN pip install wheel 
RUN python3 get-pip.py
RUN pip3 install fschat scipy
RUN pip3 install fschat[model_worker,webui] pydantic==1.10.13
# RUN pip3 install fschat[model_worker,webui] pydantic==1.10.13

EXPOSE 8000 7860

CMD ["python3", "start.py"]

