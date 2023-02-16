# necessary to extract prefix-price info from csv file
import csv

def find_matches(dict_list, phone_number):
    """ Basically finds the matches prefixes and return the list of all matches"""

    prefix_matches = [] # empty list to store prefix match 

    for prefix in dict_list.keys(): # loop through the keys which are prefixes of Op-A or Op-B 
        if phone_number.startswith(prefix): # keep the prefix of any length if it matches 
            prefix_matches.append(prefix)
    return prefix_matches  # return whole list of matches


def main(phone):
    """
    1. Reading the csv files for prefix-price info
    2. Calling find_matches function to find prefix of any length
    3. Finding the longest match inside each operator
    4. Then print/return the cheapest result by comparing price
    """
    # read Op-A prefix-price info and save into a dict
    with open('operatorA.csv', mode='r') as file:
        reader = csv.reader(file)
        op_a_dict = {str(row[0]) : row[1] for row in reader}

    # read Op-B prefix-price info and save into a dict
    with open('operatorB.csv', mode='r') as file:
        reader = csv.reader(file)
        op_b_dict = {str(row[0]) : row[1] for row in reader}

    # find Op-A prefix matches
    temp_list_a = find_matches(op_a_dict, phone)
    if temp_list_a: # if there is a match
        longest_match = max(temp_list_a, key=len) # keep the longest match
        price_a = op_a_dict[longest_match]

    # find Op-B prefix matches
    temp_list_b = find_matches(op_b_dict, phone)
    if temp_list_b: # if there is a match
        longest_match = max(temp_list_b, key=len) # keep the longest match
        price_b = op_b_dict[longest_match]
    
    if temp_list_a and temp_list_b: # both operators have matches, compare the prices
        if price_a < price_b: # Op-A offers a cheaper price
            print(f"The cheapest operator is \"A\" with the corresponding price {price_a} for \"{phone}\"")
            return float(price_a)
        elif price_b < price_a: # Op-B offers a cheaper price
            print(f"The cheapest operator is \"B\" with the corresponding price {price_b} for \"{phone}\"")
            return float(price_b)
        else: #price are the same
            print(f"You can dial \"{phone}\" using both Operator \"A\" and \"B\" with the corresponding price {price_b}")
            return float(price_a)

    elif temp_list_a: # only Op-A offer a price
        print(f"\"A\" is the only operator with the corresponding price {price_a} for \"{phone}\"")
        return float(price_a)
    elif temp_list_b: # only Op-B offer a price
        print(f"\"B\" is the only operator with the corresponding price {price_b} for \"{phone}\"")
        return float(price_b)
    else: # There is no matching prefix
        print(f"You can't dial \"{phone}\" using both Operator \"A\" and \"B\"")
        return False


if __name__ == "__main__":
    """ Program can be run via command line. If so, script will be performed for 3 sample phone number."""

    print("Program's started...")

    sample_phone_numbers = ["12025550131","46737367456","66255884858"]  # sample (made-up) phone numbers
    
    for phone in sample_phone_numbers:
        main(phone)