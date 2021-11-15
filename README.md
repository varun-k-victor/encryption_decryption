# encryption_decryption

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" width="100" height="100" />

# About the scripts

encryption_code.py Applies two layers of encryption on the text.decryption_code.py decrypts the encrypted message.

# How to use

Sender of the message runs encryption_code.py to apply two layers of encryption to plain text and generates two files, ciphertext_1.txt and ciphertext_2.dat, which 
stores secret data and needs to be sent to the reciever of the message.The reciever of the message then runs decryption_code.py which requires those two files to 
decrypt the text. 

# Prerequisite

-> Pycryptodome

# Note

Run encryption_code.py first.For decryption_code.py to work,the user must have ciphertext_1.txt and ciphertext_2.dat stored in the same location,where 
decryption_code.py is stored.
