import paho.mqtt.client as paho
broker="10.202.0.136"
	

client= paho.Client()
client.connect(broker)
client.publish("serv/bdd","on")#publish
client.loop() 
