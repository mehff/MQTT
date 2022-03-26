# EN - US
# This file intertwines everything to communicate with MyDevices, using "defi.py" and "sim.py" as sources.
# !!!!! PAY CLOSE ATTENTION TO THE DEVICE PATH ON CAYENNE!!!!!
# -------------------------------------------------------------------------------------------------------------------------------------------
# PT - BR
# Esse arquivo interliga tudo para se comunicar com o MyDevices, utilizando os arquivos "defi.py" e "sim.py" como fonte.
# !!!!! PRESTE MUITA ATENÇÃO NO CAMINHO DO DISPOSITIVO NO CAYENNE !!!!!

from sim import aquecedor, aquecedor2, temperatura, temperatura2, umidade, desligaf, desligaf2
import paho.mqtt.client as mqtt
import time
from defi import user, password, client_id, client_id2, server, port, comms, comms2

def mensagem(client, user, msg):
    vetor = '0'
    vetor = msg.payload.decode().split(',')
    if vetor[1] == '1':
        aquecedor(estado='on'),desligaf(estado=0)
        client.publish(comms+'data/2','1')
    if vetor[1] == '0':
        aquecedor(estado='off'),desligaf(estado=1)
        client.publish(comms+'data/2','0')
    client.publish(comms+'response', f'ok,{vetor[0]}')
    print(vetor)
    return vetor[1]

    
def mensagem2(client2, user, msg):
    vetor2 = '0'
    vetor2 = msg.payload.decode().split(',')
    if vetor2[1] == '1':
        aquecedor2(estado2='on'),desligaf2(estado2=0)
        client2.publish(comms2+'data/2','1')
    if vetor2[1] == '0':
        aquecedor2(estado2='off'),desligaf2(estado2=1)
        client2.publish(comms2+'data/2','0')
    client2.publish(comms2+'response', f'ok,{vetor2[0]}')
    print(vetor2)
    return vetor2[1]
    


client = mqtt.Client(client_id)
client2 = mqtt.Client(client_id2)

client.username_pw_set(user, password)
client2.username_pw_set(user, password)
client.connect(server, port)
client2.connect(server, port)

client.on_message = mensagem
client2.on_message = mensagem2
client.subscribe(comms+'cmd/3')
client2.subscribe(comms2+'cmd/3')
client.loop_start()
client2.loop_start()

def comm():
    client.publish(comms+'data/0', temperatura())
    client.publish(comms+'data/1', umidade())
    client.publish(comms+'data/2', 1)
    time.sleep(2)

def comm2():
    client2.publish(comms2+'data/0', temperatura2())
    client2.publish(comms2+'data/1', umidade())
    client2.publish(comms2+'data/2', 1)
    time.sleep(2)

while True:
    comm()
    comm2()

client.disconnect()