def main():
    fixed_costs = float(input("Enter the fixed costs: "))
    price_per_unit = float(input("Enter the price per unit: "))
    variable_cost_per_unit = float(input("Enter the variable cost per unit: "))
    break_even_point = fixed_costs / (price_per_unit - variable_cost_per_unit)
    print(f"The break-even point is: {break_even_point:.2f} units")
main()
