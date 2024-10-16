FROM continuumio/miniconda3
RUN conda install conda-forge::rdkit

WORKDIR /web

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .