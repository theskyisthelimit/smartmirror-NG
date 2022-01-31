# smartmirror-NG

## Hardware

## Software

## Installation Guide

### Install Docker

```sh
curl -fsSL https://get.docker.com | sh
```

### Create Volume for portainer data

```sh
docker volume create portainer_data
mkdir /home/pi/docker
mkdir /home/pi/docker/portainer
```

### Run Portainer

```sh
docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v /home/pi/docker/portainer:/data portainer/portainer-ce

```

## Run Watchtower

```sh
docker run -d --name watchtower -v /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower
```

### Example for Portainer Volume with docker-compose
```yaml
    version: "2"
    services:
      XXX:
        container_name: XXX
        privileged: true
        image: XXX:latest
        volumes:
          - Portainer-Volume-Name:/config
        environment:
           - TZ=Europe/Zurich
        restart: always
        network_mode: host
```
