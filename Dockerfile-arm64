# Используем официальный образ tensoflow как базовый для архитектуры x86_64
#FROM tensorflow/tensorflow:latest
# Используем  образ от bitnami как базовый для архитектуры ARM и x86_64
FROM --platform=arm64 ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV DEB_PYTHON_INSTALL_LAYOUT=deb_system
ENV LANG=C.UTF-8

USER root

####################
# Installing dependencies
####################
RUN apt-get -y update
RUN apt update

RUN apt-get -y install python3-pip python3-numpy swig python3-dev  pkg-config 
#libhdf5-dev
RUN pip3 install wheel
RUN pip install h5py==3.10.0

COPY notebooks  /app/notebooks
COPY texts  /app/texts
COPY tmp  /app/tmp
COPY train_1st  /app/train_1st
COPY train_2nd  /app/train_2nd
COPY fonts  /app/fonts

COPY main.py  /app
COPY requirements.txt /

RUN pip install --no-cache-dir --upgrade-strategy only-if-needed -r requirements.txt

EXPOSE 8888





