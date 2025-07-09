

def enforce_types(func):
  def A(*args, **kwargs):
      r1=func.__annotations__
      r2=func.__code__.co_varnames
      for i,j in enumerate(args):
          g=r2[i]
          expected_type = r1.get(g)
          if expected_type and not isinstance(j, expected_type):
              raise TypeError(
                    f"Argument '{g}' Должен быть типа {expected_type.__name__} "
                    f"Но это было принято {type(j).__name__}"
                )
           


      for l,val in kwargs.items():
          expected_type = r1.get(l)

          if expected_type and not isinstance(val, expected_type):
            
            raise TypeError(
                f"Argument '{l}' Должен быть типа {expected_type.__name__} "
                f"Но это было принято {type(val).__name__}"
            )
      return func(*args, **kwargs)
  return A



@enforce_types
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError
