import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    income_msg = str(message.payload.decode("utf-8"))
    print("received message: " ,income_msg)

mqttBroker ="broker.hivemq.com"

client = mqtt.Client("Smartphone")
client.connect(mqttBroker) 

client.loop_start()

while True:
    client.subscribe("Battery")
    client.on_message=on_message 
    
