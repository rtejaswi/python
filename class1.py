# parent class 
class Person( ):
    def __init__(self, name, idnumber,post,salary=False):
        self.name = name
        self.idnumber = idnumber
        self.post = post
        self.salary = salary
    def display(self):
        print(self.name)
        print(self.idnumber)
        print(self.post)
        print(self.salary)
        print('-------------')
    def change(self):
        if self.salary==False:
            self.salary=(int(input('enter the salary')))
        else:
            print('nothing')
# child class 
class Employee( Person ):
    def __init__(self, name, idnumber, post, salary=False):
        self.name = name
        self.idnumber = idnumber
        self.salary = salary
        self.post = post
    def display(self):
        print(self.name)
        print(self.idnumber)
        print(self.post)
        print(self.salary)
        print('-------------')
    def change(self):
        if self.salary==False:
            self.salary=(int(input('enter the salary')))
        else:
            print('nothing')
a1 = Person('Sachin',786007,'tester')
a2 = Person('Tejaswi',786007,'developer',600000)
b1 = Employee('Naveen',7367878,'analyst')
b2 = Employee('Nimish',7367878,'developer',450000)
a1.display()
a2.display()
b1.display()
b2.display()
a1.change()
a2.change()
a1.display()
a2.display()
b1.change()
b2.change()
b1.display()
b2.display()

