'''str = "Python"
reversedString=[]
index = len(str) # calculate length of string and save in index
while index > 0: 
    reversedString += str[ index - 1 ] # save the value of str[index-1] in reverseString
    index = index - 1 # decrement index
print(reversedString) # reversed string'''


'''str = 'Python' #initial string
reversed=''.join(reversed(str)) # .join() method merges all of the characters resulting from the reversed iteration into a new string
print(reversed) #print the reversed string'''


# Python code to reverse a string 
# using loop 

'''def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = "Python"

print ("The original string is : ",end="") 
print (s) 

print ("The reversed string(using loops) is : ",end="") 
print (reverse(s))'''

