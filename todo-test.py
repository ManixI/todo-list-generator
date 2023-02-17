#!/user/python3

from todo_generator import *

add_todo('Test', ['Thursday', 'Friday', 'Saturday'], 'low', '12:00')
add_todo('Practice', ['Monday', 'Wednesday', 'Friday', 'Saturday', 'Sunday'], 'low', '18:00')

remove_task('Filler')
remove_task('Test')
get_todos()
get_all_todos()
remove_task('Practice')