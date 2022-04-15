roman = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
roman_other = {"CM": 900, "CD": 400, "XL": 40, "IX": 9, "IV": 4}
roman_invalid = {"LL", "VV", "DD", "LM", "VM", "DM", "LD", "VD", "LC", "VC"}
total_value = 0
last_numberal = ""
entry = input("Please enter a Roman Numeral to be evaluated:  ")
entry = entry.upper()
index = 0
entry_list = list(entry)
first_value = entry_list[0]
in_a_row = 0
for numeral in entry_list:
    # print("Numeral is:  ",numeral)
    if numeral == first_value:
        in_a_row = in_a_row + 1
        last_numeral = numeral
        # print(last_numeral)
        # print("In a row is:  ",in_a_row)
        if in_a_row > 3:
            print("The Roman number you entered is not a valid Roman numeral.")
            import sys

            sys.exit()
    else:
        if i == last_numeral:
            in_a_row = in_a_row + 1
            # print("In a row is:  ",in_a_row)
            last_numeral = i
            # print(last_numeral)
            if in_a_row > 3:
                print("The Roman number you entered is not a valid Roman numeral.")
                import sys

                sys.exit()
        else:
            in_a_row = 1
            last_numeral = i
            # print(last_numeral)

# print(entry_list)
for letter in entry_list:
    if index < 1:
        value = roman[letter]
        total_value = total_value + value
        # print("Total value is index0:  ",total_value)
        last_letter = letter
        # print("Last Value wasindex0:  ",last_value)
        index = index + 1
    else:
        value = roman[letter]
        # print(letter)
        number_check = last_letter + letter
        # print("Number Check is: ",number_check)
        if number_check in roman_invalid:
            # print("Number Check is: ",number_check)
            print("The Roman number you entered is not a valid Roman numeral.")
            import sys

            sys.exit()
        if number_check in roman_other:
            # print("Number check is in roman_other")
            last_value = roman[last_letter]
            # print("Roman other last value is:  ",last_value)
            # print("total_value is:  ",total_value)
            total_value = total_value - last_value
            # print("total_value is after subtracting last letter:  ",total_value)
            total_value = total_value + roman_other[number_check]
            # print("total_value is:  ",total_value)
            last_letter = letter
            index = index + 1
        else:
            value = roman[letter]
            total_value = total_value + value
            # print("Total value is else:  ",total_value)
            last_letter = letter
            # print("Last Value was else:  ",last_letter)
            index = index + 1
print(
    "The Roman number you entered, ",
    entry,
    " equals ",
    total_value,
    " in Arabic numbers.",
)
