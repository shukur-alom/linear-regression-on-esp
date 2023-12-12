import paho.mqtt.client as paho
import time

try:
    client = paho.Client()
    client.connect('broker.hivemq.com', 1883)
    client.loop_start()
    client.subscribe('temperature/33445566', qos=1)
    client.subscribe('air/quality/33445566', qos=1)
    client.subscribe('pre/humidity/33445566', qos=1)
    client.subscribe('humidity/33445566', qos=1)

except: print("\n\n\n\t\tCheck Your Internet Connection\n\n")

temp,air,humidity,pre_humidity = 0,0,0,0

def on_message(client, userdata, msg):
    global temp
    global air
    global humidity
    global pre_humidity
    #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    if msg.topic == "temperature/33445566":
        temp = float(round(float(msg.payload)))
       
    elif msg.topic == "air/quality/33445566":
        air = float(round(float(msg.payload)))

    elif msg.topic == "pre/humidity/33445566":
        pre_humidity = float(round(float(msg.payload)))
    
    elif msg.topic == "humidity/33445566":
        humidity = float(round(float(msg.payload)))

while 1:
    client.on_message = on_message
    print(f'''
Temp : {temp}
Air : {air}
Humidity : {humidity}
Predicted Humidity : {pre_humidity}

''')
    time.sleep(2)