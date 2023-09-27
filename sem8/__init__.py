try:
    from t_2 import input_loop
    from t_3 import main as base_to_json
    from t_5 import walk_dir as jsons_to_pickle
    from t_6 import pickle_to_csv
    from t_7 import csv_as_pickle
except ImportError:
    from .t_2 import input_loop
    from .t_3 import main as base_to_json
    from .t_5 import walk_dir as jsons_to_pickle
    from .t_6 import pickle_to_csv
    from .t_7 import csv_as_pickle
__all__ = ['input_loop', 'base_to_json', 'jsons_to_pickle', 'pickle_to_csv', 'csv_as_pickle']
