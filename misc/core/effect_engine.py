import time , os , random , sys 

class Effect:
    BASE_DIR = os.path.dirname( os.path.abspath(__file__))
    COLOR_ARRAY = [  
            "\033[31m",  # red
            "\033[32m",  # green
            "\033[33m",  # yellow
            "\033[34m",  # blue
            "\033[35m",  # magenta
            "\033[36m",  # cyan
            "\033[37m",  # white

            ]


    RESET_COLOR = "\033[0m"

    def typewriter(self , ART_FILE:str = "" , DELAY:float = random.uniform(0.001 , 0.002) , RANDOMIZE_COLORS:bool = True) -> None:
        try:
                if not ART_FILE:
                    ART_FILE = f"{self.BASE_DIR}/art/artfile.txt"

                with open(ART_FILE, 'r') as file:
                    content = file.read()

                for char in content:
                    if RANDOMIZE_COLORS:
                        sys.stdout.write(f"{random.choice(self.COLOR_ARRAY)}{char}{self.RESET_COLOR}")
                    else:
                        sys.stdout.write(char)

                    sys.stdout.flush()
                    time.sleep(DELAY)


        except FileNotFoundError:
            print("[No Banner Found]")
