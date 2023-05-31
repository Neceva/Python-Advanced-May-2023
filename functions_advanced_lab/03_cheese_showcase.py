def sorting_cheeses(**kwargs):
    result = ""

    sorted_cheeses = sorted(
        kwargs.items(),
        key=lambda kvp: (-len(kvp[1]), kvp[0])
    )
    for cheese_name, quantity in sorted_cheeses:
        result += cheese_name + "\n"
        reversed_quantities = sorted(quantity, reverse=True)
        for q in reversed_quantities:
            result += str(q) + "\n"
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
