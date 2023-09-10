"""
Выведите в консоль таблицу умножения
от 2х2 до 9х10 как на школьной тетрадке.
✔ Таблицу создайте в виде однострочного
генератора, где каждый элемент генератора —
отдельный пример таблицы умножения.
✔ Для вывода результата используйте «принт»
без перехода на новую строку
"""
print("спустя 5 часов могу сказать что пытаться переделать незакоментированное",
      " решение в один генератор Я заеустал.")
print(*(f"{base}*{mult}={base * mult:<5}{chr(10) if base in [5, 9] else chr(9)}"
        for mult in range(2, 11) for base in range(2, 6)),
      *(f"{base}*{mult}={base * mult:<5}{chr(10) if base in [5, 9] else chr(9)}"
        for mult in range(2, 11) for base in range(6, 10)), sep="")  # собственно говоря, кто сказал что
# однострочник должен быть в одну строку?

# print(*(f"{base}*{mult}={base * mult:<5}{chr(10) if base in [5, 9] else chr(9)}"
#         for mult in range(2, 11) for base in range(2, 6)),
#       *(f"{base}*{mult}={base * mult:<5}{chr(10) if base in [5, 9] else chr(9)}"
#         for mult in range(2, 11) for base in range(6, 10)), sep="")

# print(*(((f"{base}*{mult}={base * mult:<5}{chr(10) if base in [5, 9] else chr(9)}"
#         for mult in range(2, 11) for base in rng)) for rng in [range(2,6),range(6,10)]),
#
#
#
#  sep="")
# print(f"{i}*{j}={i*j}" for i in k for j in range(1,11) for k in [range(2,6),range(6,10)])

# print(sep="",
      # *(f"{mult}*{base}={base*mult}{chr(10) if base in [5,9] else chr(9)}" for mult in range(2,10) for base  in range(2,11)))