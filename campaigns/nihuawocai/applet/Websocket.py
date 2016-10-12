#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket, threading, struct, sys, base64, hashlib, multiprocessing, os

connectionlist = {}
connectstatus = True
pidlist = []

def deleteconnection(item):
    global connectionlist
    del connectionlist['connection' + str(item)]




def handshake(client):
    headers = {}
    shake = client.recv(1024)

    if not len(shake):
        return False

    header, data = shake.split('\r\n\r', 1)
    for line in header.split('\r\n')[1:]:
        key, value = line.split(": ", 1)
        headers[key] = value

    if(headers.has_key(("Sec-WebSocket-Key"))) == False:
        print "this socket is not websocket"
        client.close()
        return False

    szOrigin = headers['Sec-WebSocket-Key']
    szKey = base64.b64encode(hashlib.sha1(headers['Sec-WebSocket-Key'] + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11').digest())
    szHost = headers["Host"]
    our_handshake = "HTTP/1.1 101 Switching Protocols\r\n"\
"Upgrade:websocket\r\n" \
"Connection: Upgrade\r\n" \
"Sec-WebSocket-Accept:" + szKey + "\r\n" \
"WebSocket-Origin:" + szOrigin + "\r\n" \
"WebSocket-Location: ws://" + szHost + "/WebManagerSocket\r\n" \
"WebSocket-Protocol:WebManagerSocket\r\n\r\n"

    client.send(our_handshake)
    return True

def RecvData(nNum, client):
    try:
        pData = client.recv(nNum)
        if not len(pData):
            return False
    except:
            return False
    else:
        code_length = ord(pData[1]) & 127

        if code_length == 126:
            masks = pData[4:8]
            data = pData[8:]
        elif code_length == 127:
            masks = pData[10:14]
            data = pData[14:]
        else:
            masks = pData[2:6]
            data = pData[6:]

        raw_str = ""
        i = 0
        for d in data:
            raw_str += chr(ord(d) ^ ord(masks[i % 4]))
            i += 1
        return raw_str




def SendData(pData, client):

    if pData == False:
        return False
    else:
        pData = str(pData)

    token = '\x81'

    length = len(pData)
    if length < 126:
        token += struct.pack("B", length)
    elif length <= 0xFFFF:
        token += struct.pack("!BH", 126, length)
    else:
        token += struct.pack("!BQ", 127, length)
    pData = '%s%s' % (token, pData)
    client.send(pData)
    return True


def DoRemoteCommand(connection, i):
    while 1:
        szBuf = RecvData(8196, connection)
        print szBuf
        if (szBuf == "exit"):
            sys.exit()

        if (szBuf == "quit"):
            deleteconnection(i)


        if (szBuf == False):
            connection.close()
            continue


        else:
            global connectionlist
            for connection in connectionlist.values():
                if connection.socket:
                    try:

                        SendData(szBuf, connection)
                    except Exception as e:
                        deleteconnection(i)
                        connection.close()
                        print e




def InitWebSocketServer(_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind(("0.0.0.0", _port))
        sock.listen(100)
        print "server start!"
    except Exception as e:
        print "server quit" + str(e)
    global connectionlist
    global connectstatus
    i = 0
    time = 0
    while True:
        if time > 1000000000000000000000000:
            break
        conn, addr = sock.accept()
        username = addr[0]
        if handshake(conn) != False:
            connectionlist['connection' + str(i)] = conn
            t = threading.Thread(target=DoRemoteCommand, args=(conn, i))
            # t = multiprocessing.Process(target=DoRemoteCommand, args=(conn, ))
            t.start()
            i += 1
            time += 1

Port = int(sys.argv[1])
InitWebSocketServer(Port)
