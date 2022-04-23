def my_new_decorator(function_to_decorate):
    def the_wrapper_function():
        print("this a code, before function")
        function_to_decorate()
        print("this is a code, after function")
    return the_wrapper_function


def stand_alone_function():
    print("I am only ordinary function.")


@my_new_decorator
def another_stand_alone_function():
    print("I am the second ordinary function")



another_stand_alone_function()
дескриптор

#pickling unpickling

#intrenals of django. ORMc