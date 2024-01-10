import string
import random
import customtkinter as ctk
import pyperclip

encrypted_text = ""

#copying to clipboard

def encrypted_copy():
    if label.cget('text') == "Click encrypt.":
        pyperclip.copy("")
    else:
        pyperclip.copy(label.cget('text'))

def decrypted_copy():
    if label2.cget('text') == "Click decrypt.":
        pyperclip.copy("")
    else:
        pyperclip.copy(label2.cget('text'))

#encryption and decryption

def encrypted():
    global encrypted_text
    encrypted_text = ""
    for letter in entry_field.get():
        index = decrypted_letters.index(letter)
        encrypted_text += encrypted_letters[index]
    label.configure(text = encrypted_text)
    encrypted_text = ""

def decrypted():
    global decrypted_text
    decrypted_text = ""
    for letter in decrypter_entry_field.get():
        index = encrypted_letters.index(letter)
        decrypted_text += decrypted_letters[index]
    label2.configure(text = decrypted_text)
    decrypted_text = ""
    
#encryption widgets

decrypted_letters = list(string.ascii_letters + string.digits + string.punctuation + " ")
encrypted_letters = decrypted_letters.copy()
random.seed(69420)
random.shuffle(encrypted_letters)

window = ctk.CTk()
window.title("Text encrypted and decrypted")
window.geometry("720x480")

main_label = ctk.CTkLabel(window,text="Password Encrypter & Decrypter", font=("", 36),text_color="white")
main_label.pack()

decrypted_text = ctk.StringVar(value="Replace this with normal text and click encrypt.")
entry_field = ctk.CTkEntry(window,font=("", 19), textvariable=decrypted_text, width=400)
entry_field.pack(pady="20")

button = ctk.CTkButton(window,text="Encrypt", command=encrypted)
button.pack()

label = ctk.CTkLabel(window,text="Click encrypt.", font=("", 12),text_color="white")
label.pack()

copy_button = ctk.CTkButton(window, text="Copy encrypted text", width=10, command=encrypted_copy)
copy_button.pack()


#decryption widgets

encrypted_text = ctk.StringVar(value="Replace this with encrypted text and clip decrypt")
decrypter_entry_field = ctk.CTkEntry(window,font=("", 19), textvariable=encrypted_text, width=450)
decrypter_entry_field.pack(pady="20")

button2 = ctk.CTkButton(window,text="Decrypt", command=decrypted)
button2.pack()

label2 = ctk.CTkLabel(window,text="Click Decrypt.", font=("", 12),text_color="white")
label2.pack()

copy_button2 = ctk.CTkButton(window, text="Copy decrypted text", width=10, command=decrypted_copy)
copy_button2.pack()

window.mainloop()
