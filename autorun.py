#!/usr/bin/env python3

import os
from todo_generator import *

file = get_todos()
os.system('subl %s' % file)
