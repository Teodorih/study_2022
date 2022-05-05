def formatter(tag):
    def inner(func):
        def wrapper(*args):
            html = f'<{tag}>'
            html += func(*args)
            html += f'</{tag}>'
            return html

        return wrapper
    return inner


@formatter('b')
def hello(name):
    return f'hello, {name}'


@formatter('i')
def goodbye(name, reason):
    return f'goodbye, {name}: {reason}'


print(hello('Bob'))
assert hello('Bob') == '<b>hello, Bob</b>'
print(goodbye('John', 'not good enough'))
assert goodbye('John', 'not good enough') == '<i>goodbye, John: not good enough</i>'


class CharField(object):
    val = None

    def __init__(self, max_length=4000):
        self.max_length = max_length

    def __get__(self, obj, objtype):
        return self.val

    def __set__(self, obj, val):
        if len(val) <= self.max_length:
            self.val = val


class Model(object):
    title = CharField(max_length=3)


m = Model()

m.title = '1234'
assert m.title is None

m.title = '123'
assert m.title == '123'

m.title = '4891'
assert m.title == '123'


def wallet_pay(type_p, pay):
    print (type_p, ' ', pay)


dicton = {
    'WALLET': lambda x, y: wallet_pay(x, y)
}

dicton['WALLET']('wallet', True)