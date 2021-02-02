# Sample application

This repository represents a Tutorial how to expose sensor Data from the BME280 to a prometheus Service and a Grafana Dashboard


## Prequisites

You need a: 
- Raspberry
- BME280 Sensor

You will need to have the following installed locally to complete this workshop:

- [Docker](https://docs.docker.com/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

If you're running Docker for Desktop for macOS or Windows, Docker Compose is already included in your installation.

```
sudo apt-get update 
sudo apt-get upgrade
sudo pip3 install flask

```

## Running

To start the sample application and the supporting services:

```
docker-compose up -d
```
```
sudo python3 main.py
```

Make sure you've set the right IP in prometheus.yaml


You will also need to add Prometheus as a Datasource in your Grafana Application

- URL = http://prometheus:9090 #Default

Simply just type .. bme in the QL Query and autocomplete will show you the sensor datas

## Screenshots
| ![GrafanaSetup](screenshot/grafana.png)
|---|
|GrafanaSetup