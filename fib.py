from time import perf_counter
from functools import wraps


def memoize(funct):
  cache = {}
  
  @wraps(funct)
  def wrapper(*args,**kwargs):
    key = str(args) + str(kwargs)

    if key not in cache:
      cache[key] = funct(*args,**kwargs)

    return cache[key]

  return wrapper


@memoize
def fibonnaci(n:int)->int:
  if n<2:
    return n
  return fibonnaci(n-1) + fibonnaci(n-2)
    
start = perf_counter()
fibonnaci(40)
end = perf_counter()
print(f"Time difference {end-start} seconds")