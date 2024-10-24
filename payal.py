Python 3.12.6 (v3.12.6:a4a2d2b0d85, Sep  6 2024, 16:08:03) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
rad=float(input("enter radius of circle"))
print=(rad)
print=(type(rad))
SyntaxError: multiple statements found while compiling a single statement
a,b=map(int,input("enter three integers separated by spaces:").split())
enter three integers separated by spaces:print(a,b)a,b=map(int,input("enter three integers separated by spaces:").split())
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a,b=map(int,input("enter three integers separated by spaces:").split())
ValueError: invalid literal for int() with base 10: 'print(a,b)a,b=map(int,input("enter'
a,b,c=map(int,input("enter three integers separated by spaces:").split())
enter three integers separated by spaces:print(a,b,c)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a,b,c=map(int,input("enter three integers separated by spaces:").split())
ValueError: invalid literal for int() with base 10: 'print(a,b,c)'
print(a,b,c)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(a,b,c)
NameError: name 'a' is not defined
a,b,c=map(int,input("enter three integers separated by spaces:").split())
enter three integers separated by spaces:4 5 6
print(a,b,c)
4 5 6
a,b,c=map(int,input("enter three integers separated by spaces:").split(","))
enter three integers separated by spaces:4 5 6
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a,b,c=map(int,input("enter three integers separated by spaces:").split(","))
ValueError: invalid literal for int() with base 10: '4 5 6'
a,b,c=map(int,input("enter three integers separated by spaces:").split(","))
enter three integers separated by spaces:4,5,6
print(a,b,c)
4 5 6
a,b,c=10,20,30
a,b,c=map(int,input("enter three integers separated by spaces:").split(","))
enter three integers separated by spaces:
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a,b,c=map(int,input("enter three integers separated by spaces:").split(","))
ValueError: invalid literal for int() with base 10: ''
a,b,c=map(int,input("enter three integers separated by commas:").split(","))
enter three integers separated by commas:4,5,6
print(a,b,c)
4 5 6

============== RESTART: /Users/payalkunwar/Desktop/python/Area.py ==============
28
a,b=input("enter two float numbers").split()
enter two float numbers3,6
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a,b=input("enter two float numbers").split()
ValueError: not enough values to unpack (expected 2, got 1)
a,b=input("enter two float numbers").split()
enter two float numbers4 5
print(a+b)
45
a,b=map(int,input("enter two float numbers").split())
enter two float numbers4 5
print(a+b)
9
print(a*b)
20
print(a**b)
1024
l,b=map(int,input("enter two float numbers").split())
enter two float numbers4 5
print(l*b)
20
print(2*(l))
8
print(2*(l+b))
18
a,b=map(int,input("enter two float numbers").split())
enter two float numbers6 7
print((a+b)/2)
6.5
a,b=map(int,input("enter two float numbers").split())
enter two float numbers8 9
a,b,c=map(int,input("enter three float numbers").split())
enter three float numbers3 5 8
print(2*(a*b+b*c+a*c))
158
a,b=map(int,input("enter two float numbers").split())
enter two float numbers3 4
print(pi*)
SyntaxError: invalid syntax
a,pi=map(int,input("enter two float numbers").split())
enter two float numbers4 3.14
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a,pi=map(int,input("enter two float numbers").split())
ValueError: invalid literal for int() with base 10: '3.14'
a,b=map(int,input("enter two float numbers").split())
enter two float numbers3 4
print(a*b*b)
48
print(a*(b*b))
48
print(a*b**2)
48
print(a*(b**2))
48
print(a*)(b**2))
SyntaxError: unmatched ')'

print(b**2*a)
48
print(b*b*a)
48
print(b**b*a)
768
print(b**a*b)
256
\
x=10
if x==10
SyntaxError: expected ':'
if x==10:
print("x is equal to 10")
SyntaxError: expected an indented block after 'if' statement on line 1
x=10
if x==10:
print("x is equal to 10")
SyntaxError: expected an indented block after 'if' statement on line 1
x=10
if x==10:
    print("x is equal to 10")

    
x is equal to 10
a=10
b=20
if a>b
SyntaxError: expected ':'
if a>b:
    print("a greater than b")
    else
    
SyntaxError: invalid syntax
if a>b:
    print("a greater than b")
    else
    
SyntaxError: invalid syntax

if a>b:
    print("a greater than b")
    else:
        
SyntaxError: invalid syntax




[DEBUG ON]
if a>b:
    print("a greater than b")
    else:
        
SyntaxError: invalid syntax
[DEBUG ON]
[DEBUG OFF]
a=33
b=33
if a>b:
    print("a is greater than b")

    
elia=33
b=33
if a>b:
    print("a is greater than b")
    
SyntaxError: multiple statements found while compiling a single statement
a=30
b=20
if a!=b
SyntaxError: expected ':'
a=30
b=20
if a!=b:
    
SyntaxError: multiple statements found while compiling a single statement
a,b=10,20
if a!=b
SyntaxError: expected ':'
a=30
b=20
if a!==b:
    
SyntaxError: multiple statements found while compiling a single statement
a=10
b=20
if a==b:
    print("both a and b are equal")
else:
    if a>b:
        print("a is greater than b")
    else:
        print("b is greater than a")

        
b is greater than a
ch1=input("enter a single character")
enter a single character9
if ch1>='0' and ch1<='9':
    print("you entered a digit")

    
you entered a digit
n1,n2=map(int,input("enter two integers").split())
enter two integers5 6
if(n1%n2==0):
else:
    
SyntaxError: expected an indented block after 'if' statement on line 1
n1,n2=map(int,input("enter two integers").split())
... enter two integers5 6
... if(n1%n2==0):
...     
SyntaxError: multiple statements found while compiling a single statement
>>> n1,n2=map(int,input("enter two integers").split())
... enter two integers5 6
... if(n1%n2=0):
...     
SyntaxError: multiple statements found while compiling a single statement
>>> n1,n2=map(int,input("enter two integers").split())
... enter two integers5 6
... if(n1%n2==0):
...     
SyntaxError: multiple statements found while compiling a single statement
>>> n1,n2=map(int,input("enter two integers").split())
... enter two integers5 6
SyntaxError: multiple statements found while compiling a single statement
>>> n1,n2=map(int,input("enter two integers").split())
... enter two integers5 6
SyntaxError: multiple statements found while compiling a single statement
>>> n1,n2=map(int,input("enter two integers").split())
... enter two integers5 6
SyntaxError: multiple statements found while compiling a single statement
>>> n1,n2=map(int,input("enter two integers").split())
... enter two integers5 6
SyntaxError: multiple statements found while compiling a single statement
>>> n1,n2=map(int, input("enter two integers").split())
... enter two integers5 6
SyntaxError: multiple statements found while compiling a single statement
>>> 
============================================ RESTART: /Users/payalkunwar/Documents/payal.pyy.py ============================================
enter a number8
num is even
>>> 
============== RESTART: /Users/payalkunwar/Documents/payal.pyy.py ==============
enter sale amount15000
you recieved discount Rs 1500.0
