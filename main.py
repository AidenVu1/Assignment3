def size():
  print("[1] large pizza (cheaper than little caesars) $6.00")
  print("[2] extra large pizza (liam's favourite) $10.00")
  print("[0] cancel order")

def topping():
  print("[1] 1 topping $1.00")
  print("[2] 2 toppings $1.75")
  print("[3] 3 toppings (recommended) $2.50")
  print("[4] 4 toppings $3.25")
  print("[0] cancel order")

def another():
  print("[1] proceed")
  print("[2] order another one")
  print("[0] cancel order")
def order(m,m1):
  op1=9
  while op1!=0:
    try:
      size()
      op1=int(input("what size do you want?\n"))
      
    except ValueError:
      print("please enter a number between 0-2")
      continue
    
    else:
      if op1 ==1:
        m=m+6.00
        break
      elif op1 ==2:
        m=m+10.00
        break
      elif op1 ==0:
        print("order cancelled")
        break
      else:
        print("please enter a number between 0-2")
      continue

  while op1!=0:
    try:
      topping()
      op2=int(input("how many toppings do you want, cheese included\n"))

    except ValueError:
      print("please enter a number between 0-4")
      continue

    else:
      if op2 == 1:
        m1=m1+1.00
        break
      elif op2 ==2:
        m1=m1+1.75
        break
      elif op2 ==3:
        m1=m1+2.50
        break
      elif op2 ==4:
        m1=m1+3.25
        break
      elif op2 ==0:
        print("order cancelled")
        op1=0
        break
      else:
        print("please enter a number between 0-4")
        continue
        
  while op1 !=0:
    try:
      another()
      op3=int(input("Is that all?\n"))
    except ValueError:
      print("please enter a number between 0-2")
    else:
      if op3==1:
        break
      elif op3==2:
        order(m,m1)
      elif op3==0:
        print("order cancelled")
        op1=0
        break
      else:
        print("please enter a number between 0-2")
        continue

  while op1!=0:
    total=round((m+m1)*1.13,2)
    print("the total cost of the pizza is $",total)
    print("have a nice day")
    exit()
order(0.00,0.00)
