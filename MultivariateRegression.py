# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 11:07:49 2018

@author: NI389899
"""
import matplotlib.pyplot as plt
import pandas as pd

#computong error for various intercept,slope values
def compute_error_for_line_given_points(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 2]
        y = points[i, 1]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(points))

#for calculating step gradient descent
def step_gradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 2]
        y = points[i, 1]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]

#main gradient descent function
def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, points, learning_rate)
    return [b, m]

#importing and reading relevant columns
dataset = pd.read_csv('auto_mpg.csv',encoding = "latin1")
model = pd.DataFrame(dataset, columns = ['mpg', 'acceleration'])
points = model.reset_index().values

# Initialize the hyper parameters
learning_rate = 0.0001
initial_b = 0 # initial y-intercept guess
initial_m = 0 # initial slope guess
num_iterations = 1000

#computing parameters for best fit line
[b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
print("After {0} iterations intercept = {1}, slope = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_line_given_points(b, m, points)))

# Plot outputs
for i in range(0, len(points)):
        x = points[i, 2]
        y = points[i, 1]
        plt.scatter(x,y,color='black')

        plt.plot(model.acceleration, (m * model.acceleration + b), color='blue',linewidth=3)
        
'''lr = [0.1,0.01,0.001,0.00001]
num_iterations = [100,500,2000,10000,15000,20000]
for i in lr:
    for j in num_iterations:
       [b, m] = gradient_descent_runner(points, initial_b, initial_m, i, j)
       print("After {0} iterations intercept = {1}, slope = {2}, error = {3}".format(j, b, m, compute_error_for_line_given_points(b, m, points))) '''

print("Least error obtained for learning rate 0.001 and iterations above 10000")     
[b, m] = gradient_descent_runner(points, initial_b, initial_m, 0.001, 15000)
print("After {0} iterations intercept = {1}, slope = {2}, error = {3}".format(15000, b, m, compute_error_for_line_given_points(b, m, points)))  