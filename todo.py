import datetime # Tells Python you need the datetime library

def print_tasks(task_list): #for print the task

     # 1. Use the built-in len() function to get the count
    task_count = len(task_list)
    print(f"\n--- You currently have {task_count} tasks to do ---\n")
    task_list.sort() #sorting the task
    for row in task_list: #looping
        print(f"{row}") #print the task
 # After the loop finishes, you might want to print a blank line for formatting
    print("-" * 35) # Prints 35 hyphens for a clean separator
task_list = [] #array


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
        row = [add] #put it on row array
        task_list.append(row) #add to task list
    elif w == '2':
        print_tasks(task_list) #print task
    elif w == '3':
        rem = input("What do you want to remove: ")
        task_list = [row for row in task_list if row[0] != rem] #Looping, if row is same like rem, skip
    elif w == '4':
        old_task = input("Which task do you want to edit? ")
        for i, row in enumerate(task_list): #what is enumerate?
            if row[0] == old_task:
                new_task = input("What do you want to change it to: ")
                task_list[i] = [new_task]
    elif w == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice, please choose a number between 1-5.") 
