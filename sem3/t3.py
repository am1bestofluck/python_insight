"""
Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды.
"""

def main():
    a = [1,2,3]*2
    a.extend([None]*10)
    print(a)
    # for i in a:
    #     print(i)
    #     if a.count(i) == 2:
    #         a.remove(i)
    #         a.remove(i)
    i = 0
    while i != len(a)-1:
        if a.count(a[i])==2:
            item = a[i]
            a.remove(item)
            a.remove(item)
            i = 0
        else:
            i +=1
    print(a)
if __name__ == '__main__':
    main()