import socket
import sys  #operating system package - save error in machine in case
                #commmunication shows issues

#running service on port 20000
def connectSocket():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#socket

    server_address = ('localhost', 20000)
    sock.bind(server_address)#binding to put socket in server

    # Listen for incoming connections
    sock.listen(1)
    return sock

def closeSocket(socket):
    
    print('closing socket')
    socket.close()

def unitScores(data):
    score_string = data.strip('{}')  #remove {}
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
    if parsed_data['unit_scores']!="{}":  #different way to deal with the scores value of the dictioanary
        parsed_data['unit_scores']=unitScores(parsed_data['unit_scores'])
    
    return parsed_data

def sendMessage(message,connection):
    connection.sendall(message.encode())

