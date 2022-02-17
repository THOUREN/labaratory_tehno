s2 = ''
s1 = input("Введите исходную строку: ")
for i in range(len(s1)):
	if ord(s1[i]) < 253:
		s2 = s2 + chr(ord(s1[i])+3)
	else:
		s2 = s2 + chr(ord(s1[i])+3-255)
print("Зашифрованная строка:", s2)

s1 = ''
for i in range(len(s2)):
	if ord(s2[i]) < 253:
		s1 = s1 +chr(ord(s2[i])-3)
	else:
		s1 = s1 +chr(ord(s2[i])-3+255)
print("Дешифрованная строка:", s1)
print("----------------------------------------------")
