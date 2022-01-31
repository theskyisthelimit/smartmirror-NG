# smartmirror-NG

## Hardware

You'll need the following Hardware for your magicmirror

- [Raspberry Pi 4](https://www.digitec.ch/de/s1/product/raspberry-pi-4-8g-model-b-armv8-entwicklungsboard-kit-13276941?supplier=406802)
  - [Raspberry Pi 4 power adapter](https://www.digitec.ch/de/s1/product/raspberry-pi-official-raspberry-pi-4-power-adapter-netzteil-elektronikzubehoer-gehaeuse-11268330?supplier=406802)
  - [Raspberry Pi 4 passive cooling](https://www.digitec.ch/de/s1/product/joy-it-pi-4b-block-gehaeuse-elektronikzubehoer-gehaeuse-12043378)
  - [MicroSDXC card](https://www.digitec.ch/de/s1/product/sandisk-extreme-pro-microsd-a2-microsdxc-128-gb-u3-uhs-i-speicherkarte-9671111?supplier=406802)
  - [Raspberry Pi micro HDMI cable](https://www.digitec.ch/de/s1/product/raspberry-pi-micro-hdmi-typ-d-hdmi-typ-a-1-m-hdmi-video-kabel-11268480)
  - [Pir Sensor](https://www.digitec.ch/de/s1/product/hc-sr501-pir-sensor-elektronikmodul-8193990?supplier=406802)
- Monitor
  - High Contrast
  - IPS Panel or OLED Panel
  - HDMI Input
  - Needs to have a proper Standby-mode
  - Monitor must turn on as soon as power is plugged in
- Picture Frame
- Spy Glass
  - e.g. [Mirropane Chrome Spy 4 MM](https://www.brigla-shop.de/spiegel-smart-mirror)


## Software

## Installation Guide

### Install Docker on Raspberry Pi

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

### Run Watchtower

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

### Start magicmirror with docker-compose

1. Download the [docker-compose.yml](docker-compose.yml) file from this repository
2. create an `mm.env` file with the following variables

  ```
  mm_TZ=Europe/Zurich
  mm_configpath=XXX
  mm_configpath_mmpm=XXX
  ```
3. Use Portainer Stacks to create a new Stack and import your env file.

You can also use docker-compose manually if you want:

   ```sh
   docker-compose --env-file mm.env up
   ```
