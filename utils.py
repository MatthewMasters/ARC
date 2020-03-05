import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

# from: https://www.kaggle.com/boliu0/visualizing-all-task-pairs-with-gridlines

cmap = colors.ListedColormap(
    ['#000000', '#0074D9','#FF4136','#2ECC40','#FFDC00',
     '#AAAAAA', '#F012BE', '#FF851B', '#7FDBFF', '#870C25'])
norm = colors.Normalize(vmin=0, vmax=9)

def get_data(task_filename):
    with open(task_filename, 'r') as f:
        task = json.load(f)
    return task

def plot_one(ax, input_matrix, title_text):
    ax.imshow(input_matrix, cmap=cmap, norm=norm)
    ax.grid(True,which='both',color='lightgrey', linewidth=0.5)    
    ax.set_yticks([x-0.5 for x in range(1+len(input_matrix))])
    ax.set_xticks([x-0.5 for x in range(1+len(input_matrix[0]))])     
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_title(title_text)

def plot_task(task):
    """
    Plots the first train and test pairs of a specified task,
    using same color scheme as the ARC app
    """    
    num_train = len(task['train'])
    num_test = len(task['test'])
    num_tot = num_train + num_test
    fig, axs = plt.subplots(2, num_tot, figsize=(3*num_tot,3*2))
    for i in range(num_train):
        plot_one(axs[0,i],task['train'][i]['input'],'train input')
        plot_one(axs[1,i],task['train'][i]['output'],'train output')
    i+=1
    for j in range(num_test):
        plot_one(axs[0,i+j],task['test'][j]['input'],'test input')
        plot_one(axs[1,i+j],task['test'][j]['output'],'test output')  
    plt.tight_layout()
    plt.show()