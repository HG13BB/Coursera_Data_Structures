# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    opening_brackets_num   =[]
    error = 0
    
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            opening_brackets_num.append(i)

        elif next in ")]}":
            # Process closing bracket, write your code here
            if i == 0 or len(opening_brackets_stack) == 0: 
                error = i + 1
                break
            elif len(opening_brackets_stack)>0 and are_matching(opening_brackets_stack[-1], next) == False:
                error = i + 1
                break
            elif len(opening_brackets_stack)>0 and are_matching(opening_brackets_stack[-1], next):
                del opening_brackets_stack[-1]
                del opening_brackets_num[-1]
            
#    print(opening_brackets_stack[-1])
#    print(are_matching(text[0], text[1]))
#    print(text[4])
#    print(error)


    if len(opening_brackets_stack) == 0 and error == 0:
        print("Success")
    elif len(opening_brackets_stack) > 0 and error > 0:
        print(error)
    elif len(opening_brackets_stack) == 0 and error > 0:
        print(error)
    elif len(opening_brackets_stack) > 0:
        print(opening_brackets_num[-1]+1)



        

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
