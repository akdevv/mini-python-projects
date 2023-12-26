# Caesar Cipher

## Overview
This Python project provides a simple implementation of the Caesar Cipher encryption and decryption algorithm. The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Features
- Encryption of plaintext
- Decryption of ciphertext
- Support for customizable shift values

## How to Use
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/akdevv/mini-python-projects.git
    cd mini-python-projects
    cd caesar-cipher
    ```
2. **Run _main.py_:**
    ```bash
    python main.py
    ```

## Examples 
```          
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
              
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello
Type the shift number:
5
Here's the encoded result: mjqqt
Type 'yes' if you want to go again. Otherwise type 'no'.
yes
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
mjqqt
Type the shift number:
5
Here's the decoded result: hello
Type 'yes' if you want to go again. Otherwise type 'no'.
no
Goodbye
```