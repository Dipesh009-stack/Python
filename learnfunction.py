def newfunction():
    """
    This is a document string
    :return:
    """
    print("I have built a new function")
    print("this is just a function")

def newfunction2(msg):
     print(msg)
newfunction2("hello world")


def newfunction3(msg):
    """This function is just a practice function which takes an argument"""
    if isinstance(msg,str):
        print(msg)
    else:
        print("your message is not a string")
        print("here is the type of what you have supplied ",type(msg))

newfunction3("ram")


