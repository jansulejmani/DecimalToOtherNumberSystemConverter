import math

base = input("Enter base of your aim number system ( between 2 and 36 ): ")
number = input("Enter the number you want to convert from the decimal system: ")


letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

rest = int(number) % int(base)
result = math.floor(int(number) / int(base))
print(f"{number} : {base} = {result} Rest {rest}")
resulting_string = str(rest)

while result != 0:
	prior_result = result
	rest = int(prior_result) % int(base)
	result = math.floor(int(prior_result) / int(base))
	print(f"{prior_result} : {base} = {result} Rest {rest}")
	
	if rest >= 10:
		rest = letters[rest - 10]

	resulting_string += str(rest)

resulting_string = resulting_string[::-1]
print(f"\n ---> {number}(10) = {resulting_string}(2)")



