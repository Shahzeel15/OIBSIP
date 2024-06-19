from tkinter import *
from tkinter.ttk import Combobox # for selection box
import string,random # for password generation
from tkinter import messagebox # for messagebox
import pyperclip # for copytext opration

root=Tk()
root.geometry("500x500")
root.title("PASSWORD GENERATOR")
root.config(bg="darkslategray")
# created two function on_enter and on_leave for password genration button
def on_enter(e):
    generate_button['bg']="darkslategray"
    generate_button['fg']="aquamarine"
def on_leave(e):
    generate_button["bg"]="aquamarine"
    generate_button["fg"]="darkslategray"
# when user press the button then these function will call and do the follwing operations to genrate password
def password_generate():
    try:
         # getting length from user
         plength=solidboss.get()

         string_lower=string.ascii_lowercase # for all lowercase char
         string_uper=string.ascii_uppercase #for all uppercase char
         string_digits=string.digits # for all digits
         string_punctuation = string.punctuation # for all punctuation

    
# create an empty list and extend all the string in it means these list has all the possible character to genrate  a password
         characters=[]
         characters.extend(list(string_uper))
         characters.extend(list(string_lower))
         characters.extend(list(string_digits))
         characters.extend(list(string_punctuation))
         print(characters)

# now using random.suffle you can randomely suffle the character inside the list  
         random.shuffle(characters)
         print(characters)

# now randomely pick the characters from the suffled list 
         print("".join(characters[0:plength]))
         # and setting it's value as password for display  
         password.set("".join(characters[0:plength]))  
    except:
        # messagebox incase of any error if it occurs then it will be handeled by these
        messagebox.askretrycancel("A problem has been occured","please try again")

# if user clicks copy button then these function will call
def copy_password():
  """Copies the text from the password entry field to the clipboard."""
  password_text = password.get()  # Get the text from the StringVar
  pyperclip.copy(password_text)  # Copy the text to the clipboard

Title = Label(root,text="PASSWORD GENERATOR" , bg="darkslategray" , fg="aquamarine" , font=("futura",20,"bold"))
Title.pack(anchor="center",pady="50px")

#label for selecting length of the password
length=Label(root,text="Select The Length Of Your Password : ",bg="darkslategray",fg="aquamarine",font=("ubuntu",16,"bold"))
length.place(x="30px",y="120px")

# created one dictionary for selection options for the password length
all_no={"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","10":"10","11":"11","12":"12","13":"14","14":"14","15":"15","16":"16","17":"17","18":"18","19":"19","20":"20","21":"21","22":"22","23":"23","24":"24","25":"25","26":"26","27":"27","28":"28","29":"29","30":"30"}
# taking it from the user
solidboss = IntVar()
selector=Combobox(root,textvariable=solidboss,state="readonly",font=("ubuntu",16,"bold"))
selector['values']=[l for l in all_no.keys()]
selector.current(7)
selector.place(x="350px",y="120px",width=300)


# label for result as generated password
result_label=Label(root,text="Generated Password : ",bg="darkslategray",fg="aquamarine",font=("ubuntu",16,"bold"))
result_label.place(x="30px",y="180px")
password=StringVar()
password_final=Entry(root,textvariable=password,bg="aquamarine",fg="darkslategray",state="readonly",font=("ubuntu",16,"bold"),width=50)
password_final.place(x="280px",y="180px")

# copy button
copy_button = Button(root, text="Copy Text", command=copy_password,bg="aquamarine",fg="darkslategray",font=("ubuntu",10,"bold"),cursor="hand2")
copy_button.place(x="810px", y="180px")

# password generation button
generate_button = Button(root,text="Generate Password",bg="aquamarine",fg="darkslategray",font=("ubuntu",20,"bold"),cursor="hand2",command=password_generate)
generate_button.bind("<Enter>",on_enter)
generate_button.bind("<Leave>",on_leave)
generate_button.pack(anchor="center",pady="100px")
root.mainloop()
