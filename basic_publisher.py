import paho.mqtt.client as mqtt
import time

# Enligt dokumentation https://pypi.org/project/paho-mqtt/#callbacks
def client_on_connect(client, data, flags, return_code):
    if return_code == 1:
        print('Could not connect \n')
    else:
        print('Connect ed successfully! \n')
    return 

client1 = mqtt.Client()
client1.on_connect = client_on_connect #knyt en callback
client1.connect(host='broker.hivemq.com', port=1883)

client1.loop_start()


while True:
    temp = input('type something: ')
    msg = client1.publish(topic='YRGO/ei23', payload=str(temp), qos=1) #qos 1 - kräv ack
    msg.wait_for_publish()
