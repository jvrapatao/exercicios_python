def new_user(active=False, admin=False):
    print(active)
    print(admin)


config = {'active': False,
          'admin': True}

new_user(**config)


def unpaching(*args):
    arg1 = args[0]
    arg2 = args[1]
    outros = args[2:]
    print(arg1)
    print(arg2)
    print(outros)


unpaching(1, 2, 3, 4, 5, 6)


def unpacking_kwargs(**kwargs):
    print(kwargs)


unpacking_kwargs(id=1, nome='Teste')
