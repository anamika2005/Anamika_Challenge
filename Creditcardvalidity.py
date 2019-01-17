
#Uisng regular expressions
import re

 #"""Check if a sequence is a valid credit card number.

#    Sequences must:

 #   -Contain exactly 16 digits;
  #  -Start with a 4,5 or 6;
   # -Only consist of digits (0-9).

#    Sequences may:
#    -Have digits in groups of 4, separated by one hyphen.

 #   Sequence must not:
  #  -Use any other separator;
   # -Have 4 or more consecutive repeated digits.
    #"""
n = int(input())
for i in range(n):
    card = input()
    #checking for length== 19, then check for seperator 
    if len(card) == 19:
        if card[0] in ("4","5","6"):
            if bool(re.match("[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$",card)):
                lst = []
                for z in range(len(card)):
                    if card[z] != "-":
                        lst.append(card[z]) 
                        #appending list without separator
                bool_4 = 1
                #eliminating consecutive numbers case
                for i in range(3,len(lst)):
                    if lst[i] == lst[i-1] and lst[i] == lst[i-2] and lst[i] == lst[i-3]:
                        bool_4 = 0
                if bool_4 == 1:
                    print("Valid")
                else:
                    print("Invalid")
            else:
                print("Invalid")
        else:
            print("Invalid")
        #checking for length == 16, then check without seperator
    elif len(card) == 16:
        if card[0] in ("4","5","6"):
            if bool(re.match("[0-9]*$",card)):
                lst = []
                for k in range(len(lst)):
                    lst.append(card[k])
                bool_4 = 1
                for i in range(3,len(lst)):
                    if lst[i] == lst[i-1] and lst[i] == lst[i-2] and lst[i] == lst[i-3]:
                        bool_4 = 0
                if bool_4 == 1:
                    print("Valid")
                else:
                    print("Invalid")
            else:
                print("Invalid")
        else:
            print("Invalid")
                    
                
    # lengths other than 19 and 16 are invalid.            
    else: 
        print("Invalid")