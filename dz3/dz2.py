"""
В большой текстовой строке подсчитать количество встречаемых слов
 и вернуть 10 самых частых.
 Не учитывать знаки препинания и регистр символов.
 За основу возьмите любую статью из википедии или из документации к языку.

 https://proxyway.com/knowledge-base/how-to-extract-text-from-a-table-using-beautifulsoup
"""
import re
from os import unlink
from pathlib import Path
from re import sub
import sys

from bs4 import BeautifulSoup
import requests

SOURCE = "https://docs.python.org/3/library/stdtypes.html"
LOCAL = Path("./built-in-types.html")
MATCHES_OUTSOURCE = 1472


def getpage() -> None:
    """
    качает страничку SOURCE
    :return:
    """
    global SOURCE, LOCAL
    if not LOCAL.exists():
        try:
            page = requests.get(SOURCE)
            with open(LOCAL, 'w', encoding='UTF-8') as dump:
                dump.write(page.text)
        except:
            unlink(LOCAL)
            sys.exit("Жаааль :). У меня работало.")


def get_text() -> str:
    global LOCAL
    out = ""
    with open(LOCAL, 'r', encoding="UTF-8") as content:
        soup = BeautifulSoup(open(LOCAL, 'r', encoding="UTF-8"), "html.parser")
        return sub(re.compile("[^\w\s]+"), '', soup.get_text()).lower()


def get_repetitions(text_edited: str):
    list_ = text_edited.split()
    temp = dict()
    for i in list_:
        temp[i] = temp.get(i, 0)+1
    temp = [(i[0], i[1]) for i in temp.items()]
    temp.sort(key=lambda x: x[1], reverse=True)
    return temp[:10]


def main():
    global MATCHES_OUTSOURCE
    getpage()
    tmp = get_repetitions(get_text())
    print(tmp)
    print(f"Мы поймали {tmp[0][1]} совпадений {tmp[0][0]!r}. Ctrl-F из браузера даёт {MATCHES_OUTSOURCE}."
          "Совпадение, к сож, не стопроцентное но Мы близки :)." if tmp[0][1] != MATCHES_OUTSOURCE else "ура?")


if __name__ == '__main__':
    main()
