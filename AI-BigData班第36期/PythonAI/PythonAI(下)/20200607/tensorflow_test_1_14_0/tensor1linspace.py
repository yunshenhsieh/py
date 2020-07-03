import tensorflow as tf

linspace = tf.linspace(1.0, 5.0, 3)

with tf.Session() as sess:
    print(sess.run(linspace))
