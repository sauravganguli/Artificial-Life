# Based on examples from here: 
# https://runestone.academy/runestone/books/published/thinkcspy/Strings/TurtlesandStringsandLSystems.html

import time
import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format


# Define the rules
# Apply relevant rule to the axiom and generate the nre string
def applyRules(src_str): 
    dest_str = ""
    if src_str == 'C':
        dest_str = 'A'   # Rule 1 [C->A]: child grows up
    elif src_str == 'A':
        dest_str = 'CA'  # Rule 2 [A->CA]: offspring
    else:
        dest_str = src_str    # no rules apply so keep the character
    return dest_str

# Select individual characters from the initial string and pass it as an axiom to applyRules() 
# to generate the new string by applying the relevant rules 
def processString(old_str): 
    new_str = ""
    for char in old_str:
        new_str = new_str + applyRules(char) #applyRules() is applied individually to each character
    return new_str


def createLSystem(iterations, axiom):
    init_str = axiom
    final_str = ""
    print("This is a simple Lindenmayer System for Child(C) and Adult(A) growth")
    
    # Display the rules

    cprint(figlet_format('RULES :', font='starwars'))
    cprint(figlet_format('Rule 1 : C -> A', font='standard'), attrs=['bold'])
    cprint(figlet_format('Rule 2 : A -> C A', font='standard'), attrs=['bold'])
    print("\n")
    time.sleep(2)

    # Apply D0L system for the specified number of iterations
    for i in range(iterations):
        text = "Step "+str(i)+" : "+init_str
        cprint(figlet_format(text, font='digital'))
        time.sleep(1)
        final_str = processString(init_str) # Pass the initial string at every step to processString()
        init_str = final_str
    return final_str

createLSystem(8, "C") # Define the number of iterations and the starting axiom