import paho.mqtt.client as paho

try:
    client = paho.Client()
    client.connect('broker.hivemq.com', 1883)
    client.loop_start()
    client.subscribe('temperature/6117931', qos=1)
    client.subscribe('air/quality/6117931', qos=1)

except: print("\n\n\n\t\tCheck Your Internet Connection\n\n")


def on_message(client, userdata, msg):
    global temp
    global air
    global humidity
    global pre_humidity
    #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    if msg.topic == "temperature/6117931":
        temp = int(round(float(msg.payload)))
       
    elif msg.topic == "air/quality/6117931":
        air = float(round(float(msg.payload)))

    elif msg.topic == "pre/humidity/6117931":
        pre_humidity = float(round(float(msg.payload)))
    
    elif msg.topic == "humidity/6117931":
        humidity = float(round(float(msg.payload)))

while 1:
    client.on_message = on_message
    print(f'''
Temp : {temp}
Air : {air}
Humidity : {humidity}
Predicted Humidity : {pre_humidity}

''')