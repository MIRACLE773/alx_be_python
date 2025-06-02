task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an unknown priority level"

if time_bound == "yes":
    if priority in ["high", "medium"]:
        reminder += " that requires immediate attention today!"
    elif priority == "low":
        reminder += ". Consider completing it soon since it's time-bound."
else:
    if priority == "low":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += "."

print(reminder)
print("Well done on completing this project! Let the world hear about this milestone achieved.")
print("🚀 Click here to tweet! 🚀")
