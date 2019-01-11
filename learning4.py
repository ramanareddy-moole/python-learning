# if-else

# calculate the wage according hours worked

# the normal hours 40
# pay_rate hourly 100 dollars
# overtime
# 40 * 100 = 4000 dollars
# 50-40=10 hours --> 10 * 100 * 1.5 = overtime hours pay
# 40 * 100 = 4000

BASE_HOURS = 40
pay_rate = 100
OT_MULTIPLIER = 1.5

hours = int(input("enter the hours worked :"))
OT_MULTIPLIER = float(input("enter OT multiplier :"))

if hours > BASE_HOURS:
    overtime_hours = hours - BASE_HOURS
    overtime_pay = BASE_HOURS * pay_rate + (overtime_hours * pay_rate * OT_MULTIPLIER)
    print("Overtime Pay is:" + str(overtime_pay))
else:
    normal_pay = BASE_HOURS * pay_rate
    print("Normal Pay is :" + str(normal_pay))
