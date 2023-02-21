hours = int(input("enter weekly hours"))

payment_regular = 20
payment_overtime = 30
regular_weekly_hours = 40

if hours <= regular_weekly_hours:
    payment = payment_regular*regular_weekly_hours
else:
    payment = payment_regular*regular_weekly_hours + payment_overtime*(hours-regular_weekly_hours)

print(f"your payment is {payment} $")