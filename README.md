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
- Duct Tape?

## Software
- [Magicmirror](https://github.com/MichMich/MagicMirror)
- [Docker](https://www.docker.com/)
- [Portainer](https://www.portainer.io/)
- [Watchtower](https://github.com/containrrr/watchtower)
- [PM2](https://pm2.keymetrics.io/)
- Webhook
- Python

## Installation Guide

```sh
Sudo apt update & sudo apt upgrade
```

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
      Portainer:
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

You can also use docker-compose manually if you are not afraid:

```sh
docker-compose --env-file mm.env up
```

### Copy Scripts

Copy all the bash (*.sh) scripts from this repository to your raspberry pi on to your home folder or you can also create a subfolder. It's up to you

ID | Name          | Description
---|---------------|-------------------------------------------------------------------------------------------------------------------------
1  | mm.sh         | (gotta check this) This script is starts the magicmirror software. I's configured to run magicmirror in clientonly mode.
2  | monitor_on.sh | This script will is being used by the pir sensor script. When a motion is detected this script will turn on the display.
3  | monitor_off.sh | This script will is being used by the pir sensor script. When no motion is detected in a certain time, the display will shut off.
4  | pir.py  | This script will is controlling the behavior of the pir sensor. you can configure the PIR_PIN, LED_PIN and the SHUTOFF_Delay  
5  | reboot.sh  | This script is being used to reboot the raspberry pi with webhooks  
6  | reload.sh  | This script will reload the pm2 instance on your raspberry pi without needing to restart the whole computer
7  | webhook.sh  | This script is being used to start your webhooks
8  | check_inet.sh  | In the past several years my raspberry pi 3 lost the internet connection several times. When this happens magicmirror will stall. This script monitors if the raspberry pi lost connection to the internet. if so, it will restart.

```sh
chmod 777
```

### Install pm2

```sh
sudo npm install -g pm2
sudo pm2 startup
pm2 start mm.sh
pm2 save
```

### pm2 controls

#### Restart

```sh
pm2 restart mm
```

#### stop
```sh
pm2 stop mm
```
#### Show logs
```sh
pm2 logs mm
```
#### Show process informations
```sh
pm2 show mm
```

### Install webhook
```sh
sudo apt update
sudo apt install webhook
```

### RPi.GPIO Python Library (Check if it works without)

```sh
sudo apt-get update
sudo apt-get install rpi.gpio
```

### crontab configuration
```sh
crontab -e
```

```
00 00 * * * cd /home/pi/MagicMirror/ && git pull
0 00 * * * /home/pi/reload.sh
0 12 * * * /home/pi/reload.sh
*/5 * * * * /home/pi/check_inet.sh
```
