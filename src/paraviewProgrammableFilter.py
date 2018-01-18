from vtk.numpy_interface import dataset_adapter as dsa
from vtk.numpy_interface import algorithms as algs
import numpy

data=inputs[0]

# provide a NumPy-style interface, but the array is essentially the VTKArray
print isinstance(data,dsa.VTKObjectWrapper)
deltav=data.PointData['deltav']
# work with arrays
print deltav[0]
print deltav[-1]
print deltav[deltav>0] # keep all the values that is greater than zero

density=2650/(1+deltav)
for i in xrange (len(density)):
	if density[i]==2650 or density[i]<0:
		density[i]=0
	elif density[i]>4000:
		density[i]=3000
output.PointData.append(density,'density')

