import cProfile
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

if __name__ == "__main__":
    cProfile.run('from main import run;run()')
