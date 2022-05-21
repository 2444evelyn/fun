from tokenize import Number


def multiple_and_greet(*number,**student):
    Numbers=1
    for y in number:
        Numbers*=y
        print(Numbers)
    print(f"Hello{student}")
        
        