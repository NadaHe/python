print("Hello python")
print("I love python")

# type() => function to know data type
# All data in python is object

print(type([1, 2, 3, 4, 5]))
print(type((1, 2, 3, 4, 5)))
print(type({"one": 1, "two": 2, "three": 3}))  # "Key" : value

my_name = "Nada"  # snake case

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

help("keywords")  # to know all reserved keywords in Python

# ----------------------------
# Escape Sequences Characters
# \b => Back Space
# \newline => Escape New Line + \
# \\ => Escape Back Slash
# \' => Escape Single Quotes
# \" => Escape Double Quotes
# \n => Line Feed
# \r => Carriage Return
# \t => Horizontal Tab
# \xhh => Character Hex Value
# ----------------------------

# Back Space
print("Hello\bWorld")  # Will Remove o

# Escape New Line + Back Slash
print(
    "Hello \
I Love \
Python"
)

# Escape Back Slash
print("I Love Back Slash \\")

# Escape Single Quote
print("I Love Single Quote 'Test' ")

# Escape Double Quotes
print('I Love Double Quotes "Test" ')

# Line Feed
print("Hello World\nSecond Line")

# Carriage Return
print("123456\rAbcde")

# Horizontal Tab
print("Hello\tPython")

# Character Hex Value
print("\x4F\x73")

# -------------------
# -- Concatenation --
# -------------------

msg = "I Love"
lang = "Python"
print(msg + " " + lang)

full = msg + " " + lang
print(full)

a = "First \
Second \
Third"

b = "A \
B \
C"

print(a + "\n" + b)

# print("Hello " + 1)  # Error => we must convert int to string

print("=======================================================")


# ------------------------
# -- Strings Formatting old ways--
# ------------------------

name = "Osama"
age = 36
rank = 10

print("My Name is: " + name)
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error

print("My Name is: %s" % "Osama")
print("My Name is: %s" % name)
print("My Name is: %s and My Age is: %d" % (name, age))
print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name, age, rank))

# placeholders

# %s => String
# %d => Number
# %f => Float

n = "Osama"
l = "Python"
y = 10

print("My Name is %s Iam %s Developer With %d Years Exp" % (n, l, y))

# Control Floating Point Number

myNumber = 10
print("My Number is: %d" % myNumber)
print("My Number is: %f" % myNumber)
print("My Number is: %.2f" % myNumber)

# Truncate String [ ba5od eli ana 3ayzo mn el string w baseeb el ba2y]

myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("Message is %s" % myLongString)
print("Message is %.5s" % myLongString)

print("=======================================================")

# ---------------------------------
# -- Strings Formatting New Ways --
# ---------------------------------

name = "Osama"
age = 36
rank = 10

print("My Name is: " + name)
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error

print("My Name is: {}".format("Osama"))
print("My Name is: {}".format(name))
print("My Name is: {} My Age: {}".format(name, age))
print("My Name is: {:s} Age: {:d} & Rank is: {:f}".format(name, age, rank))

# {:s} => String
# {:d} => Number
# {:f} => Float

n = "Osama"
l = "Python"
y = 10

print("My Name is {} Iam {} Developer With {:d} Years Exp".format(n, l, y))

# Control Floating Point Number

myNumber = 10
print("My Number is: {:d}".format(myNumber))
print("My Number is: {:f}".format(myNumber))
print("My Number is: {:.2f}".format(myNumber))

# Truncate String

myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("Message is {}".format(myLongString))
print("Message is {:.5s}".format(myLongString))
print("Message is {:.13s}".format(myLongString))

# Format Money

myMoney = 500162350198

print("My Money in Bank Is: {:d}".format(myMoney))
print("My Money in Bank Is: {:_d}".format(myMoney))
print("My Money in Bank Is: {:,d}".format(myMoney))

# ReArrange Items

a, b, c = "One", "Two", "Three"
print("Hello {} {} {}".format(a, b, c))  # Hello One Two Three
print("Hello {1} {2} {0}".format(a, b, c))  # Hello Two Three One
print("Hello {2} {0} {1}".format(a, b, c))  # Hello Three One Two

x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z))
print("Hello {1:d} {2:d} {0:d}".format(x, y, z))
print("Hello {2:f} {0:f} {1:f}".format(x, y, z))
print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z))

# Format in Version 3.6+

myName = "Osama"
myAge = 36

print("My Name is : {myName} and My Age is : {myAge}")
print(f"My Name is : {myName} and My Age is : {myAge}")

print("=======================================================")

# -------------
# -- Numbers --
# -------------

# Integer

print(type(1))
print(type(100))
print(type(10))
print(type(-10))
print(type(-110))

# Float

print(type(1.500))
print(type(100.99))
print(type(-10.99))
print(type(0.99))
print(type(-0.99))

# Complex

myComplexNumber = 5 + 6j

print(type(myComplexNumber))

print("Real Part Is: {}".format(myComplexNumber.real))
print("Imaginary Part Is: {}".format(myComplexNumber.imag))

# [1] You Can Convert From Int To Float or Complex
# [2] You Can Convert From Float To Int or Complex
# [3] You Cannot Convert Complex To Any Type

print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

print(10 + 9j)
# print(int(10 + 9j)) # can not convert complex to int

print("=======================================================")

# --------------------------
# -- Arithmetic Operators --
# --------------------------
# [+] Addition
# [-] Subtraction
# [*] Multiplication
# [/] Division
# [%] Modulus
# [**] Exponent
# [//] Floor Division
# --------------------------

# Addition

print(10 + 30)  # 40
print(-10 + 20)  # 10
print(1 + 2.66)  # 3.66
print(1.2 + 1.2)  # 2.4

# Subtraction

print(60 - 30)  # 30
print(-30 - 20)  # -50
print(-30 - -20)  # -10
print(5.66 - 3.44)  # 2.22

# Multiplication

print(10 * 3)  # 30
print(5 + 10 * 100)  # 1005
print((5 + 10) * 100)  # 1500

# Division

print(100 / 20)  # 5.0
print(int(100 / 20))  # 5

# Modulus

print(8 % 2)  # 0
print(9 % 2)  # 1
print(20 % 5)  # 0
print(22 % 5)  # 2

# Exponent

print(2 ** 5)  # 32
print(2 * 2 * 2 * 2 * 2)  # 32
print(5 ** 4)  # 625
print(5 * 5 * 5 * 5)  # 625

# Floor Division

print(100 // 20)  # 5
print(119 // 20)  # 5
print(120 // 20)  # 6
print(140 // 20)  # 7
print(142 // 20)  # 7

print("=======================================================")

