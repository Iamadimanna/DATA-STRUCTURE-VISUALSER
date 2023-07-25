"""Step 1: Replace odd letters with even letters' position point number two for each letter, generate a symbol from hashtag dollar present divide minus plus multiply.

Step 2: Replace odd positions with even positions.

Step 3: Divide and swap in two halves.

Step 4: At odd positions, add letters from the alphabet A to Z linearly"""

import tkinter as tk


def step_1(sentence):
    encrypted = ""
    for char in sentence:
        if ord(char) % 2 == 1:
            encrypted += chr(ord(char) * 2)
        else:
            symbols = ['#', '$', '%', '/', '-', '+', '*']
            encrypted += symbols[ord(char) % len(symbols)]
    return encrypted


def step_2(sentence):
    encrypted = ""
    for i, char in enumerate(sentence):
        if i % 2 == 0:
            encrypted += char
        else:
            encrypted += sentence[i - 1]
    return encrypted


def step_3(sentence):
    half_len = len(sentence) // 2
    first_half = sentence[:half_len]
    second_half = sentence[half_len:]
    return second_half + first_half


def step_4(sentence):
    encrypted = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, char in enumerate(sentence):
        if i % 2 == 1:
            idx = i // 2 % len(alphabet)
            encrypted += alphabet[idx]
        encrypted += char
    return encrypted


def reverse_step_1(encrypted):
    decrypted = ""
    for char in encrypted:
        if ord(char) % 2 == 1:
            decrypted += chr(ord(char) // 2)
        else:
            symbols = ['#', '$', '%', '/', '-', '+', '*']
            decrypted += chr(symbols.index(char) % 26 + 65)
    return decrypted


def reverse_step_2(encrypted):
    decrypted = ""
    for i in range(len(encrypted)):
        if i % 2 == 0:
            decrypted += encrypted[i]
    return decrypted


def reverse_step_3(encrypted):
    half_len = len(encrypted) // 2
    second_half = encrypted[:half_len]
    first_half = encrypted[half_len:]
    return first_half + second_half


def reverse_step_4(encrypted):
    decrypted = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(encrypted)):
        if i % 2 == 1:
            idx = (i // 2 + alphabet.index(encrypted[i])) % 26
            decrypted += alphabet[idx]
        else:
            decrypted += encrypted[i]
    return decrypted


def encrypt_sentence():
    sentence = input_text.get("1.0", "end-1c")  # Get the entire text from the text area

    # Apply step 1
    encrypted = step_1(sentence)

    # Apply step 2
    encrypted = step_2(encrypted)

    # Apply step 3
    encrypted = step_3(encrypted)

    # Apply step 4
    encrypted = step_4(encrypted)

    output_label.config(text="Encrypted: " + encrypted)


def decrypt_sentence():
    encrypted = input_text.get("1.0", "end-1c")  # Get the entire text from the text area

    # Reverse step 4
    decrypted = reverse_step_4(encrypted)

    # Reverse step 3
    decrypted = reverse_step_3(decrypted)

    # Reverse step 2
    decrypted = reverse_step_2(decrypted)

    # Reverse step 1
    decrypted = reverse_step_1(decrypted)

    output_label.config(text="Decrypted: " + decrypted)


# Create the main application window
root = tk.Tk()
root.title("Encryption and Decryption")
root.configure(bg="blue")
root.geometry("500x280")



# Create and arrange the GUI elements
input_label = tk.Label(root, text="Enter sentence:")
input_label.pack()

input_text = tk.Text(root, height=5, wrap="word")
input_text.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_sentence)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_sentence)
decrypt_button.pack()

output_label = tk.Label(root, text="")
output_label.pack()

# Run the main loop
root.mainloop()
