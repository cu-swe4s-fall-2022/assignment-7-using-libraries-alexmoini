# remember to import your libraries!
import numpy as np
import pandas as pd

def get_random_matrix(num_rows, num_columns):
	"""
	Name: get_random_matrix
	Parameters: num_rows, num_columns
		num_rows: the number of rows in the matrix (int)
		num_columns: the number of columns in the matrix (int)
	Returns: a matrix of random numbers
	"""
	# uniformly distributed matrix values between (0,1]
	matrix = np.random.rand(num_rows, num_columns)
	return matrix

def get_file_dimensions(file_name):
	"""
	Name: get_file_dimensions
	Parameters: file_name
		file_name: the name of the file to read from (string)
				   File should be CSV
	Returns: the dimensions of the matrix in the file
	"""
	try:
		csv = pd.read_csv(file_name)
	except Exception as e:
		print(str(e))
		return -1
	return csv.shape

def write_matrix_to_file(num_rows, num_columns, file_name):
	"""
	Name: write_matrix_to_file
	Parameters: num_rows, num_columns, file_name
		num_rows: the number of rows in the matrix (int)
		num_columns: the number of columns in the matrix (int)
		file_name: the name of the file to write to (string)
	Returns: nothing
	"""
	if file_name[-4:] != '.csv':
		file_name += '.csv'
	try:
		matrix = get_random_matrix(num_rows, num_columns)
	except:
		print("Error: Invalid matrix dimensions")
		return -1
	try:
		np.savetxt(file_name, matrix, delimiter=',')
	except:
		print("Error: Invalid file name")
		return -1
	return 0
