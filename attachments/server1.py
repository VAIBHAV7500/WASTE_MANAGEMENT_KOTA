import socket
#import MySQLdb

def Main():
    HOST = '' #specifies that the socket is reachable by any address the machine happens to have
    PORT = 5004
    #db = MySQLdb.connect("localhost","root","Hellobro" )
    #cursor = db.cursor()
    #cursor.execute("use dummy")


    # create an INET, TCP socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # bind the socket to a public host, and a well-known port
    serversocket.bind((HOST, PORT))
    
    # become a server socket
    serversocket.listen(2)
    print("Server Listening...")
    
    while True:
        # accept connections from outside
	
        (connsocket, address) = serversocket.accept()    

        print("Connection from: ", address)

        # Read data
        while True:
            data = connsocket.recv(1024)
            if not data: break;       
            print("from connected user: ", (data.decode()))
            # convert from byte to string
            s=str(data.decode())
            #cursor.execute("insert into sensor values('%s')"  ,(s))
            fo = open("f.txt", "w")
            fo.write(s)
        connsocket.close()
        
    serversocket.close()
    #db.close()
    
if __name__ == '__main__':
    Main()


