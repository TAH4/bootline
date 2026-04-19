import sys
import time
import random
import os

class Typewriter:
    def __init__(self, USE_RAND_COLORS: bool = True):
        self.USE_RAND_COLORS = USE_RAND_COLORS

        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.ART_DIR  = os.path.join(self.BASE_DIR , 'art/')    

        self.RAND_COLORS = [
            "\033[31m",  # red
            "\033[32m",  # green
            "\033[33m",  # yellow
            "\033[34m",  # blue
            "\033[35m",  # magenta
            "\033[36m",  # cyan
            "\033[37m",  # white
        ]

        self.RESET_COLOR = "\033[0m"

    def tprint(self, DELAY: int = random.uniform(0.001, 0.003)) -> None:
        print("\033[2J\033[H")

        try:
            with open(f"{self.ART_DIR}/art.txt", "r") as file:
                printable = file.read()
        except FileNotFoundError:
            printable = "[NO BANNER FOUND]"

        for char in printable:
            if self.USE_RAND_COLORS:
                color = random.choice(self.RAND_COLORS)
                sys.stdout.write(f"{color}{char}{self.RESET_COLOR}")
            else:
                sys.stdout.write(char)

            sys.stdout.flush()
            time.sleep(DELAY)

        print()
