list1= []

def to_do():
    task= input(f"Enter the task you want to add in To-Do-List: \n")
    list1.append(task)

def task_done():
    task= int(input("Enter the no. of task you want to remove: \n"))
    task-=1
    done= list1.pop(task)
    print(f"The task completed was: \n{done}")

def show():
    for n in list1:
        print(n)

play= True
while play:
    choose= int(input("Enter your choice: \n1 to add task \n2 to remove task \n3 to view your to-do List\n"))
    if choose==1:
        to_do()
    elif choose==2:
        task_done()
    else: 
        show()