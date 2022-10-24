import timeit
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

if __name__ == "__main__":
    print(timeit.timeit("from main import run;run()", number=1, globals=locals()))
