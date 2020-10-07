a= input('Enter a string: ')
b = ''
c=''
for i in a:
    if i.isalnum() or i.isspace():
        b += i
print('New string:',b)

i=0
while i in range(len(a)):
    if a[i].isalnum() or a[i].isspace():
        c += a[i]
    i+=1
print('New string:',c)