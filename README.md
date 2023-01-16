This is my first own Python project. I wanted to do something different, something that was not covered in the first Python Programming MOOC course I took.
This program is to organize and store passwords encrypted.
I imported a Fernet module that allows me to encrypt text. The program asks the user for a username and password, which it saves encrypted in a txt file, using Fernet cryptography for encryption.
Actually, this is not a secure way to encrypt passwords. This method is not recommended for encrypting passwords in real life.