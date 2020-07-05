import json
data = {'name':'Nimish','age':'22','job':'student','location':'bengaluru'}
print('before parsing',type(data))
fileobj = open('t:/abc.txt','w')
temp = json.dump(data,fileobj)
print(temp)
print('after parsing',type(temp))
fileobj.close()

fileobj = open('t:/abc.txt','r')
temp1 = json.load(fileobj)
print(temp1)
print(type(temp1))
fileobj.close()


'''import json
data = {'name':'Nimish','age':'22','job':'student','location':'bengaluru'}
print('before parsing',type(data))
fileobj = open('t:/abc.txt','w')
temp = json.dumps(data)
print(temp)
print(type(temp))
fileobj.write(temp)
print('after parsing',type(temp))
fileobj.close()

fileobj = open('t:/abc.txt','r')
n = fileobj.read()
print(n)
temp1 = json.loads(n)
print(temp1)
print(type(temp1))
fileobj.close()'''

