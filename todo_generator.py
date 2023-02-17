#!/user/python3

import time
import os
from datetime import date, datetime
import pandas as pd

todo_file = "checklist.json"

todo_path = str(os.getcwd())+'/daily/'


empty_dict = {
	'Task':['Filler'],
	'Day':['Monday'],
	'Priority':['low'],
	'Time':['14:00']
}

def create_file():
	pass

# add task to todo file
#
# @param {String} task name
# @param {[String]} days to add task to
# @param {String} Priority (low, high, critical)
# @param {String} Time
def add_todo(task, days, priority, time, verbose=False):
	if not os.path.isfile(todo_file):
		df = pd.DataFrame(empty_dict)
	else:
		df = pd.read_json(todo_file)

	df = df.drop_duplicates()
	
	days = set(days)

	for day in days:
		data = {'Task':[task], 'Day':[day], 'Priority':[priority], 'Time':[time]}
		if verbose:
			print(data)
		data = pd.DataFrame(data)
		df = pd.concat([data, df], ignore_index=True)

	df.to_json(todo_file)

def remove_task(task):
	df = pd.read_json(todo_file)
	df.drop(df[df['Task'] == task].index, inplace=True)
	print(df)
	df.to_json(todo_file)


def get_todos():
	date_long = date.today()
	day = datetime.now().strftime('%A')
	df = pd.read_json(todo_file)
	df = df.drop_duplicates()

	with open(todo_path+str(date_long)+".todo", 'w') as file:
		todos = df[df['Day'].isin([day])]

		for index, row in todos.iterrows():
			string = " ☐ "+str(row['Task'])+" @due("+str(row['Time'])+") @"+str(row['Priority']+'\n')
			file.write(string)

	return todo_path+str(date_long)+".todo"

def get_all_todos():
	df = pd.read_json(todo_file)
	df = df.drop_duplicates()
	with open(str('all')+".todo", 'w') as file:

		for index, row in df.iterrows():
			string = " ☐ "+str(row['Task'])+" @due("+str(row['Day'])+" "+str(row['Time'])+") @"+str(row['Priority']+'\n')
			file.write(string)

	return "all.todo"

# Only handles one day per line
def from_txt_file(name):
	with open(name, "r") as file:
		for line in file:
			entry = line.split()
			add_todo(entry[0], entry[1], entry[2], entry[3])