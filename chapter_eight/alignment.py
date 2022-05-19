from _ast import In

In[1]: print(f'[{"Amanda":>10}]\n[{"Amanda":^10}]\n[{"Amanda":<10}]')

In[2]: print(f'{10240.473:+10.2f} \n{-3210.9521:+10.2f}')

print()

name = '       Margo Magenta       '
print(name.strip())
print(name.lstrip())
print(name.rstrip())

print()

test_str = 'happy new year'.title()
print(test_str)
test_str = 'happy new year'.capitalize()
print(test_str)
test_str = 'happy new year'.upper()
print(test_str)

print()

for word in 'to be or not to be that is the the question'.split():
    if word.startswith('t'):
        print(word, end=" ")

