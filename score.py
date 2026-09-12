score = float(input("Enter your score"))
attendence = int(input("Enter your attendence"))

if score >= 75.0 and attendence >= 80:
   print("Passed with Distincion")
elif score >= 50.0 and attendence >= 75:
   print("Passed")
else:
   print("Ineligible due to attendence")
