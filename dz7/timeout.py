from os import chdir as cd
from sem7 import timeout_1 as nonsense_files, timeout_2 as sorting
from pathlib import Path

# можно было чище конечно, но там весь семинар переписывать
if __name__ == '__main__':
    root = Path.cwd()
    folder = "timeout"
    nonsense_files.main()
    cd(root)
    sorting.main(Path(sorting.fld1) / sorting.fld2)
