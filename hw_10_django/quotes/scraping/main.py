from .parser import main as parser_main
from .seed import main as seed_main
from ..scraping import models


def parser():
    try:
        parser_main()
    except Exception as e:
        print(e)

    try:
        models
    except Exception as e:
        print(e)

    try:
        seed_main()
    except Exception as e:
        print(e)
