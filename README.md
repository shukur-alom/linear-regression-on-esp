# ESP32 Linear Regression Model with MQTT and Sensor Integration

## Introduction
This repository contains code and resources for a system that implements a linear regression model on an ESP32 microcontroller. The model's coefficients (m and c) are extracted from the trained model, and the ESP32 transmits sensor data and predicted data using MQTT to a Python script for further processing.

![Device](https://github.com/shukur-alom/linear-regression-on-esp-esp32/blob/main/Media/IMG20231213010446.jpg)

[Watch Video Demo](https://github.com/shukur-alom/linear-regression-on-esp-esp32/blob/main/Media/video.mp4)

## Requirements
* ESP32 microcontroller
* MQ-2 sensor
* DHT11 temperature and humidity sensor
* Python 3.x
* Libraries specified in requirements.txt

## Setup
1. Training the Model

    * Use the provided training code (found in the repository) to train the linear regression model.
    * Retrieve the coefficients (m and c) from the trained model.
2. ESP32 Setup

    * Upload the ESP32 code available in this repository to your ESP32 device.
    * Set the obtained coefficients (m and c) in the appropriate variables within the ESP32 code.
3. Sensor Integration

    * Connect the MQ-2 and DHT11 sensors to the ESP32 based.
        * MQ-2(AO) to ESP(23)
        * MQ-2(GND) to ESP(GND)
        * MQ-2(VCC) to ESP(Vin)
        * DHT11(out) to ESP(32)
        * DHT11(-) to ESP(GND)
        * DHT11(+) to ESP(3v3)

4. Python Code

    * Utilize the provided Python code to receive MQTT messages from the ESP32.
    * Modify the code as necessary to process the received sensor data.

## Usage
1. Model Training

    * Run the training code to train the linear regression model.
    * Note down the coefficients (m and c) obtained from the model.

2. ESP32
    * Change ssid and password
    * Upload the modified code with the extracted coefficients to the ESP32 device.
    * Ensure proper connectivity with the sensors.
3. Python Script

    * Run the Python script to listen for MQTT messages sent by the ESP32.
    * Process and utilize the received sensor data as required.



[Medium](https://medium.com/@shukuralom1234/run-linear-regression-model-on-esp32-08b0b51ea207)
