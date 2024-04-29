import re



def verify_names(names):
    pattern = re.compile(r'^[A-Z][a-z]+(?:\s[A-Z][a-z]+)*$')
    for name in names:
        if pattern.match(name):
            print(name)
        else:
            print("invalid name")

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", 
         "Jordan Alexander Williams", "Madonna", "programming is cool"]

verify_names(names)