import numpy as np
import os
from os.path import join, exists
from pathlib import Path
import json
from utils import *
from objects import ObjectFromGrid

class Grid:
	def __init__(self, index, idx, grid, autodetect=True):
		self.index = index
		self.idx = idx
		self.grid = np.array(grid)
		self.shape = self.grid.shape
		self.x = self.shape[0]
		self.y = self.shape[1]
		self.objects = []
		
		if autodetect:
			self.detect_objects()

	def detect_objects(self):
		results = []
		# Detect connected volumes
		for i in range(self.x):
			for j in range(self.y):
				color = self.grid[i,j]
				if color == 0: continue
				obj_grid = np.copy(self.grid)
				flood_fill(obj_grid, i, j, target=color)
				obj_coords = np.array(list(zip(*np.where(obj_grid == -1))))
				if sum([np.array_equal(obj_coords, prev_obj[0]) for prev_obj in results]) == 0:
					results.append([obj_coords,color])

		for idx, (obj_coords, color) in enumerate(results):
			obj_grid = np.zeros_like(self.grid)
			obj_grid[obj_coords[:,0],obj_coords[:,1]] = color
			self.objects.append(ObjectFromGrid(idx, obj_grid))

		self.num_objects = len(self.objects)


	# def add_object(self):
	# 	if self.num_objects == 0:
	# 		idx = 0
	# 	else:
	# 		idx = self.objects[-1].id
	# 	obj_grid = np.zeros(self.shape)
	# 	self.objects.append(ObjectFromGrid(idx, obj_grid))
	# 	self.num_objects += 1


	def get_object_by_id(self, idx):
		result = [obj for obj in objects if obj.id == idx]
		if len(result) == 0:
			return None
		return result[0]