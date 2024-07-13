import tkinter as tk
from tkinter import messagebox, simpledialog

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.tasks = []

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.task_entry = tk.Entry(self.frame, width=50)
        self.task_entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=10)

        self.view_button = tk.Button(self.frame, text="View Tasks", command=self.view_tasks)
        self.view_button.pack(padx=10, pady=10)

        self.remove_button = tk.Button(self.frame, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(padx=10, pady=10)

        self.done_button = tk.Button(self.frame, text="Mark Task as Done", command=self.mark_task_as_done)
        self.done_button.pack(padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "status": "Pending"})
            self.task_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Task '{task}' added successfully!")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def view_tasks(self):
        if not self.tasks:
            messagebox.showinfo("Tasks", "No tasks available.")
        else:
            tasks_str = "\n".join([f"{i+1}. {task['task']} [{task['status']}]" for i, task in enumerate(self.tasks)])
            messagebox.showinfo("Tasks", tasks_str)

    def remove_task(self):
        if not self.tasks:
            messagebox.showinfo("Tasks", "No tasks available.")
        else:
            task_num_str = simpledialog.askstring("Remove Task", "Enter the task number to remove:")
            if task_num_str and task_num_str.isdigit():
                task_num = int(task_num_str)
                if 0 < task_num <= len(self.tasks):
                    removed_task = self.tasks.pop(task_num - 1)
                    messagebox.showinfo("Success", f"Task '{removed_task['task']}' removed successfully!")
                else:
                    messagebox.showerror("Error", "Invalid task number.")
            else:
                messagebox.showerror("Error", "Please enter a valid number.")

    def mark_task_as_done(self):
        if not self.tasks:
            messagebox.showinfo("Tasks", "No tasks available.")
        else:
            task_num_str = simpledialog.askstring("Mark Task as Done", "Enter the task number to mark as done:")
            if task_num_str and task_num_str.isdigit():
                task_num = int(task_num_str)
                if 0 < task_num <= len(self.tasks):
                    self.tasks[task_num - 1]["status"] = "Done"
                    messagebox.showinfo("Success", f"Task '{self.tasks[task_num - 1]['task']}' marked as done.")
                else:
                    messagebox.showerror("Error", "Invalid task number.")
            else:
                messagebox.showerror("Error", "Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
