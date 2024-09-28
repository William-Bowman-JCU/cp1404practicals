from score import determine_score_status;

MENU = """
(G)et valid score
(P)rint result
(S)how starts
(Q)uit
>>> """

def main():
    """Display menu and handle user choices for score input"""
    score = get_valid_score('Score: ')
    choice = input(MENU).lower()
    while choice != 'q':
        if choice == 'g':
            score = get_valid_score('Score: ')
        elif choice == 'p':
            (print(determine_score_status(score)))
        elif choice == 's':
            print('*' * score)
        choice = input(MENU).lower()
    print('Farewell')

def get_valid_score(prompt):
    """Prompt user for a valid score between 0 and 100"""
    score = int(input(prompt))
    while score < 0 or score > 100:
        print('Invalid score')
        score = int(input(prompt))
    return score

main()
