#!/bin/bash

# Laden des Docker-Images aus der .tar-Datei
docker load -i todo.tar

# Starten des Containers
docker run -p 3000:80 -d todo:latest