def decorator_str(func):
    def decorator_inside(value):
        data = func(value)
        if data == str(data):
            result = '<b>' + data + '</b>'
            return result
        else:
            return data

    return decorator_inside


@decorator_str
def checking(value):
    return value


print(checking('fsdf'))
