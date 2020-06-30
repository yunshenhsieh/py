import tensorflow as tf

range1 = tf.range( 5 )
range2 = tf.range( 5, delta=2 )
with tf.Session() as sess:
    print(sess.run(range1))
    print(sess.run(range2))
