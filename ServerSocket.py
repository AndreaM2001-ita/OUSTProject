import socket
import sys  #operating system package - save error in machine in case
                #commmunication shows issues

def connectSocket():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#socket

    server_address = ('localhost', 10000)
    sock.bind(server_address)#binding to put socket in server

    # Listen for incoming connections
    sock.listen(1)
    return sock

def closeSocket(socket):
    
    print('closing socket')
    socket.close()

def unitScores(data):
    score_string = data.strip('{}')  #remocve {}
    score_pairs = score_string.split(', ') #separate values

    parsed_scores = {} #dict

    for pair in score_pairs:
        unit_code, score = pair.split('=')
        parsed_scores[unit_code] = float(score)  

    return parsed_scores

#function to decode data and to create a dictionary parased data with all the information recived =so that they can be 
#used for calulation of eligibility
def decodeData(connection):
    # Receive data
    data = b''
    while b'\\n' not in data:
        data += connection.recv(3)
    received_data = data.decode()  #decode data

    
    # Parse received data
    parsed_data = {}
    lines = received_data.strip().split('\n')

    for line in lines:
        if line!='\\n':
            key, value = line.split(':')
            parsed_data[key.strip()] = value.strip()
    if parsed_data['unit_scores']!="{}":
        parsed_data['unit_scores']=unitScores(parsed_data['unit_scores'])
    
    return parsed_data

def sendMessage(message,connection):
    connection.sendall(message.encode())
"""
while True:
    # Wait for a connection
    print( 'waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print( 'received "%s"' % data)
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print( 'no more data from', client_address)
                break
            
"""
