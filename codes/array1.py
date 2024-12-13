KEY=2

def encryption(plainText):
  cesar =list('    ')
  for i in range(len(plainText)):
	  cesar[i] = chr(ord(plainText[i])+KEY)
  return cesar
                 
def decryption(cypherText):
	decypher = list('    ')
	for i in range(len(cypherText)):
		decypher[i] = chr(ord(cypherText[i])-KEY)
	return decypher
                 

plainText = 'bird'

print(encryption(plainText))
print(decryption(encryption(plainText)))
