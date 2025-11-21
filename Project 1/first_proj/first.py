import os
import sys
import math
import random

class FirstProj:
    def __init__(self):
        pass

    def greet(self,msgage=None):
        if msgage == None:
            print("Hello from FirstProj!")
        else:
            print(f"Hello from FirstProj! Message: {msgage}")

    def shout(self, message):
        print(message.upper())

if __name__ == "__main__":
    proj = FirstProj()
    proj.greet()
    msg = "Get the hell out of here"
    proj.shout(msg)
    print("Enter your message1:")
    user_input1 = input()
    print("Enter your message2:")
    user_input2 = input()
    if user_input1.strip() != msg or user_input2.strip() != msg:
        proj.shout(msg)
    blink = FirstProj()
    blink.greet()
    blink.greet("Awesome!, i did something called as overriding")