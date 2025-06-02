import tkinter as tk
import random
user_score = 0
computer_score = 0

choices = ['Rock', 'Paper', 'Scissors']

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    result_label.config(
        text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}"
    )
    score_label.config(text=f"Score — You: {user_score} | Computer: {computer_score}")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.resizable(False, False)

tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Choose your move:", font=("Arial", 12)).pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack()

rock_btn = tk.Button(btn_frame, text="Rock", width=12, command=lambda: play('Rock'))
rock_btn.grid(row=0, column=0, padx=5, pady=5)

paper_btn = tk.Button(btn_frame, text="Paper", width=12, command=lambda: play('Paper'))
paper_btn.grid(row=0, column=1, padx=5, pady=5)

scissors_btn = tk.Button(btn_frame, text="Scissors", width=12, command=lambda: play('Scissors'))
scissors_btn.grid(row=0, column=2, padx=5, pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), pady=10)
result_label.pack()

score_label = tk.Label(root, text="Score — You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack()
root.mainloop()
