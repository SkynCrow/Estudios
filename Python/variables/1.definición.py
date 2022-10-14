# En este fichero se ejemplificara como crear variables de todo tipo.
# Dejando en claro cual es la diferencia con otros lenguajes

# Asignaciones

website = "apple.com"
print('Variable website asignada como: ' + website)

# Se reasigna la variable

website = "programiz.com"
print('Variable website reasignada como: ' + website)

# Asignaciones multiples

a, b, c = 5, 3.2, "Hello"

print ('a: ' + str(a))
print ('b: ' + str(b))
print ('c: ' + str(c))

x = y = z = "same"

print ('x: ' + x)
print ('y: ' + y)
print ('z: ' + z)
# Constantes
PI = 3.14
GRAVITY = 9.8
print('PI: ' + str(PI))
print('GRAVITY: ' + str(GRAVITY))
# En realidad, python no usa constantes.
# Nombrar las variables en mayúscula es una convención
# para separarlas de las demás variables, sin embargo, 
# esto no previene que sean reasignadas.

# Convenciones de nombres
# - snake_case
# - MACRO_CASE
# - camelCase
# - CapWords

# Asignaciones literales

a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal

float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 

x = 3.14j

print(f'a: {a},b: {b},c: {c},d: {d}')
print(f'float_1: {float_1}, float_2: {float_2}')
print(f'x: {x}, x.imag: {x.imag},x.real {x.real}')

# Asignaciones literales de cadenas

strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

# Asignaciones literales de booleanos

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

# Asignaciones literales especiales

drink = "Available"
food = None

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

menu(drink)
menu(food)

# Asignaciones literales de colecciones

fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)
