#Create a tuple, contains the odd number from 1 to 20
m = ()
for i in range(1,21):
    if (i % 2 != 0):
        m+=(i,)
print(m) 
    
#Create a list, repeat 1 to 5 sequentially 3 times
m = []
for i in range(1,6):
    j = 3
    while (j > 0):
        m.append(i)
        j-=1
print(m)

#Create a list, contains the multiples of 50
m = []
for i in range(1,50):
    if (i % 5 == 0):
        m.append(i)
print(m)

#Create a set e, contains "NASDAQ", "Dowjones", "DAX", "FTSE"
e = ("NASDAQ", "Dowjones", "DAX", "FTSE")
print(e)

#Transform  "abc" to tuple, list, set:
a = ("abc",)
print(type(a))

a = ["abc"]
print(type(a))

a = {"abc"}
print(type(a))

# Find "A", "b", "\n" ASCII, use these as keys, and ASCII code as values for a dict
a = {"A":65, "b": 98, "\n": 10}
print(a["\n"])
