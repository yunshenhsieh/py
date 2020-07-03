import tensorflow as tf
import numpy as np

def layer(output_dim,input_dim,inputs,activation=None):
    W=tf.Variable(tf.random_normal([input_dim,output_dim]))
    b=tf.Variable(tf.random_normal([1,output_dim]))
    XWb=tf.matmul(inputs,W)+b
    if activation is None:
        outputs = XWb
    else:
        outputs=activation(XWb)
    return outputs

X=tf.placeholder("float",[None,4])
h=layer(output_dim=3,input_dim=4,inputs=X,activation=tf.nn.relu)
y=layer(output_dim=2,input_dim=3,inputs=h)
with tf.Session() as sess:
    init=tf.global_variables_initializer()
    sess.run(init)
    X_array=np.array([[0.4,0.2,0.4,0.5]])
    (layer_X,layer_h,layer_y)=sess.run((X,h,y),feed_dict={X:X_array})
    print('input Layer X:');print(layer_X)
    print('hidden Layer h:');print(layer_h)
    print('output Layer y:');print(layer_y)

def layer_debug(output_dim,input_dim,inputs,activation=None):
    W=tf.Variable(tf.random_normal([input_dim,output_dim]))
    b=tf.Variable(tf.random_normal([1,output_dim]))
    XWb=tf.matmul(inputs,W)+b
    if activation is None:
        outputs = XWb
    else:
        outputs=activation(XWb)
    return outputs,W,b


X = tf.placeholder("float", [None, 4])
h,W1,b1 = layer_debug(output_dim=3, input_dim=4, inputs=X, activation=tf.nn.relu)
y,W2,b2 = layer_debug(output_dim=2, input_dim=3, inputs=h)
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    X_array = np.array([[0.4, 0.2, 0.4, 0.5]])
    (layer_X, layer_h, layer_y,W1,b1,W2,b2) = sess.run((X, h, y,W1,b1,W2,b2), feed_dict={X: X_array})
    print('input Layer X:');print(layer_X)
    print('W1:');print(W1)
    print('b1:');print(b1)
    print('hidden Layer h:');print(layer_h)
    print('W2:');print(W2)
    print('b2:');print(b2)
    print('output Layer y:');print(layer_y)
