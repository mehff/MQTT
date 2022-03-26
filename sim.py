# EN - US
# This file defines everything related to simulated devices, as I don't own a greenhouse nor all those sensors!
# -------------------------------------------------------------------------------------------------------------------------------------------
# PT - BR
# Esse arquivo define tudo relacionado aos dispositivos simulados, já que eu não tenho uma estufa nem os sensores!

import random

temp = 0
temp2 = 0
tempp = 0
tempp2 = 0
forceoff = 0
forceoff2 = 0

def temperatura():
    global temp
    global tempp
    if temp == 0:
        temp = random.randrange(2,35)
        return temp
    else:
        if tempp >= temp:
            return aquecedor(estado='off')
        if tempp <= temp:
            return aquecedor(estado='on')
            
def temperatura2():
    global temp2
    global tempp2
    if temp2 == 0:
        temp2 = random.randrange(2,35)
        return temp2
    else:
        if tempp2 >= temp2:
            return aquecedor2(estado2='off')
        if tempp2 <= temp2:
            return aquecedor2(estado2='on')

def umidade():
    return random.randrange(10,70)

def aquecedor(estado: str):
    global temp
    global tempp
    global forceoff
    print('forceoff', forceoff)
    if temp <= 29 and forceoff == 0:
        estado == 'on'
        tempp = temp
        temp += 1
        print('Aquecedor ON', temp)
        print('temp:', temp)
        print('tempp:', temp)
        return temp
    if temp >= 30 or forceoff == 1:
        estado == 'off'
        tempp = temp
        temp -= 1
        print('Aquecedor OFF', temp)
        print('temp:', temp)
        print('tempp:', tempp)
        return tempp

def aquecedor2(estado2: str):
    global temp2
    global tempp2
    global forceoff2
    print('forceoff', forceoff2)
    if temp2 <= 29 and forceoff2 == 0:
        estado2 == 'on'
        tempp2 = temp2
        temp2 += 1
        print('Aquecedor 2 ON', temp2)
        print('temp2:', temp2)
        print('tempp2:', temp2)
        return temp2
    if temp2 >= 30 or forceoff2 == 1:
        estado2 == 'off'
        tempp2 = temp2
        temp2 -= 1
        print('Aquecedor 2 OFF', temp2)
        print('temp2:', temp2)
        print('tempp2:', tempp2)
        return tempp2

def desligaf(estado: int):
    global forceoff
    if estado == 1:
        forceoff = 0
        return forceoff
    if estado == 0:
        forceoff = 1
        return forceoff

def desligaf2(estado2: int):
    global forceoff2
    if estado2 == 1:
        forceoff2 = 0
        return forceoff2
    if estado2 == 0:
        forceoff2 = 1
        return forceoff2