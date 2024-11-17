# myfile = open("test", "w")

# print("hello", end=" ", file=myfile)
# print("my", "friends", sep="-", file=myfile)
# import time
# message = "hello my friends"
# for c in message:
#     print(c, end="", flush=True)
#     time.sleep(0.2)

# ruler = int(input("enter a number: "))

x = 12
y = 13
print(x + y)

numbers = [1,2,3,4,5]
print(sum(numbers))
s = 0
for n in numbers:
    s += n
print(s)

fruits = ["apple", "banana", "cherry"]
for f in fruits:
    if len(f) > 5:
        print(f)
        
numbers = (1,10, 5)
print(max(numbers))
names = ("nima", "nikan", "sara", "sama")
if "sama" in names:
    print("yes")