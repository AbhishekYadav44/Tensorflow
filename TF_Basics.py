
import tensorflow as tf


scalar=tf.constant(2)
vector=tf.constant([1,2,3])

matrix=tf.constant([[1,2,3],[4,5,6],[7,8,9]])

tensor=t.constant([
				[[1,2,3],[4,7,6],[23,6,88]],
				[[2,3,4],[8,6,5],[0,2,7]],
				[[1,8,0],[2,55,78],[2,-22,88]]
				])

with tf.Session() as session:
	result=session.run(scalar)
	print "scalr output is:\n %s" %result
	
	result=session.run(vector)
	print("vector is : \n %s \n" %result)

	result=session.run(tensor)
	print("tensor is: \n %s \n" %result)
	
#-----------------------

tf.add(mat1,mat2)
tf.matmul(mat1,mat2)

#-----------------

activation functions:

sigmoid()
softplus()
softmax()
ReLU()
tanh()
	
#----------------------






import tensorflow as tf



vec=tf.random_vector(shape(3,))

a=vec+1
b=vec+2

sess=tf.Session()
print(sess.run({ab=(a,b),vec}))
#------------------------------------


import tensorflow as tf

x=tf.placeholder(tf.float32)
y=tf.placeholder(tf.float32)
z=x+y

sess=tf.Session()
result=sess.run(z,feed_dict={x:[1,2,5,6,22,3],y=[2,56,9,2,9,8]})

print(result)
sess.close()
--print(tf.Session().run(z,feed_dict={x:[1,2,3],y:[4,66,1]}))

with tf.Session() as sess
print(sess.run(z,feed_dict={x:[1,3,5],y:[2,4,6]}))

#-----------------------------------
from scipy import signal as sg

g=[-1,-1]
x=[1,2,3,4]

y=sg.convolve(x,g,'valid')
#----------------------------------------------

In the code chunks above you have just defined a default Session, but it’s also good to know that you can pass in options as well. You can, for example, specify the config argument and then use the ConfigProto protocol buffer to add configuration options for your session.

For example, if you add

config=tf.ConfigProto(log_device_placement=True)

to your Session, you make sure that you log the GPU or CPU device that is assigned to an operation. You will then get information which devices are used in the session for each operation. You could use the following configuration session also, for example, when you use soft constraints for the device placement:

config=tf.ConfigProto(allow_soft_placement=True)

#---------------------------------

