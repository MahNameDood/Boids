import math, pygame, random

def rad_to_deg(rad):
	return rad * (180/math.pi)

def deg_to_rad(deg):
	return deg / (180/math.pi)

def distance(p1, p2):
	return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def wrap_angle(x):
	return (x+180) % 360 - 180

def steer(rot, speed, des, force):
	init_vel = [math.cos(deg_to_rad(rot))*speed, math.sin(deg_to_rad(rot))*speed]
	des_vel = [math.cos(deg_to_rad(des))*speed, math.sin(deg_to_rad(des))*speed]

	force_vel = [des_vel[0]-init_vel[0], des_vel[1]-init_vel[1]]

	new = [(init_vel[0] + force_vel[0]) * force, (init_vel[1] + force_vel[1]) * force]
	return rad_to_deg(math.atan2(new[1], new[0]))
