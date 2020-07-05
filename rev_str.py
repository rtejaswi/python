def reverse(string): 
	if len(string)==0: 
		return
	a=string[0]
	reverse(string[1:]) 
	print(a,end='')  
string = 'karma'
print(string)
reverse(string) 
