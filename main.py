import numpy as np
import os
from os.path import join, exists
from pathlib import Path
import json

class Task:
	"""
	A task consists of four objects:
		1. State (binary string)
		2. Situation generation function
			- input: State
			- output: Situation
			- generates binary string Situation which belongs to the situation space
		3. Scoring function
			- inputs: [Situation, Response, State]
			- outputs: [Score, Feedback]
			- Score is a scalar value meant to measure the appropriateness of a response to a situation
			- Feedback is a binary string. It may encode full or partial information about the current score, or about scores corresponding to past responses
		4. Self-update function
			- inputs: [Response, State]
			- output: State
			- mutates the task state based on the response to the latest situation
	"""

	def __init__(self, task_id):
		self.task_id = task_id
		self.state = 0
		self.load_task()
	

	def load_task(self):
		self.task_file = str(training_path / training_tasks[self.task_id])
		with open(self.task_file, 'r') as f:
			self.task_dict = json.load(f)
		self.train_states = self.task_dict['train']
		self.test_states = self.task_dict['test']
		self.num_states = len(self.states)

	def generator(self):
		"""
		Generates sitation from state
		input: State
		output: Situation
		"""

		return

	def scoring_function(self):
		"""
		Scores the appropriateness of a response to a situation
		inputs: [Situation, Response, State]
		outputs: [Score, Feedback]
		"""
		score, feedback = 0.0, []
		return score, feedback

	def update(self, response):
		"""
		Self-update function. Mutates the task state based on the response to the latest situtation
		input: [Response, State]
		output: State
		"""
		if response == 'STOP':
			self.state = -1
		else:
			self.state += 1


class IntelligentSystem:
	"""
	An IntelligentSystem consists of three objects:
		1. State (binary string)
		2. Skill program generation function
			- input: State
			- outputs: [SkillProgram, SkillProgram.State]
			- 
	"""



	def __init__(self):
		self.state = []

class IntelligentSystem:
	def __init__(self):
		self.state = []




if __name__ == '__main__':
	data_path = Path('/home/matthew/Programming/ARC/data/')
	training_path = data_path / 'training'
	evaluation_path = data_path / 'evaluation'
	test_path = data_path / 'test'

	training_tasks = sorted(os.listdir(training_path))
	print(len(training_tasks))
	# i = 127

	# task_file = str(training_path / training_tasks[i])
	# with open(task_file, 'r') as f:
	#     task_dict = json.load(f)


	# task = Task(task_dict)
	# print(task.output_grid)

	# print(task_dict)