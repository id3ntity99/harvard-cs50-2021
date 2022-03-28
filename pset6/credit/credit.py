from cs50 import get_string

def print_result(obj):
    print(obj["comp"])

def check_valid(result, obj):
    if result % 10 == 0:
        obj["valid"] = True
    if obj["valid"] and obj["digits"][0] == "4":
        obj["comp"] = "VISA"
        obj["valid"] = "VALID"
    elif obj["valid"] and obj["digits"][:2] == "34" or obj["digits"][:2] == "37":
        obj["comp"] = "AMEX"
        obj["valid"] = "VALID"
    elif obj["valid"] and obj["digits"][0] == "5":
        obj["comp"] = "MASTERCARD"
        obj["valid"] = "VALID"
    else:
        obj["comp"] = "INVALID"

    print_result(obj)


def calculate_eles(temp, last, obj):
    second_to_last = []

    # Calculate the temporary array.
    for i in temp:
        if len(i) > 1:
            share = int(int(i) / pow(10, len(i) - 1))
            remainder = int(i) % pow(10, len(i) - 1)
            second_to_last.append(share)
            second_to_last.append(remainder)
        else:
            second_to_last.append(int(i))
    # Here is the result of Luhn's Algorithm.
    result = sum(second_to_last) + sum(last)

    check_valid(result, obj)


def reverse_search(number, obj):
    # Make card number to list.
    digits = list(number)
    temp = []
    last = []

    # Process each elements of the array reversely.
    for idx, digit in enumerate(digits[::-1]):
        # If index is second-to-last:
        if idx % 2 == 1:
            temp.append(str(int(digit) * 2))
        else:
            last.append(int(digit))

    calculate_eles(temp, last, obj)


def main():
    card_number = get_string("Number: ")

    # Make a new card dictionary.
    card = {
        "digits": card_number,
        "valid": False,
        "comp": ""
    }

    reverse_search(card_number, card)


main()

