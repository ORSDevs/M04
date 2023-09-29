from datetime import datetime

current_date = datetime.now().strftime("%Y-%m-%d")

with open("today.txt", "w") as file:
    file.write(current_date)

print("Current Date:", current_date)