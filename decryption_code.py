from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import time
import pickle

def main():
	print("loading ciphertext_2.dat...")
	time.sleep(3)
	file2=open("ciphertext_2.dat","rb")
	encrypted_2=pickle.load(file2)
	key_2=pickle.load(file2)
	iv=pickle.load(file2)
	file2.close()
	print("\n")

	print("AES decryption")
	time.sleep(2)
	print("decrypting text...")
	time.sleep(3)
	aes=AES.new(key_2,AES.MODE_CBC,iv)
	decrypted_2=aes.decrypt(encrypted_2)
	unpadded_text=unpad(decrypted_2,16)
	decoded_text=unpadded_text.decode()
	print("AES decryption successful")
	print("decrypted text: ",decoded_text)
	print("\n")

	print("loading ciphertext_1.txt...")
	time.sleep(3)
	file1=open("ciphertext_1.txt","r")
	key_1=int(file1.read())
	file1.close()
	print("\n")

	print("caesor decryption")
	time.sleep(2)
	print("decrypting text....")
	time.sleep(3)
	if(key_1>9 or key_1<1):
		print("caesor key should be a number between 1 and 9")
	else:
		decrypted_1=""
		for i in decoded_text:
			decrypted_1=decrypted_1+chr(ord(i)-key_1)
	print("caesor decryption successful")
	print("decrypted text: ",decrypted_1)
	
if __name__=="__main__":
	main()
