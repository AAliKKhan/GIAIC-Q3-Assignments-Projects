import math

def main():
   sideAB:float=float(input("enter length of side A to B : "))
   sideAC:float=float(input("enter length of side A to C : "))
   
   sideBC:float= math.sqrt(sideAB**2 + sideAC)

   print("The length of BC (the hypotenuse) is: " + str(sideBC))
if __name__ == '__main__':
    main()