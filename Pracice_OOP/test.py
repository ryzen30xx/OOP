a = 100
b = 'ABC'
print(isinstance(a, (int, float))) #if a = 100 => True because a have integer value

print(isinstance(b, (int, float))) # if a = 100 => have False result because B is String value and in requirement, I only request check b is integer or float

if (isinstance(b, (int, float)) and a >= 100):
	print('That is integer and equal or lower 100')
else:
	print('That is not integer or float and higher 100')