date = input ("Enter today's date: ")
mood  = input("how do you rate your mood from 1 to 10? ")
thought = input("let us know your thought: \n")

with open(f"../journal/{date}.txt" , "w") as file:
    file.write(mood +2 * "\n")
    file.write(thought)