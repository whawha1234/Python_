budget = float(input("Enter your budget"))
total_cost = int(input("Enter your total cost"))

if total_cost <= budget and total_cost > 0:
    print(total_cost-budget,"Purchase successful! Remaining budget:")
elif not total_cost <= budget:
    print(total_cost-budget,"Insufficient funds!You need: ")
