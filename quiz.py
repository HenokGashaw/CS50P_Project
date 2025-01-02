import random
def get_quiz_questions():
    """Returns a dictionary of quiz questions for each scale."""
    return {
        "Selamta": [
            {"question": "What are the notes in the Selamta scale?",
             "options": ["C D F G A C", "C D E G A C", "C D Eb G Ab C"],
             "answer": "C D F G A C"},
            {"question": "What is the gap between the first two notes in Selamta?",
             "options": ["1", "1.5", "0.5"],
             "answer": "1"}
        ],
        "Tizita": [
            {"question": "What are the notes in the Tizita scale?",
             "options": ["C D F G A C", "C D E G A C", "C Db F Gb A C"],
             "answer": "C D E G A C"},
            {"question": "What is the gap between the second and third notes in Tizita?",
             "options": ["1.5", "1", "2"],
             "answer": "1"}
        ],
        "Tizita Minor": [
            {"question": "What are the notes in the Tizita Minor scale?",
             "options": ["C D Eb G Ab C", "C Db F Gb A C", "C E F G B C"],
             "answer": "C D Eb G Ab C"},
            {"question": "What is the gap between the third and fourth notes in Tizita Minor?",
             "options": ["2", "0.5", "1.5"],
             "answer": "2"}
        ],
        "Chernet": [
            {"question": "What are the notes in the Chernet scale?",
             "options": ["C Db F Gb A C", "C D F G A C", "C D Eb G Ab C"],
             "answer": "C Db F Gb A C"},
            {"question": "What is the gap between the second and third notes in Chernet?",
             "options": ["2", "0.5", "1.5"],
             "answer": "2"}
        ],
        "Ambasel": [
            {"question": "What are the notes in the Ambasel scale?",
             "options": ["C Db F G Ab C", "C D F G A C", "C Db F Gb A C"],
             "answer": "C Db F G Ab C"},
            {"question": "What is the gap between the third and fourth notes in Ambasel?",
             "options": ["1", "0.5", "2"],
             "answer": "1"}
        ],
        "Bati": [
            {"question": "What are the notes in the Bati scale?",
             "options": ["C E F G B C", "C D F G A C", "C D Eb G Ab C"],
             "answer": "C E F G B C"},
            {"question": "What is the gap between the first and second notes in Bati?",
             "options": ["2", "1.5", "1"],
             "answer": "2"}
        ],
        "Bati Minor": [
            {"question": "What are the notes in the Bati Minor scale?",
             "options": ["C Eb F G Bb C", "C E F G B C", "C Db F Gb A C"],
             "answer": "C Eb F G Bb C"},
            {"question": "What is the gap between the fourth and fifth notes in Bati Minor?",
             "options": ["1", "1.5", "2"],
             "answer": "1.5"}
        ]
        # Add questions for other scales here.
    }

def administer_quiz(scale_name):
    """Administers a quiz for the selected scale."""
    questions = get_quiz_questions().get(scale_name, [])
    if not questions:
        print(f"No quiz available for the {scale_name} scale.")
        return

    score = 0
    print(f"\nStarting quiz for the {scale_name} scale!\n")
    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q['question']}")
        for idx, option in enumerate(q["options"], start=1):
            print(f"{idx}. {option}")
        while True:
            try:
                answer = int(input("Your answer (enter the number): "))
                if 1 <= answer <= len(q["options"]):
                    if q["options"][answer - 1] == q["answer"]:
                        print("Correct!\n")
                        score += 1
                    else:
                        print(f"Wrong! The correct answer is: {q['answer']}\n")
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    print(f"\nYou scored {score} out of {len(questions)} on the {scale_name} scale.\n")
