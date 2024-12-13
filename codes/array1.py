cars = ["Ford", "Volvo", "BMW"]

carlist = list(cars)
p = cars.index('BMW')
cars.insert(1,'Toyota')

print(cars)
print('P = ',p)

number = [ 7, 6 ,4,2 , 9 , 20]
number.sort(reverse=True)
print(number)

plainText = 'bird'
cesar =list('    ')
decypher = list('    ')
for i in range(4):
	cesar[i] = chr(ord(plainText[i])+2)
    
for i in range(4):
	decypher[i] = chr(ord(cesar[i])-2)

print(plainText)
print(cesar)
print(decypher)
