# ==> Global Variable

globalval = "I am global variable"


def myfun1():
    print(f"Inside function myfun1: {globalval}")


myfun1()  # * Inside function myfun1: I am global variable

print(
    "Outside function myfun1: ", globalval
)  # * Outside function myfun1:  I am global variable

# ? Local Variable


def myfun2():
    localval = "I am local variable"
    print(f"Inside function myfun2 {localval}")


myfun2()  # * Inside function myfun2 I am local variable
# print(localval) #! NameError: name 'localval' is not defined. Did you mean: 'globalval'?

# ? Same name for local and Global variable

globalvar = "I am Global"


def myfun3():
    globalvar = "I am Local"  # ? Override lote lite tar
    print("Inside function myfun3: ", globalvar)


myfun3()  # * Inside function myfun3:  I am Local
print("Outside function myfun3: ", globalvar)  # * Outside function myfun3:  I am Global

# todo Exercise including global keyword
msg1 = "Hello Sir, this is global variable."


def funone():
    msg2 = "Hi student, this is local variable."
    print("inside function funone = ", msg1)
    print("inside function funone: ", msg2)


funone()


def funtwo():
    msg1 = "Hello Teacher, this is local variable"
    msg2 = "Hi Staffs, this is local variable"
    print("Inside function fun2: ", msg1)
    print("Inside function fun2: ", msg2)


funtwo()
# print("Outside function funtwo: ", msg2) #! NameError: name 'msg2' is not defined. Did you mean: 'msg1'?


def myfunthree():
    global msg1  # ? tat tat htet pay tat new variable ma hote buu a pyin ka kg ko override lote tar par
    msg1 = "Hello Boss, this is local variable"
    msg2 = "Hello Employee, this is local variable"
    print("inside function funthree: ", msg1)
    print("inside function funthree: ", msg2)


myfunthree()
print("outside function myfunthree: ", msg1)
# print("outside function myfunthree: ", msg2) #! Error

# ? Nested Function and nonlocal keyword


def funfour():
    msg3 = "msg3 from outside funfive()"

    def funfive():
        nonlocal msg3
        msg3 = "I am msg3 modified by funfive"
        print(msg3)

    print("Before invoking funfive: ", msg3)
    funfive()
    print("After invoking funfive: ", msg3)


funfour()
