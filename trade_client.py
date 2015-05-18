import json
import socket
import hashlib


def send_msg(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(1024)
        print "Received: {}".format(response)
    finally:
        sock.close()


def send_offer(ip, port, offer):
    message = json.dumps(offer)
    send_msg(ip, port, message)
