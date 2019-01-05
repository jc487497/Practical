def main():
    """Display income report for incomes over a given number of MONTHS."""
    incomes = []
    MONTHS = int(input("How many MONTHS? "))

    for month in range(1, MONTHS + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    get_report(incomes, MONTHS)


def get_report(incomes, months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
