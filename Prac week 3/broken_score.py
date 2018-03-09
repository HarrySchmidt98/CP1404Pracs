"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    scores()

def scores():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif 90 > score:
        print("Passable")
    elif score < 50:
        print("Bad")

main()