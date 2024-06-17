# chat application 
#serverside


import threading # for handling threads
import socket # for creating socket
import argparse # handling args
import os # for os realated work

# creating class called server passing threads
class Server(threading.Thread):
    # creating function of initalization and passing self , host , and port in that function which initalize the obj
    def __init__(self_chat,host_chat,port_chat):
        super().__init__()
        self_chat.connections_chat=[]
        self_chat.host_chat=host_chat
        self_chat.port_chat=port_chat
    # creating function called run 
    def run(self_chat):
        # creating socket named sock and setsocket 
        sock_chat=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock_chat.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        # bind the socket
        sock_chat.bind((self_chat.host_chat,self_chat.port_chat))
        sock_chat.listen(1)
        # now server is listing at 
        print("Listen the server at ...",sock_chat.getsockname())
        
        # while loop 
        while True:
            #these will accept the new connections from the client 
            sc,sockname=sock_chat.accept()
            print(f"New connections acceptance from {sc.getpeername()}to {sc.getsockname()}")

            #these is for  creating new thread.. 
            sever_socket=ServerSocket(sc,sockname,self_chat)

            #these is for staring new thread that we have created
            sever_socket.start()

            #these is to Adding thread to active connection.. 
            self_chat.connections_chat.append(sever_socket)
            print("You Are Ready to Recieve Messages From",sc.getpeername())

     # function for broadcast
    def broadcast(self_chat,message,source):
        for connection in self_chat.connections_chat:
            #these will send to all connected client accept the source client
            if connection.sockname != source:
                connection.send(message)

    # function for remove the connection
    def remove_connection(self_chat,connection):
        self_chat.connections_chat.remove(connection)

# now creating another class called serversocket
class ServerSocket(threading.Thread):

#creating function of initalization and passing self,sc,sockname and server in that function which initalize the obj
   
    def __init__(self_chat,sc,sockname,server):
        super().__init__()
        self_chat.sc=sc
        self_chat.sockname=sockname
        self_chat.server=server

# creating function called run 
    def run(self_chat):
        # while loop 
        while True:
            message=self_chat.sc.recv(1024).decode('ascii')
            if message:
                print(f"{self_chat.sockname} type {message}")
                self_chat.server.broadcast(message,self_chat.sockname)
            else:
                print(f"{self_chat.sockname}has terminate their connection.")
                self_chat.sc.close()
                Server.remove_connection(self_chat)
                return
    # creating function called send for sending the message
    def send(self_chat,message):
        self_chat.sc.sendall(message.encode('ascii'))

    # creating function called exit to terminate the connection 
    def exit(server):
        while True:
            ipt_chat=input("")
            if ipt_chat == "q":
                print("Terminating all of the connections...")
                for connection_chat in server.connections_chat:
                    connection_chat.sc.close()
                print("Closing The Server \n Shutting down the Server....")
                os._exit(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Chatapplication Server")
    parser.add_argument('host',help='Interface is the server listen at these ')
    parser.add_argument('-p',metavar='PORT',type=int,default=1060,help='TCP port (default 1060)')

    args=parser.parse_args()

     
    server= Server(args.host,args.p)
    server.start()
    exit=threading.Thread(target=exit,args=(server,))
    exit.start()










        