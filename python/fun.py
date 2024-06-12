def hi():
    return "Hi, User!"


def min(a: int, b: int):
    if (a < b):
        return a
    else:
        return b


def get_from_list(data: list, index: int):
    return data[index]


def main():
    hi()
    print("Enter two numbers:")
    a = int(input("First: "))
    b = int(input("Second: "))
    print(f"Min of {a} and {b} = {min(a, b)}")
    try:
        list = [a, b]
        print(f"Take element of list from these nums {list} by index:")
        index = int(input("Index: "))
        print(f"Element: {list[index]}")
    except IndexError:
        print("Index out of range")
