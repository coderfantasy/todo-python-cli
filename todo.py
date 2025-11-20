import datetime # Tells Python you need the datetime library
import json

# 1. New Save Function
def save_tasks(task_list: list):
    """Saves the master task list to a file."""
    # Add your json import here if you are doing JSON now!
    import pickle # or import json

    # You will move the actual saving code from the main script into this try/except block
    try:
        with open("todo.json", "w") as f: # Use 'w' for text mode with JSON! 'wb' is for pickle
            # If using PICKLE (original format):
            # pickle.dump(task_list, f)

            # If using JSON (better format - recommended):
             json.dump(task_list, f) # You'll need to open the file in text mode ('w')
           
        print("Tasks saved successfully.")
    except Exception as e:
        print(f"Error saving tasks: {e}")

# 2. New Load Function
def load_tasks() -> list:
    """Loads tasks from file or returns an empty list if file is not found."""
    # Add your import here:
 
    # This is the CORE of your error handling
    try:
        # We try to open the file (The RISKY part)
        with open("todo.json", "r") as f: # Use 'r' for text mode with JSON! 'rb' is for pickle
            # If using PICKLE:
            # return pickle.load(f)
             data = json.load(f)
             return data
            # If using JSON:
            # return json.load(f) # You'll need to open the file in text mode ('r')

    except FileNotFoundError:
        # If the file is not there, we don't crash, we return a blank list
        print("No save file found. Starting a new list.")
        return []

    except Exception as e:
        # Catch any other error (like corruption)
        print(f"Error loading tasks: {e}")
        return []
    

def print_tasks(task_list): #for print the task

     # 1. Use the built-in len() function to get the count
    task_count = len(task_list)
    print(f"\n--- You currently have {task_count} tasks to do ---\n")
    task_list.sort() #sorting the task
    for row in task_list: #looping
        print(f"{row}") #print the task
 # After the loop finishes, you might want to print a blank line for formatting
    print("-" * 35) # Prints 35 hyphens for a clean separator
task_list = load_tasks()

while True: #looping
    now = datetime.datetime.now()
    today_date = now.strftime("%Y-%m-%d")
    print(f"""TODO List Management System, Today is {today_date}
    1: Add New Task
    2: View
    3: Remove
    4: Edit
    5: Exit""")
    w = input() #kind like a switch
    if w == '1':
        add = input("What do you want to add: ") #add variable is the input of What do you want to add
        row = [add]
        task_list.append(row)
        save_tasks(task_list)
    elif w == '2':
        print_tasks(task_list) #print task
    elif w == '3':
        rem = input("What do you want to remove: ")
        task_list = [row for row in task_list if row[0] != rem] #Looping, if row is same like rem, skip
        save_tasks(task_list)
    elif w == '4':
        old_task = input("Which task do you want to edit? ")
        for i, row in enumerate(task_list): #what is enumerate?
            if row[0] == old_task:
                new_task = input("What do you want to change it to: ")
                task_list[i] = [new_task]

                save_tasks(task_list)
    elif w == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice, please choose a number between 1-5.") 
