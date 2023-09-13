import schedule
import time
from datetime import datetime
import threading

# Initialize an empty list to store tasks
task_list = []

def create_task():
    print("\nCool! Let's quickly create the tasks for today...\n")
    task_name = input("Enter the task name: ")
    print("Time and Date now: ", time.strftime('%X (%d/%m/%y)'))
    task_time = input("Enter the target task time in 24-Hour format (HH:MM): ")
    task_date = input("Enter the task date in (YYYY-MM-DD) format: ")

    try:
        task_datetime = datetime.strptime(f'{task_date} {task_time}', '%Y-%m-%d %H:%M')
        time_difference_seconds = (task_datetime - datetime.now()).total_seconds()

        def notify_task():
            print(f'\nTask "{task_name}" is due now.')
            print("Get back to work")

        task = schedule.every().day.at(task_time).do(notify_task)
        task_list.append({
            "name": task_name,
            "time": task_datetime.strftime('%Y-%m-%d %H:%M')
        })
        print(f'\nTask "{task_name}" scheduled for {task_datetime.strftime("%Y-%m-%d %H:%M")}.')
        print("You'll be notified when the schedule arrives\n")
        
        # Start a thread to run the schedule in the background
        def run_schedule():
            while True:
                schedule.run_pending()
                time.sleep(1)
        
        # Start the thread
        schedule_thread = threading.Thread(target=run_schedule)
        schedule_thread.daemon = True
        schedule_thread.start()

    except ValueError:
        print("Invalid date or time format. Please use YYYY-MM-DD and HH:MM formats.")

def greeting():
    print("\nWelcome To Task Generator!")
    a = input("Hello! How are you doing Today? (good/great/bad) ? ----> ")
    if str.lower(a) == 'good':
        print("\n--Nice! Let's plan something new today!--\n")
    elif str.lower(a) == 'great':
        print("\n--Awesome! Let's achieve something new today!--\n")
    elif str.lower(a) == 'bad':
        print("\n--Oops! Don't be sad, let's make this day productive, cheer up!--\n")

def scheduling_permission():
    b = input("Do you Want to Plan Anything New Today? [Y/n]: ")
    if str.lower(b) == 'y':
        create_task()
        asking_user()
    elif str.lower(b) == 'n':
        print("Thank You for using the Service!")

def oth_services():
    g = int(input("\nDo You want to exit or continue services?\nPress 1 to continue\nPress 0 to exit: "))
    if g == 1:
        t1 = int(input(("\nDo You Want to know any other things?\nPress 1 to know 'Number of tasks pending now'\nPress 2 to 'cancel all the jobs': ")))
        if t1 == 1:
            jobs_active = input("Do You Want to know How many Tasks are Actively Present now?[Y/n]: ")
            if jobs_active.lower() == 'y':
                print("Number of tasks pending now: ", len(schedule.get_jobs()))
            else:
                oth_services()
        elif t1 == 2:
            t2 = input("\n\nDo you want to cancel all the jobs present right now? [Y/n]: ")
            if t2.lower() == 'y':
                schedule.clear()
            else:
                print("Thank You for using the Service!")
    elif g == 0:
        print("Thank You for using the Service!")

def asking_user():
    while True:
        add_another = input("Do you want to create another task? [Y/n]: ")
        if str.lower(add_another) == 'n':
            break
        create_task()

greeting()
scheduling_permission()
oth_services()

# The program will continue running in the background and notify you when tasks are due.
while True:
    pass
