import utils as u
from config import ROOT_DIR
import os.path

DATA_DIR = os.path.join(ROOT_DIR, "data", "operations.json")


def main():
    list_all = u.create_list_all_operations(DATA_DIR)
    list_necessary = u.create_necessary_operations(list_all)

    for operation in list_necessary:
        print(u.get_formatted_operation(operation))


if __name__ == '__main__':
    main()
