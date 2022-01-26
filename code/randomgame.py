import sys
import random

try:
    start=int(sys.argv[1])
    end=int(sys.argv[2])
except ValueError:
    print("bad options was given, retry with good ones")
else:
    answer = random.randint(start, end)
    while True:
        try:
            user_num = int(input(f"guess a number between {start}-{end}: "))
        except ValueError:
            print("give a number, i say a fucking number")
            continue
        else:
            if start <= user_num <= end:
                if user_num != answer:
                    print("you're near")
                else:
                    print("wohoo success :)")
                    break
            else:
                print("don't give a number out of the range")