import time
import paho.mqtt.client as paho
import ssl

client= paho.Client()
client.tls_set('/home/test/ssl/ca.crt')
client.connect("10.202.4.1",8883,60)
client.publish("serv/bdd","ok")#publish
client.disconnect()
client.loop_forever() 
