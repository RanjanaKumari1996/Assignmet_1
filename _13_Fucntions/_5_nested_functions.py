def outer():
    print("you are inside the outer function")
    def inner():
        print("you are inside the inner function")
    inner()


outer()