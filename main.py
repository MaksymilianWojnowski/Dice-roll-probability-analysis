# Import necessary libraries
import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from itertools import product

# Function to generate and show the plot inside the tkinter frame
def show_plot(number_of_die, frame):
    # Clear any previously displayed figures in the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Generate all possible outcomes of rolling the specified number of six-sided dice
    outcomes = list(product(range(1, 7), repeat=number_of_die))
    sums_counts = {}

    # Count the occurrence of each sum of the dice rolls
    for outcome in outcomes:
        outcome_sum = sum(outcome)
        if outcome_sum in sums_counts:
            sums_counts[outcome_sum] += 1
        else:
            sums_counts[outcome_sum] = 1

    # Calculate the total number of combinations
    total_combinations = sum(sums_counts.values())

    # Calculate the probability of each sum and round it to 2 decimal places
    probabilities = {sum_: round((count / total_combinations) * 100, 2) for sum_, count in sums_counts.items()}

    # Create a matplotlib figure to plot the probabilities
    fig = plt.Figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.bar(list(probabilities.keys()), list(probabilities.values()))
    ax.set_title("Probability of rolling a sum with " + str(number_of_die) + " dice (6-sided)")
    ax.set_xlabel("Total Sum of Die Faces")
    ax.set_ylabel("Probability [%]")
    ax.set_xticks(list(probabilities.keys()))
    ax.get_yaxis().set_visible(False)

    # Add text labels above each bar in the bar chart
    for i, value in enumerate(list(probabilities.values())):
        ax.text(i + 1 + number_of_die - 1, value, str(value), ha='center')

    # Embed the matplotlib figure into the tkinter frame
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Function to prompt the user to enter the number of dice to roll
def ask_number_of_dice():
    # Use tkinter's simpledialog to ask for integer input
    number_of_die = simpledialog.askinteger("Input", "How many dice do you want to roll?", parent=root, minvalue=1, maxvalue=10)
    # If the user provided a valid input, display the plot
    if number_of_die:
        show_plot(number_of_die, frame)

# Set up the main tkinter window
root = tk.Tk()
root.title("Dice Roll Probability")

# Create a frame in the tkinter window to hold the plot
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)

# Delay the display of the input dialog to ensure the main window is fully loaded
root.after(100, ask_number_of_dice)

# Start the tkinter event loop
root.mainloop()
