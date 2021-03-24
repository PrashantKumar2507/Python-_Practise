n=eval(input("Enter the year :"))
while True:
                if n%4==0 and n%10!=0 or n%400==0:
                                print("Leap year ")
                                break
                else:
                                print("Not leap year")
                                break
                                
