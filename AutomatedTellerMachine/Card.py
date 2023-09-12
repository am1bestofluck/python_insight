class Card:
    """
    Это токен который мы кормим банкомату чтобы начать работать.
    В себе содержит номер карты и собственно всё.
    Поддерживаемые номера:
        с   1234_0000_0000_0000
        по  1234_0000_0001_0000
    """

    def __init__(self, number: int):
        self.__number = number

    def get(self):
        return self.__number
    def get_pin(self):
        return f"Покрутив карту в руках мы заметили нацарапанные цифры {str(self.__number)[-5:]}"

if __name__ == '__main__':
    card = Card(1234_0000_0001_0000)
    print(card.get(),card.get_pin())
