#!/usr/bin/env python
import time
import os
import paho.mqtt.client as mqtt
import json

data = {}
with open('/data/options.json') as json_file:
    data = json.load(json_file)

def topic_prefix():
  return 'homeassistant/'+data['component']+'/'+data['object_id']

def on_connect(client, userdata, flags, rc):
  os.system("echo 'Connected with result code "+str(rc)+"'")
  client.publish(topic_prefix()+"/config",'{"name": "'+data['object_id']+'", "command_topic":"'+topic_prefix()+'/set"}')
  client.subscribe(topic_prefix()+"/set")
  
def on_message(client, userdata, msg):
  operation = msg.payload.decode().lower()
  os.system("echo 'message received: "+operation+"'")
  os.system("sendv2 " + data['operations'][operation])


client = mqtt.Client()
client.username_pw_set(username=data['mqtt']['user'],password=data['mqtt']['password'])
client.connect(data['mqtt']['host'],1883,60)

client.on_connect = on_connect
client.on_message = on_message
client.loop_start()

while True:
  client.publish(topic_prefix()+"/config",'{"name": "'+data['object_id']+'", "command_topic":"'+topic_prefix()+'/set"}')
  time.sleep(60)