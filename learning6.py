# while loop

#while expression:
    #statement1
    #statement2
    #statement3

#prorated wage base
proceed = 'y'
BASE_HOURS = 40

while proceed == 'y':
    hours = int(input("enter the number of hours"))
    pay_rate = float(input("enter the pay rate"))
    OT_MULTIPLIER = 1.5
    if hours > BASE_HOURS:
        overtime_hours = hours - BASE_HOURS
        overtime_pay = BASE_HOURS * pay_rate + (overtime_hours * pay_rate * OT_MULTIPLIER)
        print("Overtime Pay is:" + str(overtime_pay))
    else:
        normal_pay = BASE_HOURS * pay_rate
        print("Normal Pay is :" + str(normal_pay))
    #proceed = input("do you want to calculate for another pay? please press y to proceed otherwise n")
else:
    pass