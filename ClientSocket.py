import socket
import time
import sys


#function to connect socket from client to server 1
def connectSocket():

    for attempt in range(5): #retry connection for 5 times
        try:
            # Create a TCP/IP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Connect the socket to the port where the server is listening
            server_address = ('localhost', 20000)
            print('-> Creating a connection to %s port %s' % server_address)
            print()
            sock.connect(server_address)
            return sock
        except ConnectionRefusedError:  #in case connection is rerfused because server is down 
            print("Connection refused. Retrying...")
            time.sleep(1)  # Wait before retrying
            continue

#function to close socket from client to server 1 
def closeSocket(socket):
    
    print('->closing socket')
    socket.close()

#fucntion to create a message within one string to be sent to server 
def messageHandler(user_id, unit_scores="", name="", last_name="",email=""):
    # Create a dictionary with your message
    message_dict = {
        'user_id': user_id,
        'name': name,
        'last_name': last_name,
        'email': email,
        'unit_scores': unit_scores,

    }

    # Convert the dictionary to a string representation
    message_string = ""
    for key, value in message_dict.items():
        if isinstance(value, dict):  # Check if value is a dictionary
            value_str = "{"  #first character for the dictioanry string
            for k, v in value.items():  #get the values off dictioanry
                value_str += f"{k}={v}, "  #create pairs
            value_str = value_str.rstrip(", ") + "}"    #remove last comma and closedict to sent
            message_string += f"{key}:{value_str}\n"
        else:
            message_string += f"{key}:{value}\n"
    
    message_string+="\\n"
    return message_string

#function to send the message to server
def sendMessage(message,socket):
    socket.sendall(message.encode())

def decodeData(socket):
    # Receive data
    data = b''
    while b'\\n' not in data:
        data += socket.recv(3)
    received_data = data.decode() 
    
    return received_data
