def add_to_list(add_task):
	print("Task Added!")
	return add_task

def view_all_tasks(status_of_task, list_of_task):
	for index, status in enumerate(status_of_task):
		print(index+1, status, list_of_task[index])

	
def mark_task_as_completed(status_of_task, list_of_task):
	for index, task in enumerate(list_of_task):
			print(index+1, task)
	user_input = int(input("Enter the number of the completed task: "))
	user_input = user_input-1
	status_of_task[user_input] = "[X]"	
	return status_of_task

	
def delete_a_task(user_input, list_of_task):
	list_of_task.pop(user_input)
	return list_of_task

def delete_status(user_input, status_of_task):
	status_of_task.pop(user_input)
	return status_of_task


	