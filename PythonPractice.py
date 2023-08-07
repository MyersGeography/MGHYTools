import arcpy

# Indexing Strings

#trying to conceptually get ot the idea of "take a string and capitalize every 2nd letter"
# Like anthropomorphization -> aNtHroPoMoRpHiZaTiOn

#let's start with indexing
# this one works and will just spit out "y" because it's the 4th indexed letter.
ss = "Sammy Shark!"
nums = [1,3,5,7,9]
print(ss[4])

# another cool part of string parsing, is the "step"

print("anthropomorphization"[2])
#  ^^^ will return "t"
print("anthropomorphization"[:2])
#  ^^^ will return the first two letters of the string
print("anthropomorphization"[::2])
#  ^^^ will return every second letter (this is called the step)
# but I don't know if this helps me really, because I need to apply the .upper method to some parts of the string


def ConvertStringToList(str):
    stringlist=[]
    stringlist[:0] = str
    return stringlist

str2 = "anthropomorphization"
print(ConvertStringToList(str2))

print("anthropomorphization"[:0])

# But then, how to get a list of all the letters in the string?

# perhaps this problem is looking for an *args situation with a function

def argsEx(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)

argsEx("Stinky", "Stanky", "Stonky", "Stew")

# what if I create a split up

#def myfunc(word):
    # take string, if an index number is odd, change to upper case
    # I think this wants me to use a
    #x = word[0]

    #if x ==0:
        # capitalize the letter
    #else:
        #leave it alone

# an answer from the internet ...

def foo(s):
    ret = ""
    i = True # capitalize
    for char in s:
        if i:
            ret += char.upper()
        else:
            ret += char.lower()
        if char != ' ':
            i = not i
    return ret

print(foo("hello world"))


