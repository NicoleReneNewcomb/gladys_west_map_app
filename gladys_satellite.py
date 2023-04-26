import json
import os.path

"""
	Student: Nicole-Rene Newcomb
	Module: gladysSatellite
	Description: This module opens and reads the
		files containing sattelite data, including 
		latitude, longitude, altitude, and time,
		and, after converting from a list of
		dictionaries into a new dictionary of x,y
		tuple key pairs with corresponding values,
		looks up the match and returns the value.
		The function call includes x and y values
		as arguments, as well as the sat variable 
		that represents either altitude, latitude, 
		longitude, or time, depending on which file 
		information is needed for that particular 
		function call.
"""


def read_sat(sat, path_to_json_data_files):
	"""
		reads satellite data from a json file
	"""

	# data file path
	file_name = sat + "_satellite.json"
	file_path = path_to_json_data_files + "/" + file_name

	# open the file
	try:
		file_handle = open(file_path)
	except IOError:
		print("ERROR: Unable to open the file " + file_path)
		raise IOError

	# print("file_path = ", file_path)

	# read the file
	data = json.load(file_handle)

	return data


def gps_value(x, y, sat):
	"""
		This function assigns the path to the satellite
			files folder to the variable named
			path_to_json_data_files. It then calls the 
			read_sat function, which reads and assigns 
			the sattelite data into a list of 
			dictionaries. This data is then transfered 
			into a dictionary of tuple keys and values,
			where the arguments x,y match a tuple key.
	"""

	# Assigns JSON file folder path to path_to_json_data_files
	path_to_json_data_files = os.path.join(os.path.dirname(__file__), 
		"satellite_data")
	
	# Satellite data returned as 
	data = read_sat(sat, path_to_json_data_files)

	# Create new dictionary to hold tuple keys
	value_dictionary = dict()

	# Loop through dictionaries within data list
	for data_dictionary in data:
		x_temp = data_dictionary['x']
		y_temp = data_dictionary['y']
		value_temp = data_dictionary['value']

		# Assign values to dictionary with x,y tuple key
		value_dictionary[x_temp, y_temp] = value_temp
	
	# Lookup x,y values passed to function within dictionary
	value = value_dictionary[x, y]
	
	# Returns value looked up based on x,y key
	return value
