import os 
import sys

def resource_path(relative_path):
    """
    возвращает правильный путь для файлов
    """
    if getattr(sys,"frozen",False):
        base_path=sys._MEIPASS
    else:
        base_path=os.path.abspath(os.path.dirname(__file__))
        print(base_path)
        print(relative_path)

    return os.path.join(base_path,relative_path)  