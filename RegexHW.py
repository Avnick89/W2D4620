#Assighnment/Regex

import re

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]

def validate_names(names):
    pattern = re.compile(r"^[A-Z]")
    for names in names:
        if re.match (pattern, names):
            print(names)
        else:
            print("Invalid Name")

validate_names(names)