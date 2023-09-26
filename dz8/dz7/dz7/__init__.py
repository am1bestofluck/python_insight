try:
    from timeout import sorting
    from t1 import main as custom_rename
    from timeout import nonsense_files
except ImportError:
    from .timeout import sorting
    from .t1 import main as custom_rename
    from .timeout import nonsense_files

make_spam_files = nonsense_files.main
type_sort = sorting.main

__all__ = ['type_sort', 'custom_rename', 'make_spam_files']


def __test():
    from pathlib import Path
    abstest = Path("test").absolute()
    make_spam_files(abstest)
    type_sort(abstest)
    custom_rename(folder_i=abstest, new_name="nn", new_ext="exe", target_ext="dll", number_size=6, saved_part=range(5))


if __name__ == '__main__':
    __test()
