#chat Application 
# client side


import threading# for handling threads
import socket# for creating socket
import argparse# handling args
import os # for os realated work 
import sys 
import tkinter as tk#for gui
username=""

# creating send class and pass threads
class Send(threading.Thread):
    #getting input from user through commandline
    #connecting  to sock's object
    #name (str) : The user name provided by the user 
    def __init__(self,sock,name):
        super().__init__()
        self.sock = sock
        self.name=name

    def run(self):
        #read user input from the command line and send it to the server
        #typing "Quit" will close the conection and exit the app
        while True:
            print('{}: '.format(self.name),end='')
            sys.stdout.flush()
            message = sys.stdin.readline()[:-1]

            #if user type "quit" user leave the chat
            if message=="QUIT":
                self.sock.sendall('Server: {} has left the chat.'.format(self.name).encode('ascii'))
                break
            #else send msgs
            else:
                self.sock.sendall('{} : {} .'.format(self.name,message).encode('ascii'))

        print('/n Qutting...')
        self.sock.close()
        os.exit(0)

class Receive(threading.Thread):

    #read user input from commandline
    def __init__(self,sock,name):
        super().__init__()
        self.sock = sock
        self.name=name
        self.messages=None

    def run (self):
        #receive data from server and print it over here
        while True:
            message = self.sock.recv(1024).decode('ascii')
            if message:
                if self.messages:

                     self.messages.insert(tk.END,message)
                     print('Hii')
                     print('/r{}\n{}:'.format(message,self.name),end='')

                else:
                     print('/r{}\n{}:'.format(message,self.name),end='')

            else:
                print('\n We Have Lost The Connection To The Server !!')
                print('/n EXIT...')
                self.sock.close()
                os.exit(0)

class Client:

    #GUI
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.name=None
        self.messages=None

    def start(self):
        print("connecting to {}:{}".format(self.host,self.port))
        self.sock.connect((self.host,self.port))
        print("successfully connected to {} : {}".format(self.host,self.port))
        print()
        self.name=input("Your Name : ")
        global username
        username=self.name
        print()
        print("Welcome , {} ! You can send and Receive Message !".format(self.name))

        # send and receive threads creating

        send=Send(self.sock,self.name)
        receive=Receive(self.sock,self.name)
        send.start()
        receive.start()

        self.sock.sendall('Server : {} has joined the chat '.format(self.name).encode('ascii'))
        print("\r Ready ! You can leave the chat anytime by just typing 'QUIT' \n")
        print('{} : '.format(self.name),end='')
        return receive
    
   

    def send(self,textInput):
        #sends textinput from GUI
        message=textInput.get()
        textInput.delete(0,tk.END)
        self.messages.insert(tk.END,'{}:{}'.format(self.name,message))
        # if the message is quit then left the chat else it will sending the msg to the server
        #QUIT for exit the chat
        if message == "QUIT":
            self.sock.sendall('Server : {} is exit from the chat'.format(self.name).encode('ascii'))
            print('/n EXIT...')
            self.sock.close()
            os._exit(0)

        #message sending to server for broadcasting 
        else:
           self.sock.sendall('{}: {}'.format(self.name, message).encode('ascii'))
        
def main(host,port):


    
    # create and excute our GUI App over here

    client= Client(host,port)
    receive=client.start()

    

    msg_window = tk.Tk()
    msg_window.title("CHAT APPLICATION")
    msg_window.configure(bg="#708090")

# Container Frame for packing
    container = tk.Frame(master=msg_window)
    container.pack(fill=tk.BOTH, expand=True)

# Header Frame
    header_frame = tk.Frame(master=container, bg="#708090")
    header_label = tk.Label(master=header_frame, text="CHAT APPLICATION", bg="#708090", font=("Helvetica", 16, "bold"))
    header_label.pack(pady=10)
    header_username_label = tk.Label(master=header_frame, text=f"welcome ! {username} to our chat application !!", bg="#708090", font=("Helvetica", 13, "bold"))
    header_username_label.pack(pady=10)
    header_frame.pack(side=tk.TOP, fill=tk.X)

# Main Content Frame
    main_frame = tk.Frame(master=container,bg="#708090")
    main_frame.pack(fill=tk.BOTH, expand=True)

    receivemsg = tk.Frame(master=main_frame)
    scroll_chat = tk.Scrollbar(master=receivemsg)
    messages_list = tk.Listbox(master=receivemsg, yscrollcommand=scroll_chat.set, bg="#100F0F", fg="white")

    scroll_chat.pack(side=tk.RIGHT, fill=tk.Y, expand=False)
    messages_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    client.messages = messages_list
    receive.messages = messages_list

    receivemsg.grid(row=0, column=0, columnspan=2, sticky="nsew")
    receivemsg_entry = tk.Frame(master=main_frame)
    textInput = tk.Entry(master=receivemsg_entry)

    textInput.pack(fill=tk.BOTH, expand=True)
    textInput.bind("<Return>", lambda x: client.send(textInput))
    textInput.insert(0, "You Can Type your Message Over Here")

    send_button = tk.Button(master=main_frame, text="Send Message", command=lambda: client.send(textInput))

    receivemsg_entry.grid(row=1, column=0, padx=10, sticky="ew")
    send_button.grid(row=1, column=1, padx=10, sticky="ew")

    main_frame.rowconfigure(0, minsize=500, weight=1)
    main_frame.rowconfigure(1, minsize=50, weight=0)
    main_frame.columnconfigure(0, minsize=500, weight=1)
    main_frame.columnconfigure(1, minsize=200, weight=0)

    msg_window.mainloop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Chatapplication Server")
    parser.add_argument('host',help='Interface is the server listen at these ')
    parser.add_argument('-p',metavar='PORT',type=int,default=1060,help='TCP port (default 1060)')

    args=parser.parse_args()

    main(args.host,args.p)






      