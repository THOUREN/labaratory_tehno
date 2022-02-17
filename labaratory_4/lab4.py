def decode(s:str, k:int=1):
    d = {x+1:'' for x in range(k)}
    c=0
    v=1
    h=(len(s)-(len(s)//k)*k)
    while(v<=h):
        for j in range((len(s)//k)+1): 
            d[v] += s[j+c]
        c +=(len(s)//k)+1
        v +=1
    while(v<k+1):
        for j in range((len(s)//k)):
            d[v] += s[j+c]
        c +=(len(s)//k)
        v +=1
    x = []
    c=0
    while(c<(len(s)//k)):
        for j in d.values():
            x.append(j[c])
        c+=1
    for i in range(h):
        x.append(d[i+1][-1])
    return ''.join(x)
 
def encode(s:str, k:int=1):
    d = {x+1:'' for x in range(k)}
    for i in [s[0+x:k+x] for x in range(0, len(s), k)]:
        c = 1
        for j in i:
            d[c] += j
            c += 1
    return ''.join([x for x in d.values()])

f = open('codeFileName.txt', 'r', encoding="utf-8")
c = open('codeFileEncode.txt', 'w', encoding="utf-8")
strtocode = f.read()
keycode = int(input("Введите ключь(число):"))
 
print('Исходная строка:',strtocode,'Ключ:',keycode)
print('Шифрование: ',encode(strtocode,keycode))
#print('Декодируем:',decode(encode(strtocode,keycode),keycode))

s2 = ''
s1 = encode(strtocode,keycode)
key = '314'
for i in range(len(s1)):
	if ord(s1[i]) < 253:
		s2 = s2 + chr(ord(s1[i])+int(key[i%len(key)]))
	else:
		s2 = s2 + chr(ord(s1[i])+int(key[i%len(key)])-255)
print("Зашифрованная строка:", s2)
c.write(s2)
c.close()
g = open('codeFileEncode.txt', 'r', encoding="utf-8")
s2 = g.read()
s1 = ''
for i in range(len(s2)):
	if ord(s2[i]) < 253:
		s1 = s1 +chr(ord(s2[i])-int(key[i%len(key)]))
	else:
		s1 = s1 +chr(ord(s2[i])-int(key[i%len(key)])+255)
print("Дешифрованная строка:", s1)
print('Декодируем:',decode(s1,keycode))
s3 = decode(s1,keycode)
q = open('codeFileDecode.txt', "w", encoding="utf-8")
q.write(s3)
q.close()
