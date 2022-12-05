from tkinter import *
import datetime
import paho.mqtt.client as mqtt


mqttBroker ="broker.hivemq.com"
#setup mqtt broker client
client = mqtt.Client("Smartphone")
#connect the client to the broker
client.connect(mqttBroker)
#start the subscription
client.loop_start()

#decode the msg acquired from subscription and display it
def on_message(client, userdata, message):
    income_msg = str(message.payload.decode("utf-8"))
    volt = income_msg
    data = datetime.datetime.now().strftime("Time: %H:%M:%S")+" /n"+ volt
    lab.config(text=data)
    root.after(200, getVolt)

root = Tk()
lab = Label(root)
lab.pack()


client.subscribe("Battery", 0)
client.on_message=on_message

root.mainloop()