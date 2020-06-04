#!/bin/bash

sudo usermod -aG docker ${USER}

sudo docker stack deploy --compose-file docker-compose.yaml sfia2stack