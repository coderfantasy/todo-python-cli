import datetime # Tells Python you need the datetime library
import json
import requests


def fetch_remote_tasks() -> list:
    """Fetches a list of 5 placeholder tasks from a public API."""
    
    # The URL of the public API endpoint
    API_URL = "https://jsonplaceholder.typicode.com/todos?_limit=5" # _limit=5 makes it quick

    try:
        # 1. Make the HTTP GET Request
        # The .get() function calls the server and waits for a response
        response = requests.get(API_URL)

        # 2. Check for a successful response (Status code 200 is success)
        if response.status_code == 200:
            # 3. Convert the JSON text from the internet into a Python List/Dictionary
            remote_data = response.json()
            
            # --- IMPORTANT CLEANUP STEP ---
            # The remote list has keys like 'title', 'completed', etc.
            # Your local list only has the task text. We clean it up here.
            
            # This is a list comprehension to pull just the 'title' key
            # and format it to match your existing list structure: [['task 1'], ['task 2']]
            clean_list = [[item.get('title')] for item in remote_data]

            print(f"\n--- Loaded {len(clean_list)} tasks from external API. ---\n")
            return clean_list

        else:
            print(f"Failed to fetch tasks. Status code: {response.status_code}. Loading from local file.")
            # Fallback to your local load function
            return load_tasks() 

    except requests.exceptions.RequestException as e:
        # This catches errors like 'no internet connection'
        print(f"Connection Error: {e}. Loading from local file.")
        # Fallback to your local load function
        return load_tasks()
    


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
task_list = fetch_remote_tasks()

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
