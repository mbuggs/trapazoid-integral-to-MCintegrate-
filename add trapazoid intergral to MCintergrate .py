Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def trap(f, a, b, n):
...     h = (b - a) / n  
...     integral = 0.5 * (f(a) + f(b))  
... 
...     for i in range(1, n):
...         x = a + i * h
...         integral += f(x)  
... 
...     integral *= h  
...     return integral
... 
... 
... def f(x):
...     return x ** 2
... 
... a = 0  
... b = 2  
... n = 100  
... 
... result = trap(f, a, b, n)
... print("Approximate integral:", result)
