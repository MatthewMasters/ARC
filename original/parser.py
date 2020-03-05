import numpy as np
import os
from os.path import join, exists
from pathlib import Path
import json
from utils import *
from grid import Grid
from objects import ObjectFromGrid


class Task:
	def __init__(self, task):
		self.train = [Pair('train', idx, t) for idx,t in enumerate(task['train'])]
		self.train_len = len(self.train)
		self.rules = np.sum(np.stack([p.rule_vec for p in self.train]),axis=0) / self.train_len

		print(self.rules)

		if 'output' in task['test'][0].keys():
			self.test = Pair('test', 0, task['test'][0])
			output_grid = np.zeros_like(self.test.input.grid)
			t_objects = self.test.input.objects
			for t_obj in t_objects:
				obj_grid = np.zeros_like(output_grid)
				if self.rules[0] == 1:
					coords = np.copy(t_obj.coords)
					coords[:,0] += t_obj.height
					if len(np.where(coords[:,0] >= self.test.input.x)[0]) > 0:
						coords = np.copy(t_obj.coords)
						coords[:,0] -= t_obj.height
					obj_grid[coords[:,0],coords[:,1]] = t_obj.color
					output_grid += obj_grid
				elif self.rules[1] == 1:
					coords = np.copy(t_obj.coords)
					coords[:,0] += t_obj.width
					if len(np.where(coords[:,0] >= self.test.input.x)[0]) > 0:
						coords = np.copy(t_obj.coords)
						coords[:,0] -= t_obj.width
					obj_grid[coords[:,0],coords[:,1]] = t_obj.color
					output_grid += obj_grid
				elif self.rules[2] == 1:
					coords = np.copy(t_obj.coords)
					coords[:,1] += t_obj.height
					if len(np.where(coords[:,0] >= self.test.input.x)[0]) > 0:
						coords = np.copy(t_obj.coords)
						coords[:,1] -= t_obj.height
					obj_grid[coords[:,0],coords[:,1]] = t_obj.color
					output_grid += obj_grid
				elif self.rules[3] == 1:
					coords = np.copy(t_obj.coords)
					coords[:,1] += t_obj.width
					if len(np.where(coords[:,0] >= self.test.input.x)[0]) > 0:
						coords = np.copy(t_obj.coords)
						coords[:,1] -= t_obj.width
					obj_grid[coords[:,0],coords[:,1]] = t_obj.color
					output_grid += obj_grid
			self.output_grid = output_grid
			# plot_grids(self.test.input.grid, self.output_grid)
		else:
			self.test = task['test']


class Pair:
	def __init__(self, index, idx, pair):
		self.index = index
		self.idx = idx
		self.input = Grid(self.index, self.idx, pair['input'])
		self.output = Grid(self.index, self.idx, pair['output'])

		# Observables
		self.obs_same_num_objects = self.input.num_objects == self.output.num_objects # Same number of objects before and after

		rule_vec = np.zeros((4))
		c = 0
		if self.obs_same_num_objects:
			# Do objects share color?
			for obj_in in self.input.objects:
				for obj_out in self.output.objects:
					if obj_in.color == obj_out.color and obj_in.shape == obj_out.shape:
						vi = obj_out.top - obj_in.top
						vj = obj_out.left - obj_in.left
						di = abs(vi)
						dj = abs(vj)
						rule_vec[0] += di == obj_in.height
						rule_vec[1] += di == obj_in.width
						rule_vec[2] += dj == obj_in.height
						rule_vec[3] += dj == obj_in.width
						c += 1
						# print(R1,R2,R3,R4)
		rule_vec /= c
		self.rule_vec = rule_vec