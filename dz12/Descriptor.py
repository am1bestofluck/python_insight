from string import digits


class TitleCaseASKII:

    def __init__(self, ban: str):
        self.ban = set(ban)

    def __set_name__(self, owner, name):
        self.param_name = "_"+name
        return self.param_name

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def validate(self, value: str):
        if not value.istitle():
            raise ValueError("Title case expected")
        for char in value:
            if char in self.ban:
                raise ValueError("no digits")
