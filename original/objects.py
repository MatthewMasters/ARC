import numpy as np
from geometry import *


class ObjectFromGrid:
	def __init__(self, idx, obj_grid):
		self.id = idx
		self.grid = obj_grid
		self.children = []
		self.coords = np.array(list(zip(*np.where(self.grid > 0))))
		self.num_cells = len(self.coords)
		self.get_properties()

	def get_properties(self):
		ex_coord = self.coords[0]
		self.color = self.grid[ex_coord[0], ex_coord[1]]
		coords_min = np.min(self.coords, axis=0)
		coords_max = np.max(self.coords, axis=0)
		coords_range = coords_max - coords_min + 1
		self.height = coords_range[0]
		self.width = coords_range[1]
		self.box_area = self.height * self.width
		self.top = self.coords[np.argmin(self.coords[:,0])][0]
		self.bottom = self.coords[np.argmax(self.coords[:,0])][0]
		self.left = self.coords[np.argmin(self.coords[:,1])][1]
		self.right = self.coords[np.argmax(self.coords[:,1])][1]

		self.shape = ''
		# Check if rectangle
		if self.box_area == self.num_cells:
			self.shape = 'rectangle'
			if self.height == self.width:
				self.shape = 'square'
		else:
			self.shape = 'irregular'