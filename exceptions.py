try:
  age=input("How old are you?")
  print("In 2032 you will be", int(age) +10)
  print(100/int(age))
except ValueError:
  print("Hey, that is not a number")
except ZeroDivisionError:
    print("can not divide by zero")
except:
    print("this is a new error that I did not see")
finally:
    print("This is what we do after all is done")
