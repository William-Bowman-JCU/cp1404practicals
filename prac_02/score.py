"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
    """Get user score & random score, and show their statuses"""
    score = float(input("Enter score: "))
    print(determine_score_status(score))
    random_score = random.randint(0, 100)
    print(f'Random score: {random_score}')
    print(determine_score_status(random_score))

def determine_score_status(score):
    """Determine users score status based off of their score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

# main()