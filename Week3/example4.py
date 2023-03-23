

y = 30

def my_function():
  x = 10  # x has local scope
  print("Inside the function, x = " + str(x))
  print("Inside the function, y = " + str(y))




if __name__ == '__main__':
  my_function()
  print("Outside the function, y = ", y)  # This will not raise an error
  print("Outside the function, x = ", x)  # This will raise an error
