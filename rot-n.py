#!/usr/bin/env python
# Simple ROT-Any Encryption/Decryption v1.2
# Daniel Neall


import os
import time

alpha = "abcdefghijklmnopqrstuvwxyz"

def rotate(strg,n):
   return strg[n:] + strg[:n]

# Encryption logic
def encrypt():
	plaintext   = input("What string should I encrypt?")
	plaintext = plaintext.lower()
	key = rotate(alpha, int(input("Shift by how many? (1-25)"))) # Use mod instead of limiting rotation value
	cipherTable = ''.maketrans (alpha, key)
	return plaintext.translate(cipherTable)

#Decryption logic
def decrypt():
  cipher = input("Input cipher to decrypt:")
  cipher = cipher.lower()
  key = rotate(alpha, int(input("Shift by how many?")))
  cipherTable = ''.maketrans (key, alpha)
  return cipher.translate(cipherTable)

#Front-end Menu Formatting
def mainMenu():
  #print (28 * '─')

  print ("   \t Main Menu")
  print (28 * '═')
  print ("1. Encrypt")
  print ("2. Decrypt")
  print ("3. Quit")
  print (28 * '═')

  choice = input('Enter your choice [1-3] : ')
  choice = int(choice)
 
### Front-end Menu Logic ###
  if choice == 1:
      	print (encrypt())
  elif choice == 2:
      	print (decrypt())
  elif choice == 3:
      	print ("Exiting")
  else:   
      	print ("Invalid number. Try again...")
      	time.sleep(3)
      	main()    	 
      	
mainMenu()

#EOF
