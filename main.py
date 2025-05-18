import base64
import tkinter
import os
from tkinter import PhotoImage, Button, END
from tkinter import messagebox
from cryptography.fernet import Fernet


window = tkinter.Tk()
window.title("Secret Notes")
window.minsize(width=700, height=600)


photo= tkinter.PhotoImage(file="top-secret_10201555.png")
photo_button=Button(image=photo)
photo_button.pack()

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)









def encrypt_message_create_desktop():
    title_message=title_message_entry.get()
    key_message=key_message_entry.get()
    secret_message=secret_message_text.get(1.0, tkinter.END)

    if len(title_message) == 0 or len(key_message) == 0 or len(secret_message)==0:
        messagebox.showinfo(title="Error!",message="Please enter all info.")
    else:
        message_encrypted=encode(key_message,secret_message)
        try:
            with open("mysecret.txt", "a") as data_file:
                data_file.write(f'\n{title_message}\n{message_encrypted}')
        except:
            with open("mysecret.txt", "w") as data_file:
                data_file.write(f'\n{title_message}\n{message_encrypted}')
        finally:
            title_message_entry.delete(0, END)
            key_message_entry.delete(0, END)
            secret_message_text.delete("1,0",END)


def decrypt_notes():
    message_encrypted = secret_message_text.get("1.0", END)
    master_secret = key_message_entry.get()

    if len(message_encrypted) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Error!", message="Please enter all information.")
    else:
        try:
            decrypted_message = decode(master_secret,message_encrypted)
            secret_message_text.delete("1.0", END)
            secret_message_text.insert("1.0", decrypted_message)
        except:
            messagebox.showinfo(title="Error!", message="Please make sure of encrypted info.")







title_message_label = tkinter.Label(window, text="Enter Your Title")
title_message_label.pack()
title_message_entry = tkinter.Entry(window)
title_message_entry.pack()
secret_message_label_1= tkinter.Label(window, text="Enter Your Secret Message")
secret_message_label_1.pack()
secret_message_text= tkinter.Text(window, height=20, width=50)
secret_message_text.pack()
key_message_label = tkinter.Label(window, text="Enter Master Key")
key_message_label.pack()
key_message_entry = tkinter.Entry(window)
key_message_entry.pack()
save_encrypted_message_button = tkinter.Button(text="Save & Encrypt",command=encrypt_message_create_desktop)
save_encrypted_message_button.pack()
decrypt_button = tkinter.Button(text="Decrypt",width=12,height=0,command=decrypt_notes)
decrypt_button.pack()









window.mainloop()