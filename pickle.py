import pickle
data = ['qwertyuiopasdfghjklzxcvbnm']
print('before',type(data))
fileobj = open('t:/pickle1.pkl','wb')
data1 = pickle.dump(data,fileobj,pickle.HIGHEST_PROTOCOL)
print(data1)
print(type(data1))
fileobj.close()
