import numpy as np
import os
from os.path import join, exists
import json
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import colors

cmap = colors.ListedColormap(
	['#000000', '#0074D9','#FF4136','#2ECC40','#FFDC00',
	 '#AAAAAA', '#F012BE', '#FF851B', '#7FDBFF', '#870C25']
)

norm = colors.Normalize(vmin=0, vmax=9)

def plot_task(task):
	fig, axs = plt.subplots(1, 4, figsize=(15,15))
	axs[0].imshow(task['train'][0]['input'], cmap=cmap, norm=norm)
	axs[0].axis('off')
	axs[0].set_title('Train Input')
	axs[1].imshow(task['train'][0]['output'], cmap=cmap, norm=norm)
	axs[1].axis('off')
	axs[1].set_title('Train Output')
	axs[2].imshow(task['test'][0]['input'], cmap=cmap, norm=norm)
	axs[2].axis('off')
	axs[2].set_title('Test Input')
	axs[3].imshow(task['test'][0]['output'], cmap=cmap, norm=norm)
	axs[3].axis('off')
	axs[3].set_title('Test Output')
	plt.tight_layout()
	plt.show()


def plot_grids(g0,g1):
	fig, axs = plt.subplots(1, 2, figsize=(15,15))
	axs[0].imshow(g0, cmap=cmap, norm=norm)
	axs[0].axis('off')
	axs[0].set_title('Input')
	axs[1].imshow(g1, cmap=cmap, norm=norm)
	axs[1].axis('off')
	axs[1].set_title('Prediction')
	plt.tight_layout()
	plt.show()


def plot_pair(pair):
	plot_grids(pair.input.grid, pair.output.grid)

def plot_prediction(task,prediction=0):
	fig, axs = plt.subplots(2, 4, figsize=(15,15))

	axs[0,0].imshow(task['train'][0]['input'], cmap=cmap, norm=norm)
	axs[0,0].axis('off')
	axs[0,0].set_title('Train Input')
	axs[0,1].imshow(task['train'][0]['output'], cmap=cmap, norm=norm)
	axs[0,1].axis('off')
	axs[0,1].set_title('Train Output')
	axs[0,2].imshow(task['test'][0]['input'], cmap=cmap, norm=norm)
	axs[0,2].axis('off')
	axs[0,2].set_title('Test Input')
	axs[0,3].imshow(task['test'][0]['output'], cmap=cmap, norm=norm)
	axs[0,3].axis('off')
	axs[0,3].set_title('Test Output')

	axs[1,0].imshow(task['train'][0]['input'], cmap=cmap, norm=norm)
	axs[1,0].axis('off')
	axs[1,0].set_title('Train Input')
	axs[1,1].imshow(task['train'][0]['output'], cmap=cmap, norm=norm)
	axs[1,1].axis('off')
	axs[1,1].set_title('Train Output')
	axs[1,2].imshow(task['test'][0]['input'], cmap=cmap, norm=norm)
	axs[1,2].axis('off')
	axs[1,2].set_title('Test Input')
	axs[1,3].imshow(task['test'][0]['output'], cmap=cmap, norm=norm)
	axs[1,3].axis('off')
	axs[1,3].set_title('Test Output')
	
	plt.tight_layout()
	plt.show()

def plot_state(state):
	"""
	Plots the state of a system using the established ARC color scheme
	"""
	fig, axs = plt.subplots(1, 1, figsize=(15,15))
	axs.imshow(state, cmap=cmap, norm=norm)
	axs.axis('off')
	# axs[0].set_title('Train Input')
	plt.tight_layout()
	plt.show()

def flood_fill(state, i=0, j=0, target=0, replacement=-1):
	if target == replacement:
		return state
	elif state[i, j] != target:
		return state
	else:
		state[i, j] = replacement
	if i < state.shape[0] - 1:
		flood_fill(state, i + 1, j, target=target, replacement=replacement)
	if i > 0:
		flood_fill(state, i - 1, j, target=target, replacement=replacement)
	if j < state.shape[1] - 1:
		flood_fill(state, i, j + 1, target=target, replacement=replacement)
	if j > 0:
		flood_fill(state, i, j - 1, target=target, replacement=replacement)
	return state

def find_enclosed(state):
	state = flood_fill(state)
	state_B = np.zeros_like(state)
	state_B[np.where(state == 0)] = 1
	return state_B

def state_to_occupancy(state):
	return state.astype(np.bool).astype(np.int)

def find_occupancy_difference(input_state, output_state):
	input_state = state_to_occupancy(input_state)
	output_state = state_to_occupancy(output_state)
	difference = output_state - input_state
	return difference