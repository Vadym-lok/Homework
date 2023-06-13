def decorator_str(func):
    def result_string(*args, **kwargs):
        data = func(*args, **kwargs)
        if data == str(data):
            result = '<b>' + data + '</b>'
            return result
        else:
            return data

    return result_string


@decorator_str
def checking(value):
    return value


print(checking('fsdf'))
