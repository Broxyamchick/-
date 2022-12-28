try:
    result = []
    def divider(a, b):
        if a < b:
            raise ValueError
        if b > 100:
            raise IndexError
        return a/b

    data = {10, 2, 5, 4, 18, 0, 15, 8}

    for key in data:
        res = divider(key, data[key])
        result.append(res)
    print(result)
except TypeError:
    print("Объект 'set' не подлежит подписке")
except ValueError:
    print("a < b")
except IndexError:
    print("b > 100")