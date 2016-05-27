#!/usr/bin/env python

import socket

class Client:
    port = 8089

    @classmethod
    def sendMessage(self, message):
        try:
            clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientsocket.connect(('localhost', self.port))
            clientsocket.send(message.encode('UTF-8'))
            clientsocket.close()
        except ConnectionRefusedError:
            print("Connection Refused. (is the daemon running?)")
            return False

        return True
