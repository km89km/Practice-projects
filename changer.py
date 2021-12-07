#! python3
# changer.py - A simple function that returns a dictionary of change.

"""Given a float value representing the change of a transaction in GBP, the
function will return a dictionary using the largest denominations and therefore
the fewest individual pieces."""


def changer(amount):
    # dictionary of each denomination in a till with its name and value.
    money = {'£20': 20, '£10': 10, '£5': 5, '£1': 1, '50p': .5, '20p': .2,
             '10p': .1, '5p': .05, '2p': .02, '1p': .01, }
    # initialised change dictionary that will be returned at the culmination.
    change = {}
    # Loop through the keys and values in the money dictionary.
    for key, value in money.items():
        # Use the largest available denomination.
        while amount >= value:
            # upon the first instance of a key in the money dictionary, the
            # setdefault() method will add the key of the denomination to the
            # change dictionary and set it's value to 0.
            change.setdefault(key, 0)
            # increment the value of the denomination
            # every time it is available.
            change[key] += 1
            # round the new change amount to 2 integers to avoid discrepancies.
            amount = round(amount - value, 2)
    return change
