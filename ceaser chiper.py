import tkinter as tk

def caesar_cipher(text, shift):
    result = ""

    # loop through each character in the text
    for char in text:
        # check if the character is an uppercase letter
        if char.isupper():
            # find the position of the character in the alphabet
            char_position = ord(char) - ord('A')
            # apply the shift to the position
            new_position = (char_position + shift) % 26
            # convert the new position back to a character and add it to the result
            result += chr(new_position + ord('A'))
        # check if the character is a lowercase letter
        elif char.islower():
            # find the position of the character in the alphabet
            char_position = ord(char) - ord('a')
            # apply the shift to the position
            new_position = (char_position + shift) % 26
            # convert the new position back to a character and add it to the result
            result += chr(new_position + ord('a'))
        else:
            # the character is not a letter, so just add it to the result
            result += char

    return result

def encrypt():
    plaintext = entry.get()
    shift = int(shift_entry.get())
    ciphertext = caesar_cipher(plaintext, shift)
    output_label.config(text=ciphertext)

def decrypt():
    ciphertext = entry.get()
    shift = int(shift_entry.get())
    plaintext = caesar_cipher(ciphertext, -shift)
    output_label.config(text=plaintext)

# Create the GUI window
window = tk.Tk()
window.title("Caesar Cipher")

# Create the input label and entry box
input_label = tk.Label(window, text="Enter text to encrypt or decrypt:")
input_label.pack()
entry = tk.Entry(window)
entry.pack()

# Create the shift label and entry box
shift_label = tk.Label(window, text="Enter the shift amount:")
shift_label.pack()
shift_entry = tk.Entry(window)
shift_entry.pack()

# Create the encrypt and decrypt buttons
encrypt_button = tk.Button(window, text="Encrypt", command=encrypt)
encrypt_button.pack()
decrypt_button = tk.Button(window, text="Decrypt", command=decrypt)
decrypt_button.pack()

# Create the output label
output_label = tk.Label(window, text="")
output_label.pack()

# Run the GUI window
window.mainloop()
