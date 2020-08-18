#!/usr/bin/python3

print("hello, python!")

str='abcdefg'
print(str)
print(str[0:-2])
print(str[2])
print(str[3:])
print(str*2)
print(str+"hlij")

#转义
print('abc \ndef')

#不转义
print(r'abc \n def')

dict = {
    'api.register': ['email', 'username', 'password']
}

for i in dict:
    print(type(i))
    print(i)

print('{a}'.format(a='123'))
