import sys, time

def timer_func(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'Function {func.__name__!r} executed in {1000*(t2-t1):.4f}ms')
        return result
    return wrap_func

# @timer_func
def main():
  with open(sys.argv[1], 'r') as infile:
    puzzle_input_list = infile.readlines()
    
  for i, istr in enumerate(puzzle_input_list):
    for j, jstr in enumerate(puzzle_input_list):
      for k, kstr in enumerate(puzzle_input_list):
        if i != j != k and int(istr) + int(jstr) + int(kstr) == 2020:
          print(int(istr) * int(jstr) * int(kstr))
          return
        
main()