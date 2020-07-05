import re

data = "end of the python class"

sub1 = re.sub(r'\A\w','$',data)
sub2 = re.sub(r'\w{1}\Z','$',data)
print(data)
print(sub1)
print(sub2)



'''import re

data = "end of the python class"

sub1 = re.sub(r'\b\w{1}','$',data)
sub2 = re.sub(r'\b\w{0}','$',sub1)
print(data)
print(sub1)
print(sub2)'''




