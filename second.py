#!/usr/bin/python3.6
import re, datetime


class AbonentFormatException(Exception):
    pass


def compose_abonent(number, balance):
    """
    Composes abonent

    :param str number: Number of abonent
    :param str balance: Balance
    :return: Composed dictionary of abonent
    :rtype: dict
    """
    abonent = {}
    if not number or not re.match("^[+|\d]\d+$", number):
        raise AbonentFormatException("Number has to have only + and digit numbers")
    if not balance or not re.match("^\d+[\.|\d]*\d*$", balance):
        raise AbonentFormatException("Balance must be float or int")
    abonent['number'] = number
    abonent['balance'] = float(balance)
    return abonent

def create_abonent_flow():
    """
    Creates initial abonent

    :return: If abonent create - dict. Otherwise - None
    :rtype: dict|None
    """
    while True:
        inputted_data = input("Input through space next fields: number and current balance")
        if not inputted_data or len(inputted_data) == 0:
            print("Inputted data are empty. Try again!")
            continue
        ls = inputted_data.strip().split(" ")
        if len(ls) != 2:
            print("Amount of fields should match with initial data above. Try again!")
            continue
        try:
            return compose_abonent(number=ls[0].strip(), balance=ls[1].strip())
        except AbonentFormatException as e:
            print("Error ", e.args[0])
            continue

def show_info(abonent):
    print("You can use next commands: \n"
          "     'q' - quit\n"
          "     'in' - make incoming call.\n"
          "     'out' - make outcoming call. Tariff is 1 pseudo balance for 1 minute \n"
          "     'add' - replenish account\n"
          "     'show' - show info about abonent\n"
          "     Abonent info %s \n" % abonent)

def handle_outcoming(abonent, duration):
    if abonent['balance'] < duration:
        print("You haven't enough money to originate call")
        return
    abonent['outcoming'] = abonent.get('outcoming', 0) + duration
    abonent['balance'] -= duration

def handle_incoming(abonent, duration):
    abonent['incoming'] = abonent.get('incoming', 0) + duration

def handle_replishment_balance(abonent, money):
    if money <= 0:
        print("Value is not less than 0")
        return
    abonent['balance'] += money
    abonent['last_payment'] = str(datetime.datetime.now())


print("Hi, this program leads calculation for ATC abonent")
abonent = create_abonent_flow()
if not abonent:
    pass
else:
    show_info(abonent)
    while True:
        try:
            command = input("Your command is ")
            if command == 'q':
                print("Good luck")
                break
            elif command == 'out':
                duration = int(input("Input duration of call: "))
                handle_outcoming(abonent, duration)
            elif command == 'in':
                duration = int(input("Input duration of call: "))
                handle_incoming(abonent, duration)
            elif command == 'add':
                money = float(input("How many money do you want to spend? "))
                handle_replishment_balance(abonent, money)
            elif command == 'show':
                show_info(abonent)
        except ValueError as e:
            print("Error. Format of inputted data not valid. Try again!")