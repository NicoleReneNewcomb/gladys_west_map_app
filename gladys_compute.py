import gladys_satellite as satellite
import math

"""
	Student: Seraina Burge
	Module: gladys_compute
	Description: This module computes the average distance between
 	the two satellite positions
	using the coordinates from the gladys_satellite module
"""


def gps_average(x, y):
	"""
		calculates the average distance between the two positions based on
		the longitudal, altidudal, latitudal and time distances
	"""
	
	"Add up the before mentioned distances by getting them from the satellite module"
	value = satellite.gps_value(x, y, "altitude") + satellite.gps_value(x, y, "longitude") + satellite.gps_value(x, y, "latitude") + satellite.gps_value(x, y, "time")
	"get the average by dividing the total distanc by 4"
	average = value / 4

	return average


def distance(x_current, y_current, x_destination, y_destination):
	"""
		Calculates the distance between two points using the gps_average function
	"""

	"""
		Distance => Add the average distance squared of both points and get the root of that.
	"""
 
	distance = math.sqrt(pow(gps_average(x_current, y_current), 2) + pow(gps_average(x_destination, y_destination), 2))

	return distance
