import math
import json

def Basic_Calculations():
    Operator=input("Enter the operator (+, -, *, /, %, //, **): ")
    n1 = get_number("Enter the first number: ")
    n2 = get_number("Enter the second number: ")

    
    if Operator == "+":
       r=n1+n2
    elif Operator == "-":
       r=n1-n2
    elif Operator == "*":
         r=n1*n2
    elif Operator == "/":
      if n2==0  :
         print("Error! The number entered is zero ")
         return None
      else :
          r=n1/n2
    elif Operator == "%":
      if n2==0:
         print("Error! The number entered is zero ")
         return None 
      else:
       r=n1%n2
    elif Operator == "//":
       if n2==0:
          print("Error! The number entered is zero ")
          return None
       else:
          r=n1//n2
    elif Operator == "**":
       r=n1**n2
    else:
      print("Wrong! input")
      return None
    return {"operation": f"{n1} {Operator} {n2}", "answer": round(r, 4)}



def Math_Functions():
       
       f=input("Enter the function (round, abs, sqrt, ceil, floor, factorial): ").lower()
       n=get_number("Enter a number to perform mathematical functions : ")
       if f=="round":
          d = get_int("Enter the number of decimal places to round off to ")

          r2 = round(n,d)
       elif f=="abs":
          r2= abs(n)
       elif f=="sqrt":
          if n<0:
             print("Cannot calculate square root of negative number")
             return None
          else: 
           r2= math.sqrt(n)
       elif f == "ceil":
          r2= math.ceil(n)
       elif f =="floor":
          r2= math.floor(n)
       elif f == "factorial":
         if n < 0 or n != int(n):
           print("Factorial requires a non-negative whole number")
           return None
         else:
           r2 = math.factorial(int(n))
       else:
        print("Wrong ! Input")
        return None
       return {"operation": f"{f}({n})", "answer": round(r2, 4)}  



def Trigonometric_Functions():
       
       t = input("Enter the function (sin, cos, tan, sec , cosec, cot , all): ").lower()
       deg = get_number("Enter the value in degrees : ")

       d=math.radians(deg)
       if t =="sin":
          rt=round(math.sin(d),4)
       elif t =="cos":
          rt=round(math.cos(d),4)
       elif t =="tan":
         if abs(math.cos(d)) < 0.0000000001:   
           print("tan is undefined for this angle")
           return None
         else:
           rt = round(math.tan(d), 4)
       elif t =="sec":
         if abs(math.cos(d)) < 0.0000000001:      
            print("sec is undefined for this angle")
            return None
         else:
           rt = round(1 / math.cos(d), 4)
       elif t =="cosec": 
            if abs(math.sin(d)) < 0.0000000001:      
               print("cosec is undefined for this angle")
               return None
            else:
               rt = round(1 / math.sin(d), 4)
       elif t =="cot":
         if abs(math.sin(d)) < 0.0000000001:   
           print("cot is undefined for this angle")
           return None
         else:
           rt = round(1 / math.tan(d), 4)    
       elif t =="all":
           s = math.sin(d)
           c = math.cos(d)
           print(f"The value of {deg} degrees in all the Trigonometric Functions is : ")
           print(f"Sin   : {round(s, 4)}")         
           if abs(c) < 0.0000000001:                     
              print("Cos   : 0.0")                 
              print("Tan   : undefined")
              print("Sec   : undefined")          
           else:
               print(f"Cos   : {round(c, 4)}")
               print(f"Tan   : {round(s/c, 4)}")   
               print(f"Sec   : {round(1/c, 4)}")   
           if abs(s) < 0.0000000001:               
               print("Cosec : undefined")           
               print("Cot   : undefined")           
           else:
               print(f"Cosec : {round(1/s, 4)}")    
               print(f"Cot   : {round(c/s, 4)}")    
           return None 
       else:
         print("Wrong ! Input")
         return None 
       return {"operation": f"{t}({deg}°)", "answer": round(rt, 4)}
def load_history():
    try:
        with open("history.json", "r") as f:
            return json.load(f)          
    except FileNotFoundError:
        return []                        
def save_history():
    with open("history.json", "w") as f:
        json.dump(history, f, indent=2)  
def get_choice():
    while True:
        try:
            ch = int(input("Choose (0-5): "))   
            return ch
        except ValueError:
            print("Please enter a number (0-5).")
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")





history= load_history()
while True:
    print("\n<---- MENU ---->")
    print("1. Basic Calculations")
    print("2. Math Functions")
    print("3. Trigonometric Functions")
    print("4. Show History")
    print("5. Clear History")
    print("0. Exit")
    ch = get_choice()
    if ch == 0:
       print("GoodBye!")
       break
       
    elif ch == 1:
        record = Basic_Calculations()
        if record is not None:
           print(f"Result: {record['answer']}")
           history.append(record)
           save_history() 
    elif ch == 2:
        record =Math_Functions()
        if record is not None:
           print(f"Result: {record['answer']}")
           history.append(record)
           save_history() 

    elif ch == 3:
        record = Trigonometric_Functions()
        if record is not None:
            print(f"Result: {record['answer']}")
            history.append(record)
            save_history() 
    elif ch ==4:
       if len(history)==0:
          print("No Calculations YET!")
          print()
       else:
          print("<----History---->")
          for i, record in enumerate(history, start=1):
            print(f"{i}. {record['operation']} = {record['answer']}")
       continue 
    elif ch ==5:
       history.clear()
       save_history() 
       print(" History Cleared")
       print()
       continue
    else:
        print("Invalid Input!")
