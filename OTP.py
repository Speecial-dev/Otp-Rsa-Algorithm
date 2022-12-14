
# os.randum is more secure for generating random numbers
from random import randint

character_list = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ,./\;:"[]{}()_-!@#$%^&*|?<>`~'

def generate_otp(sheets, length):

	
	for sheet in range(sheets):
		with open("otp" + str(sheet) + ".txt", "w") as f:

			
			for i in range (length):
				f.write(str(randint(0, 81)) + "\n")


def load_sheet(filename):
	with open(filename, "r") as f:

		
		contents = f.read().splitlines()

	return contents


def get_plaintext():
	plain_text = input('Enter your message: ')

	return plain_text


def load_file(filename):

	
	with open(filename, 'r') as f:
		contents = f.read()

	return contents


def save_file(filename, data):

	
	with open(filename, 'w') as f:
		f.write(data)


def encrypt(plaintext, sheet):
	ciphertext = ''

	
	for position, character in enumerate(plaintext):

		
		if character not in character_list:
			ciphertext += character
		else:
			
			encrypted = (character_list.index(character) + int(sheet[position])) % 81

			
			ciphertext += character_list[encrypted]

	return ciphertext


def decrypt(ciphertext, sheet):
	plaintext = ''

	for position, character in enumerate (ciphertext):

		if character not in character_list:
			plaintext += character
		else:
			decrypted = (character_list.index(character) - int(sheet[position])) % 81
			plaintext += character_list[decrypted]

	return plaintext


def menu():
	choices = ['1', '2', '3', '4']
	choice = '0'

	
	while True:
		print('1. Generate one-time pads')
		print('2. Encrypt a message')
		print('3. Decrypt a message')
		print('4. Quit program')

		
		choice = input('Enter number: ')

		
		if choice == '1':
			sheets = int(input('How many OTP should be generated? '))
			length = int(input('What will be the maximum message length? '))

			generate_otp(sheets, length)

		elif choice == '2':
			filename = input('Enter filename of the OTP you want to use: ')
			sheet = load_sheet(filename)
			plaintext = get_plaintext()
			ciphertext = encrypt(plaintext, sheet)
			filename = input('Enter name of encrypted file: ')

			save_file(filename, ciphertext)

		elif choice == '3':
			filename = input('Enter filename of the OTP you want to use: ')
			sheet = load_sheet(filename)
			filename = input('Type the name of the file to be decrypted: ')
			ciphertext = load_file(filename)
			plaintext = decrypt(ciphertext, sheet)

			print('Decrypted Message: \n' + plaintext)

		elif choice == '4':
			exit()

		
		choice = '0'



menu()
