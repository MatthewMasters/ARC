import numpy as np
import os
from os.path import join, exists
from pathlib import Path
import json
from utils import *
from parser import Task

data_path = Path('/home/matthew/Programming/ARC/data/')
training_path = data_path / 'training'
evaluation_path = data_path / 'evaluation'
test_path = data_path / 'test'

training_tasks = sorted(os.listdir(training_path))

i = 127

task_file = str(training_path / training_tasks[i])
with open(task_file, 'r') as f:
    task_dict = json.load(f)


task = Task(task_dict)
print(task.output_grid)

# print(task_dict)