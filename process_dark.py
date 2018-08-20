import numpy as np
import copy


def frunning_mean(x, N=2):
	'''smooth data with N
	'''
	cumsum = np.cumsum(np.insert(x, 0, 0)) 
	return (cumsum[N:] - cumsum[:-N]) / float(N)

def running_mean2D(image, size=5):
	'''
	running mean of 2D image with small box of NxN size
	---------
	parameter:
	image:  2D array
	size:  odd number
	----------
	return:
	original image with smaller size 
	running mean image with smaller size
	----------
	example:
	image = np.array([[1,1,1], [2,2,2], [5,5,5]])
	a, b = running_mean2D(image, size=2)
	a = np.array([[2]])
	b = np.array([[2.66667]])
	'''
	edge = size//2
	ima = image[edge:(image.shape[0]-edge), edge:(image.shape[1]-edge)]
	
	im = np.array([frunning_mean(i, size) for i in image])
	imb = np.array([frunning_mean(i, size) for i in im.T ])
	
	return np.nan_to_num(ima), np.nan_to_num(imb.T)

def clean_dark(image, size, sp0, sp1, w, deviation=None):
	'''
	find bad points of dark and substute it with around small mean box.
	parameter:
	------------
	image: 2D array
	size: odd number
	sp0: box shift along axis0, y
	sp1: box shift along axis1, x
	w: box size wXw
	deviation: decide bad points. imb.std()*3

	return:
	-----------
	new image with smaller size
	bad point x and y
	'''

	ima, imb = running_mean2D(image, size)
	im = copy.copy(ima)

	x = np.arange(ima.shape[1], dtype=int)
	y = np.arange(ima.shape[0], dtype=int)
	X, Y = np.meshgrid(x, y)

	if deviation == None:
		deviation = ima.std()*3

	choose = np.abs(ima-imb)>deviation
	print('im.shape {} choose size {:05d}, percentile {:.6f}% ,deviation {:.2f}'.
		format(im.shape, X[choose].size, X[choose].size/ima.size*100, deviation))

	for p1, p0 in zip(X[choose], Y[choose]):
		im[p0, p1] = np.nanmean(ima[p0+sp0-w:p0+sp0+w, p1+sp1-w:p1+sp1+w])

	return im, (X[choose], Y[choose])