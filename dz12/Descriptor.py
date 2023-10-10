from string import digits


class TitleCaseASKII:
    ban = set(digits)

    def __init__(self, value: str):
        self.value = value

    # def __get__(self,instance,owner):
    #     return getattr(instance,)
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance,None,None)

    def validate(self, value: str):
        if set(value).intersection(set(self.ban)) is not None:
            raise ValueError("no digits expected")
        if not value.istitle():
            raise ValueError("Title case expected")
