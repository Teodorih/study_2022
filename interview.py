# ***************************************
# 1. Multiprocessing/Multithreading/Async

# ***************************************


# ***************************************
# 2. Decorators function/class
import time


def time_decorator(function):
    def wrapper():
        start_time = time.now()
        result = function()
        end_time = time.now()
        print(f'Time executing: {end_time - start_time}')
        return result

    return wrapper


@time_decorator
def my_function():
    print("It's out first function")
    # ***************************************

    # ***************************************
    # 3. What are the benefits of Generators
    # ***************************************

    # ***************************************
    # 4. Pickling & Unpickling. jwt, salt
    # 4.1 celery + redis. Очереди. Memcache
    # ***************************************

    # **************************************
    # 5. Packages and Modules in python
    # 5.1 Why we need __init__.py ?
    # 5.2 inside /app/__init__.py
    print("Hello World")

    # inside /app/some_class.py


# **************************************


# ******************************************************
# 6. Dynamic class generation using "XXXX" function.
# ******************************************************
def generate_class_by_user_inputs(*args, **kwargs) -> object:
    return type(*args, **kwargs)


# 7. Duck typing
class Human():
    def some_method(self):
        pass


class Person(Human):
    pass


class Person():
    def some_method(self):
        pass


# ******************************************************
# 7. Singleton
# ******************************************************
class App:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance
        cls._instance = super(App, cls).__new__(*args, **kwargs)
        return cls._instance

# ********************************************************


# 8. Lazy Loading
# ********************************************************


# *****************************************************
# 9. bubble_sort сложность сортировки
# *****************************************************


# *******************************************************
# SQL
# 10. Difference between WHERE and HAVING ?
# *******************************************************



# ********************************************************
# 11. Pagination in SQL
# ********************************************************
def list_users_with_pagination(amount, offset) -> str:
    # Return 50 users starting form the 70th
    return """select * from users offset offset limit amount"""


# ********************************************************
# 12. SQL Joins
# ********************************************************
# Fetch users with their profile data. User should be destructured while profile not.


