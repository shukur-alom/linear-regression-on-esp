# ESP32 Linear Regression Model with MQTT and Sensor Integration

## Introduction
This repository contains code and resources for a system that implements a linear regression model on an ESP32 microcontroller. The model's coefficients (m and c) are extracted from the trained model, and the ESP32 transmits sensor data using MQTT to a Python script for further processing.

## Requirements
* ESP32 microcontroller
* MQ-2 sensor
* DHT11 temperature and humidity sensor
* Python 3.x
* Libraries specified in requirements.txt