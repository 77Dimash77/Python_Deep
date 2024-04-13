def create_argument_dict(**kwargs):
    argument_dict = {}
    for key, value in kwargs.items():
        if isinstance(key, (int, float, str, tuple, frozenset)):
            key = str(key)
        argument_dict[value] = key
    return argument_dict


arguments = create_argument_dict(a=1, b=2, c=3)
print(arguments)
