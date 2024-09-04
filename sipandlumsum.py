try:
    class main1:
        def __init__(self,investment,timeperiod,expectedreturn):
            self.investment = investment
            self.timeperiod = timeperiod
            self.expectedreturn= expectedreturn
        def sip(self):
            x = self.investment
            y = self.timeperiod
            z = self.expectedreturn
            i = y/12/100
            print(f"i mounty intrest {i:4f}")
            maturity = x * (((1+i)**z-1)/i)* (1+ i)
            print(maturity)
    class main2:
        def __init__(self,pv,r,n):
            self.pv = pv
            self.r = r
            self.n = n
        def lumsum(self):
            a = self.pv
            b = self.r
            c = self.n
            intrest = b/100
            sub  = (1+intrest)**c
            further_value  = a*sub
            print(further_value) 
            
    choice  =input("enter the choice sip or lumsum:-")
    if choice == "sip":
        investment = int(input("enetr the amount you want invest in mountyly:-"))
        expectedreturn = float(input("enter the expected return ratio in pa:-"))
        timeperiod = int(input("number of mounts you have paid:-"))
        obj = main1(investment,timeperiod,expectedreturn)
        obj.sip()
    elif choice == "lumsum":
        pv = int(input("Present Value or initial investment amount:-"))
        r = float(input("Interest rate per period:-"))
        n = int(input("Number of periods the money is invested or borrowed for:-"))
        obj1 = main2(pv,r,n)
        obj1.lumsum()
    else:
        print("invalid choice")
except KeyError as k:
    print(f"error is {k}")
finally:
    print(f'{choice} had been calculated')















