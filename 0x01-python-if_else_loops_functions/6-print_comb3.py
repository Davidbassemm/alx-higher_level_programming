#!/usr/bin/python3
for digit1 in range(10):
    for digit2 in range(digit1, 10):
        if digit1 < digit2:
            print("{:d}{:d}".format(i, j),
                  end="\n" if digit1 == 8 and digit2 == 9 else ", ")
