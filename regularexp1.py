'''import re 

v = "Aye aye captain"
# class [abcde] will match with string with 'a', 'b', 'c', 'd', 'e'. 
p = re.compile('[a-e]') 

# findall() searches for the Regular Expression and return a list upon finding 
print(p.findall(v))'''

'''import re 

# \d is equivalent to [0-9]. 
p = re.compile('\d') 
print(p.findall("I came to Qspiders 10 A.M. on 3rd Oct 2019")) 

# \d+ will match a group on [0-9], group of one or greater size 
p = re.compile('\d+') 
print(p.findall("I came to Qspiders 10 A.M. on 3rd Oct 2019"))'''


'''import re 

# '*' replaces the no. of occurrence of a character. 
p = re.compile('ab*') 
print(p.findall("ababbaabbb"))'''


'''from re import split 

# '\W+' denotes Non-Alphanumeric Characters or group of characters 
# Upon finding ',' or whitespace ' ', the split(), splits the string from that point 
print(split('\W+', 'Words, words , Words')) 
print(split('\W+', "Word's words Words")) 

# Here ':', ' ' ,',' are not AlphaNumeric thus, the point where splitting occurs 
print(split('\W+', 'On 12th Jan 2016, at 11:02 AM')) 

# '\d+' denotes Numeric Characters or group of characters 
# Splitting occurs at '12', '2016', '11', '02' only 
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM'))'''


'''import re 

# Splitting will occurs only once, at '12', returned list will have length 2 
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1)) 

# 'Boy' and 'boy' will be treated same when flags = re.IGNORECASE 
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags = re.IGNORECASE)) 
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here'))'''


'''import re 

# Regular Expression pattern 'ub' matches the string at "Subject" and "Uber". 
# As the CASE has been ignored, using Flag, 'ub' should match twice with the string 
# Upon matching, 'ub' is replaced by '$' in "Subject", and in "Uber", 'Ub' is replaced. 
print(re.sub('ub', '$' , 'Subject has Uber booked already', flags = re.IGNORECASE)) 

# Consider the Case Senstivity, 'Ub' in "Uber", will not be reaplced. 
print(re.sub('ub', '$' , 'Subject has Uber booked already')) 

# As count has been given value 1, the maximum times replacement occurs is 1 
print(re.sub('ub', '$' , 'Subject has Uber booked already', count=1, flags = re.IGNORECASE)) 

# 'r' before the patter denotes RE, \s is for start and end of a String. 
print(re.sub(r'\sAND', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE))'''


'''import re 
print(re.subn('ub', '$' , 'Subject has Uber booked already')) 
t = re.subn('ub', '$' , 'Subject has Uber booked already', flags = re.IGNORECASE) 
print(t) 
print(len(t)) 

# This will give same output as sub() would have 
print(t[0])''' 






