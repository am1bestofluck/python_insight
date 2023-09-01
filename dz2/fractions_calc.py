import re


class FractionsCalc:

    __ops: [str, re.Pattern] = {
        "add": re.compile("\d*/\d*\+\d*/\d*"),
        "mult": re.compile("\d*/\d*\*\d*/\d*"),
        "div": re.compile("\d*/\d*/\d*/\d*"),
        "sub": re.compile("\d*/\d*-\d*/\d*")
    }

    def __init__(self, equation: str = None):
        self.equation_i = self.__check_string(equation)

    def __check_string(self, equation: str):
        return "error" if not isinstance(equation, str) or len(equation) > 200 else equation

    def get_next(self, equation: str):
        """следующая строка"""
        self.equation_i = self.__check_string(equation)

    def eval(self) -> str:
        """определяем кто есть кто"""
        buffer = None
        for i in FractionsCalc.__ops:
            if re.match(FractionsCalc.__ops[i], self.equation_i):
                buffer = i
                break
        if not buffer:
            return self.equation_i  # вернёт error если на входе чушь

        if buffer == "div": # отдельный случай!
            temp = self.equation_i.split('/')
            first,second = (temp[0],temp[1]),(temp[2],temp[3])
        else:
            temp = re.split("[\+,\*]",buffer)
            first,second = (temp[0].split('/')[0],temp[0].split('/')[1]),\
                (temp[1].split('/')[0],temp[1].split('/')[1])
        return self.__calc([first,second,buffer])
    def __calc(self,args:list) -> str:

        out = ""
        assertion_args = [None,None]
        match args[3]:
            case "add":
                pass
            case "mult":
                pass
            case "div":
                pass
            case "sub":
                pass

        assert True
        return out
