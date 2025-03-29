def average(a: float, b:float):
    avg=a=b/2

    return avg

def main():
   avg1=float(input("enter first number: "))
   avg2=float(input("enter second number: "))

   final = average(avg1,avg2)
   print( "Average is",final)
if __name__ == '__main__':
    main()   