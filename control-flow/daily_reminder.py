# Prompt for a single task
task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no) ")
priority = input("Priority (high, medium, low): ")

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task.title()} is a {priority} priority task that requires immediate attention today!")
        else: 
            print(f"Reminder: {task.title()} is a {priority} task. Consider completing it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"{task.title()} is a {priority} priority task. Consider completing it as soon as possible.")
        else:
            print(f"{task.title()} is a {priority} task. Don't wait too long.")
    case "low":
        if time_bound == "yes":
            print(f"Note: {task.title()} is a {priority} priority task. Don't wait too long.")
        else:
            print(f"Note: {task.title()} is a {priority} priority task. Consider completing when you have free time.")

