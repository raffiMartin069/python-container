FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

RUN sudo apt-get update && sudo apt-get upgrade -y && \
    sudo apt-get install -y postgresql  && \
    sudo apt-get install -y postgresql-common && \
    sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh && \
    apt-get clean
