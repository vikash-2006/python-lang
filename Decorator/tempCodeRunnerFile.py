def add_fun(fun):
    def add_func():
        print("This is the message")
        fun()
    return add_func



@add_fun
def hello():
    print("This is the message")
    print("Hello from the hello function")

hello()
