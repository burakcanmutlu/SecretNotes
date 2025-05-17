import tkinter
from tkinter import PhotoImage
window = tkinter.Tk()
window.title("Secret Notes")
window.minsize(width=700, height=600)



image= tkinter.PhotoImage(file="top-secret_10201555.png")
image_label= tkinter.Label(window, image=image)
image_label.pack()




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
save_encrypted_message_button = tkinter.Button(window, text="Save & Encrypt",width=12,height=0)
save_encrypted_message_button.pack()
decrypt_button = tkinter.Button(window, text="Decrypt",width=12,height=0)
decrypt_button.pack()













window.mainloop()