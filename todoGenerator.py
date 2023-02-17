#!/user/python3

from todo_generator import *
import sys
from sys import argv

lookup_dict = {
	'c':'critical',
	'h':'high',
	'l':'low',
	'M':'Monday',
	'T':'Tuesday',
	'W':'Wednesday',
	'Th':'Thursday',
	'F':'Friday',
	'S':'Saturday',
	'Sn':'Sunday'
}

#todo_path = '~/dev/other/todo-generator/daily'

if "--help" in argv:
	pass
	sys.exit()

if "--file" in argv or "-f" in argv:
	from_txt_file(argv[2])
	sys.exit()

if "--update" in argv:
	file_name = get_todos()
	with open(file_name, "r") as fp:
		for line in fp:
			print(line)
	sys.exit()

if "--check-all" in argv:
	file_name = get_all_todos()
	with open(file_name, 'r') as fp:
		for line in fp:
			print(line)
	sys.exit()

if "--add" in argv:
	add_todo(argv[2], argv[3], argv[4], argv[5])
	sys.exit()

if "--remove-prompt" in argv:
	while True:
		task = input("Task to remove: ")
		remove_task(task)
		cont = input("Add ANother [y/N]: ")
		if cont.lower() != 'y':
			sys.exit()

if "--remove" in argv:
	remove_task(argv[2])
	sys.exit()

while True:
	task = input("Task Name: ")
	days_short = input("Day(s) [M,T,W,Th,F,S,Sn]: ")
	time = input("Time [hh:mm]: ")
	pri = input("Priority [c/h/l]: ")

	pri = lookup_dict[pri.lower()]

	days_short = days_short.split(',')
	for day in days_short:
		print(day)
		dy = lookup_dict[day]
		print(dy)
		add_todo(task, [dy], time, pri, verbose=True)

	cont = input("Add ANother [y/N]: ")
	if cont.lower() != 'y':
		sys.exit()

