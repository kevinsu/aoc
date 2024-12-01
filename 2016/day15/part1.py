import sys
from common.perf import profiler
from sympy.ntheory.modular import crt 
  
@profiler
def main(argv):  
  m = [13, 19, 3, 7, 5, 17, 11] 
  v = [11, 7, 1, 2, 2, 6, 4] 
    
  print(crt(m, v))


if __name__ == "__main__":
  main(sys.argv[1:])
