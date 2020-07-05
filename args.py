#args

# blog1 = 'Hi Im Tejaswi'
# blog2 = 'Im learnimg Python'
# blog3 = 'and I like coding'
#
# my_title = '*****My Blog*****'
#
# def my_blog(title, *args):
#     print(title)
#     print('the blogs are')
#     for post in args:
#         print(post)
# my_blog(my_title, blog1, blog2, blog3)



#**kwrgs

# my_title = '*****My Blog*****'
#
# def my_blog(title, **kwargs):
#     print(title)
#     print('the blogs are')
#     for post in kwargs.items():
#         print(post)
# my_blog(my_title,blog1 = 'Hi Im Tejaswi',
#                  blog2 = 'Im learnimg Python',
#                  blog3 = 'and I like coding')


#**kwrgs & *args

my_title ='*****My Blog*****'

def my_blog(title, *args, **kwargs):
    print(title)
    print('The blogs are:')
    for arg in args:
        print(arg)
    for post in kwargs.items():
        print(post)
my_blog(my_title,'1', '2', '3', blog1 = 'Hi Im Tejaswi',
                 blog2 = 'Im learnimg Python',
                 blog3 = 'and I like coding')
