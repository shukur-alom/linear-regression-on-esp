import paho.mqtt.client as paho
import time
import pickle
import numpy as np
with open('AI models/temp.pkl', 'rb') as file:
    model = pickle.load(file)
with open('AI models/airq.pkl', 'rb') as file:
    model_1 = pickle.load(file)

try:
    client = paho.Client()
    client.connect('broker.hivemq.com', 1883)
    client.loop_start()
    client.subscribe('temperature/6117931', qos=1)
    client.subscribe('air/quality/6117931', qos=1)

except: print("\n\n\n\t\tCheck Your Internet Connection\n\n")

pre_temp_list = [40, 40, 40, 39, 39, 40, 40, 39]
pre_aiq_list = [120.0, 146.0, 176.0, 156.0, 85.0, 94.0, 74.0, 82.0]

pre_temp = 0
air_quality_index = 0
predict_air_quality_index = 0

def on_message(client, userdata, msg):
    global pre_temp
    global air_quality_index
    global predict_air_quality_index
    #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    if msg.topic == "temperature/6117931":
        temp = int(round(float(msg.payload)))
        pre_temp_list.append(temp)
        pre_temp = model.predict([pre_temp_list])[0]
        pre_temp_list.remove(pre_temp_list[0])

    elif msg.topic == "air/quality/6117931":
        air_0 = float(round(float(msg.payload)))

        pre_aiq_list.append(air_0)
        air = model_1.predict([pre_aiq_list])[0]
        pre_aiq_list.remove(pre_aiq_list[0])

        if air_0>=0 and air_0<=50: air_quality_index = 1
        elif air_0>=51 and air_0<=100: air_quality_index = 2
        elif air_0>=101 and air_0<=200: air_quality_index = 3
        elif air_0>=201 and air_0<=300: air_quality_index = 4
        elif air_0>=301 and air_0<=400: air_quality_index = 5
        elif air_0>=401 and air_0<=500: air_quality_index = 6
        elif air_0>=501 and air_0<=600: air_quality_index = 7
        elif air_0>=601 and air_0<=700: air_quality_index = 8
        elif air_0>=701 and air_0<=800: air_quality_index = 9
        elif air_0>=801 and air_0<=900: air_quality_index = 10
        elif air_0>=901 and air_0<=100000000: air_quality_index = 11


        client.publish(f"predict/air/quality/6117931", str(round(air, 2)), qos=0)

        if air>=0 and air<=50: predict_air_quality_index = 1
        elif air>=51 and air<=100: predict_air_quality_index = 2
        elif air>=101 and air<=200: predict_air_quality_index = 3
        elif air>=201 and air<=300: predict_air_quality_index = 4
        elif air>=301 and air<=400: predict_air_quality_index = 5
        elif air>=401 and air<=500: predict_air_quality_index = 6
        elif air>=501 and air<=600: predict_air_quality_index = 7
        elif air>=601 and air<=700: predict_air_quality_index = 8
        elif air>=701 and air<=800: predict_air_quality_index = 9
        elif air>=801 and air<=900: predict_air_quality_index = 10
        elif air>=901 and air<=1000000000: predict_air_quality_index = 11

