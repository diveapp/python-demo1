import os
print(os.access('/Users/dragon/my_code/python/demo1/test.txt', os.X_OK))

f = open('/Users/dragon/my_code/python/demo1/test.txt', 'wb+')

num = f.write(b'1234567890abcdef')

print('字数：{}'.format(num))

f.seek(4)
f.seek(1, 0)
print(f.read(1))
f.close()

f = open('/Users/dragon/my_code/python/demo1/test.txt', 'r')

print('-------------------------')

s = f.readline()
while s != '':
    print(s)
    s = f.readline()
else:
    print('下面没有了...')
