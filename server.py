# -*- coding: utf-8 -*-

import socket
import thread

import settings


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((settings.HOST, settings.PORT))

sock.listen(10)


def handle_conn(conn):
    reply = "HTTP/1.1 200 OK\r\n"
    conn.send(reply)
    conn.settimeout(settings.CONN_TIMEOUT)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
    conn.close()

while True:
    conn, addr = sock.accept()
    print "get connection from:", addr
    thread.start_new_thread(handle_conn, (conn,))
