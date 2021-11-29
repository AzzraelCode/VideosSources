import os

root_path = os.path.dirname(os.path.abspath(__file__))

def get_path(*path):
    """
    Формирую абс путь
    :param path:
    :return:
    """
    return os.path.join(root_path, *path)