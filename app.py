"""
Just a demo script to show off the learnfromanyone library
"""

import learnfromanyone

key = input("Openai Key (hit enter to skip and use GPT-J): ")

name = input("Enter name: ")
person = learnfromanyone.Person(name)

if key:
    person.openai_key = key

while True:
    print(person.respond(input("> ")))