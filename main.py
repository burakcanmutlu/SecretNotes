import base64
import tkinter
import os
from tkinter import PhotoImage
from tkinter import messagebox
from cryptography.fernet import Fernet


window = tkinter.Tk()
window.title("Secret Notes")
window.minsize(width=700, height=600)



image= tkinter.PhotoImage(file="top-secret_10201555.png")
image_label= tkinter.Label(window, image=image)
image_label.pack()





def encrypt_message_create_desktop():
    message=title_message_entry.get()
    dosya_yolu = os.path.join(os.path.expanduser("~"), "Desktop",message+".txt")
    secret_message=secret_message_text.get(1.0, tkinter.END)
    key_input= key_message_entry.get()
    key_bytes=key_input.encode()
    key_bytes=key_bytes.ljust(32)[:32]
    key=base64.urlsafe_b64encode(key_bytes)
    with open(dosya_yolu, "w") as dosya:
        dosya.write(secret_message)
        dosya.write(str(key))

    fernet=Fernet(key)
    encrypted_message=fernet.encrypt(secret_message.encode())
    decrypt_message=fernet.decrypt(encrypted_message).decode()
    tkinter.messagebox.showinfo("Secret", "Secret Notes Created")
    print(decrypt_message)



def decrypt_message():
    pass
    def decrypt_message():
        global encrypted_message
        global key_input

        if not encrypted_message or not key_input:
            messagebox.showerror("Hata", "Şifreli mesaj ve anahtar gerekli!")
            return

        try:
            key_bytes = key_input.encode()
            key_bytes = key_bytes.ljust(32)[:32]
            key = base64.urlsafe_b64encode(key_bytes)

            fernet = Fernet(key)
            decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()

            messagebox.showinfo("Çözülen Mesaj", decrypted_message)
        except:
            messagebox.showerror("Hata", "Geçersiz anahtar veya şifreli mesaj!")





































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
decrypt_button = tkinter.Button(text="Decrypt",width=12,height=0,command=decrypt_message)
decrypt_button.pack()














window.mainloop()