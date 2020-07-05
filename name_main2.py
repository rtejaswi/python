import name_main1
def two():
    print('this is inside two()')
name_main1.one()
if __name__ == '__main__':
    print('the tow() is running directly')
else:
    print('two() is not running directly')
