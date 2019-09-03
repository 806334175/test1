num = 10


def demo1():
    a = 11
    b = 22
    return a, b


def demo2():
    a = 1
    b = 2

    [a, b] = [b, a]
    print(a)
    print(b)
    pass


def demo3(num_list):
    num_list.clear()
    num_list.append("123")
    num_list.append("456")
    pass


gl_list = [1, 2, 3]
demo3(gl_list)
print(gl_list)

str = "  a  b   c   "
print(str)
print(str.strip())
print(str.replace(" ",""))
