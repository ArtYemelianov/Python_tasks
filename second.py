#!/usr/bin/python3.6
import re

class AbonentFormatException(Exception):
    pass

def compose_abonent(*args):
    """
    Composes abonent

    :param str number: Number of abonent
    :param str bill: Active bill
    :param str incoming: Duration of incoming calls
    :param str outcoming: Duration of outcoming calls
    :param str last_cash: Last sum of cash that done
    :param str last_payment: Date of last payment
    :return: Composed dictionary of abonent
    :rtype: dict
    """
    abonent = {}
    if not args[0] or not re.match("^[+|\d]\d+$",args[0].strip()):
        raise AbonentFormatException("Number has to have only + and digit numbers")
    if not args[1] or not re.match("^\d+$",args[1].strip()):
        raise AbonentFormatException("Bill must be int")
    if not args[2] or not re.match("^\d+$",  args[2].strip()):
        raise AbonentFormatException("Incoming duration must be int")
    if not args[3] or not re.match("^\d+$",  args[3].strip()):
        raise AbonentFormatException("Outcoming duration must be int")
    if not args[4] or not re.match("^\d+$",  args[4].strip()):
        raise AbonentFormatException("Last cash must be int")
    if not args[5] or not re.match("^[\d|\.]+$",  args[5].strip()):
        raise AbonentFormatException("Last payment must be int")
    abonent['number'] = args[0]
    abonent['bill'] = int(args[1].strip())
    abonent['incoming'] = int(args[2].strip())
    abonent['outcoming'] = int(args[3].strip())
    abonent['last_cash'] = int(args[4].strip())
    abonent['last_payment'] = args[5].strip()
    return abonent

print("Hi, this program leads calculation for ATC abonent")

while True:
    inputted_data = input("Input through comma next fields: number, current balance, incoming duration, outcoming duration, last cash and last date payment:\n")
    if not inputted_data or len(inputted_data) == 0:
        print("Inputted data are empty. Try again!")
        continue
    ls = inputted_data.split(",")
    if len(ls) != 6:
        print("Amount of fields should match with initial data above. Try again!")
        continue
    try:
        abonent = compose_abonent(*ls)
        break
    except AbonentFormatException as e:
        print("Error ", e.args[0])
        continue

print("Your abonent is %s" % abonent)

