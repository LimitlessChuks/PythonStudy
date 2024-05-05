Built-in Functions

A
abs()
aiter()
all()
anext()
any()
ascii()

B
bin()
bool()
breakpoint()
bytearray()
bytes()

C
callable()
chr()
classmethod()
compile()
complex()

D
delattr()
dict()
dir()
divmod()

E
enumerate()
eval()
exec()

F
filter()
float()
format()
frozenset()

G
getattr()
globals()

H
hasattr()
hash()
help()
hex()

I
id()
input()
int()
isinstance()
issubclass()
iter()
L
len()
list()
locals()

M
map()
max()
memoryview()
min()

N
next()

O
object()
oct()
open()
ord()

P
pow()
print()
property()




R
range()
repr()
reversed()
round()

S
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()

T
tuple()
type()

V
vars()

Z
zip()

_
__import__()


# The following Python code defines a function called histogram that takes a string s as input and returns a dictionary representing the histogram of the characters in the string:

def histogram(s):
#     """
#     Returns a histogram of the characters in a string.

#     Parameters:
#     s (str): The string to create a histogram for.

#     Returns:
#     dict: A dictionary where the keys are the characters in the string and the values are the corresponding frequencies.
#     """
d = dict()
for c in s:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1
return d


# Here's a step-by-step explanation of the code:

# 1. def histogram(s):: This line defines a Python function named histogram that takes one argument, s, which is expected to be a string.

# 2. """ ... """: This is a docstring that provides documentation for the function. It describes the purpose of the function, the parameter it takes, and the return value.

# # 3. d = dict(): This line creates an empty dictionary called d. This dictionary will be used to store the histogram, where the keys will be the characters in the string and the values will be the corresponding frequencies.

# 4. for c in s:: This line starts a for loop that iterates over each character c in the input string s.

# 5. if c not in d:: Inside the loop, this line checks if the current character c is not already a key in the d dictionary. If c is not in the dictionary, it means that this is the first time we've encountered this character in the string.

# 6. d[c] = 1: If c is not in the dictionary, this line adds it as a key with a value of 1. This indicates that we've encountered this character once so far.

# 7. else:: If c is already a key in the dictionary, this else block is executed.

# 8. d[c] += 1: Inside the else block, this line increments the value associated with the key c by 1. This means that we've encountered this character again, so we increase its frequency count by 1.

# 9. return d: After iterating through all the characters in the string and updating the dictionary accordingly, this line returns the d dictionary as the result of the histogram function. The dictionary contains the histogram of the characters in the input string.

# In summary, the histogram function takes a string as input and creates a dictionary where the keys are the characters in the string and the values are the corresponding frequencies of occurrence. This dictionary represents the histogram of the characters in the string and is returned as the output of the function.



# The following Python code defines a function called print_hist that takes a dictionary h as input and prints the keys and values of the dictionary in a formatted manner:

def print_hist(h):
    # """
    # Prints a histogram represented by a dictionary.

    # Parameters:
    # h (dict): A dictionary where the keys are the characters and the values are the corresponding frequencies.
    # """
    for c in h:
        print(c, h[c])


# Here's a step-by-step explanation of the code:

# 1. def print_hist(h):: This line defines a Python function named print_hist that takes one argument, h, which is expected to be a dictionary.

# 2. """ ... """: This is a docstring that provides documentation for the function. It describes the purpose of the function and the parameter it takes.

# 3. for c in h:: This line starts a for loop that iterates over each key c in the input dictionary h.

# 4. print(c, h[c]): Inside the loop, this line prints the key c followed by the corresponding value h[c] from the dictionary. This prints each character along with its frequency in a formatted manner.

# In summary, the print_hist function takes a dictionary representing a histogram as input and prints the characters (keys) and their corresponding frequencies (values) in a formatted manner.