# coding:utf-8
# collatz序列，输入验证

import sys

def collatz(number):
    print (number)
    if number == 1:
        sys.exit()
    elif number%2 == 0:
        number = number//2
        collatz(number)
    else:
        number = 3*number+1
        collatz(number)

def main():
    try:
        num = int(input("Enter number: "))
        return collatz(num)
    except ValueError:
        print ("Please enter a integer.")

if __name__ == '__main__':
    while True:
        if (main() == 1):
            break