import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    #print("message topic=",message.topic)
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)

########################################
broker_address="broker.hivemq.com"

print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker


client.loop_start() #start the loop
print("Subscribing to topic","battery/voltage")
client.subscribe("battery/voltage") 
while True:

    print("Publishing message to topic","battery/voltage")
    client.publish("battery/voltage","voltage data")
    time.sleep(1)
    client.subscribe("battery/voltage") 
    time.sleep(1) # wait
