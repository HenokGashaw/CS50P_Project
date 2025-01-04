from scales import teach_scale
import quiz

def get_user_name():
    """Prompts the user for their name and returns it."""
    name = input("Welcome to the Ethiopian Hymns Learning App! What's your name? ").strip()
    return name if name else "Learner"  # Default to 'Learner' if no input is given.

def display_introduction(name):
    """Displays the introduction to the app."""
    print(f"\nHello, {name}! 👋")
    print("This app is designed to teach you the 7 common scales of Ethiopian hymns.")
    print("You'll learn how each scale is constructed using notes [C D E F G A B],")
    print("understand the gaps between the notes, and test your knowledge with quizzes.")
    print("\nLet's get started!\n")

def introduce_scales(name):
    """Introduces Ethiopian scales and asks the learner to choose one."""
    scales = [
        "Selamta",
        "Tizita",
        "Tizita Minor",
        "Chernet",
        "Ambasel",
        "Bati",
        "Bati Minor"
    ]

    print(f"So {name}, Ethiopian music is deeply rooted in its cultural heritage, and the scales used")
    print("reflect this rich tradition. Here are the 7 common scales of Ethiopian hymns:")
    for i, scale in enumerate(scales, start=1):
        print(f"{i}. {scale}")

    # Prompt the learner to choose a scale
    while True:
        try:
            choice = int(input("\nWhich scale would you like to learn about? (Enter the number): "))
            if 1 <= choice <= len(scales):
                selected_scale = scales[choice - 1]
                print(f"\nGreat choice! You selected: {selected_scale}.")
                return selected_scale
            else:
                print("Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main execution
def main():
    user_name = get_user_name()
    display_introduction(user_name)
    selected_scale = introduce_scales(user_name)
    teach_scale(selected_scale)

    take_quiz = input("Would you like to take a quiz on this scale? (yes/no): ").strip().lower()
    while take_quiz not in ["yes", "no"]:
        take_quiz = input("Please enter 'yes' or 'no': ").strip().lower()
    quiz.administer_quiz(selected_scale)

if __name__ == "__main__":
    main()