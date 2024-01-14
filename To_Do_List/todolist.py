import mysql.connector

def add_task(task_name):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database = "todolist"
    )
    cursor = connection.cursor()

    insert_query = "INSERT INTO Tasks (task_name) VALUES (%s)"
    data = (task_name,)

    cursor.execute(insert_query, data)

    connection.commit()

    cursor.close()
    connection.close()

def view_tasks():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="todolist"
    )
    cursor = connection.cursor()

    select_query = "SELECT * FROM Tasks"
    cursor.execute(select_query)

    tasks = cursor.fetchall()

    for task in tasks:
        print(f"ID: {task[0]}, Task: {task[1]}, Completed: {'Yes' if task[2] else 'No'}")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            task_name = input("Enter the task: ")
            add_task(task_name)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")