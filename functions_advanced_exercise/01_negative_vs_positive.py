def print_numbers(positives, negatives):
    print(negatives)
    print(positives)

    if positives > abs(negatives):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(x) for x in input().split()]
positive_numbers = sum(x for x in numbers if x > 0)
negative_numbers = sum(x for x in numbers if x < 0)

print_numbers(positive_numbers, negative_numbers)
