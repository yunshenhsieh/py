import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as input_data
from time import time
import matplotlib.pyplot as plt
import tf_keras_17

mnist = input_data.read_data_sets("MNIST_data/",one_hot=True)
def weight(shape):
    return tf.Variable(tf.truncated_normal(shape,stddev=0.1),name='W')
def bias(shape):
    return tf.Variable(tf.constant(0.1,shape=shape),name='b')
def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')
def max_pool_2x2(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

with tf.name_scope('Input_Layer'):
    x=tf.placeholder("float",shape=[None,784],name='x')
    x_image=tf.reshape(x,[-1,28,28,1])# x reshape為4維張量，輸入筆數不固定為-1，單色為1，彩色為3
with tf.name_scope('C1_Conv'):
    W1=weight([5,5,1,16])
    b1=bias([16])
    Conv1=conv2d(x_image,W1)+b1
    C1_Conv=tf.nn.relu(Conv1)
with tf.name_scope('C1_Pool'):
    C1_Pool=max_pool_2x2(C1_Conv)
with tf.name_scope('C2_Conv'):
    W2=weight([5,5,16,36])
    b2=bias([36])
    Conv2=conv2d(C1_Pool,W2)+b2
    C2_Conv=tf.nn.relu(Conv2)
with tf.name_scope('C2_Pool'):
    C2_Pool=max_pool_2x2(C2_Conv)
with tf.name_scope('D_Flat'):
    D_Flat=tf.reshape(C2_Pool,[-1,1764])
with tf.name_scope('D_Hidden_Layer'):
    W3=weight([1764,128])
    b3=bias([128])
    D_Hidden=tf.nn.relu(tf.matmul(D_Flat,W3)+b3)
    D_Hidden_Dropout=tf.nn.dropout(D_Hidden,keep_prob=0.8)
with tf.name_scope('Output_Layer'):
    W4=weight([128,10])
    b4=bias([10])
    y_predict=tf.nn.softmax(tf.matmul(D_Hidden_Dropout,W4)+b4)
with tf.name_scope("optimizer"):
    y_label=tf.placeholder("float",shape=[None,10],name="y_label")
    loss_function=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y_predict,labels=y_label))
    optimizer=tf.train.AdamOptimizer(learning_rate=0.0001).minimize(loss_function)
with tf.name_scope("evaluate_model"):
    correct_prediction=tf.equal(tf.argmax(y_predict,1),tf.argmax(y_label,1))
    accuracy=tf.reduce_mean(tf.cast(correct_prediction,"float"))

trainEpochs=30
batchSize=100
totalBatchs=int(mnist.train.num_examples/batchSize)
loss_list=[];epoch_list=[];accuracy_list=[]
startTime=time()
sess=tf.Session()
sess.run(tf.global_variables_initializer())

for epoch in range(trainEpochs):
    for i in range(totalBatchs):
        batch_x,batch_y=mnist.train.next_batch(batchSize)
        sess.run(optimizer,feed_dict={x:batch_x,y_label:batch_y})
    loss,acc=sess.run([loss_function,accuracy],feed_dict={x:mnist.validation.images,y_label:mnist.validation.labels})
    epoch_list.append(epoch);
    loss_list.append(loss)
    accuracy_list.append(acc)
    print("Train Epoch:",'%02d' % (epoch+1),"Loss=","{:.9f}".format(loss),"Accuracy=",acc)
duration=time()-startTime
print("Train Finished takes:",duration)

fig=plt.gcf()
fig.set_size_inches(4,2)
plt.plot(epoch_list,loss_list,label='loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['loss'],loc='upper left')
plt.show()

plt.plot(epoch_list,accuracy_list,label='accuracy')
fig=plt.gcf()
fig.set_size_inches(4,2)
plt.ylim(0.8,1)
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend()
plt.show()
print('Accuracy:',sess.run(accuracy,feed_dict={x:mnist.test.images,y_label:mnist.test.labels}))


prediction_result=sess.run(tf.argmax(y_predict,1),feed_dict={x:mnist.test.images,y_label:mnist.test.labels})
print(prediction_result[:10])
tf_keras_17.plot_images_labels_prediction(mnist.test.images,mnist.test.labels,prediction_result,0)

# TensorBoard，視覺化看計算流程圖
merged=tf.summary.merge_all()
train_writer=tf.summary.FileWriter('log/CNN',sess.graph)