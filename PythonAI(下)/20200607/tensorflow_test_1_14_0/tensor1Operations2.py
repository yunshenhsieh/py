import tensorflow as tf

a = tf.constant( 8 )
b = tf.constant( 5 )

tf_add = tf.add(a, b)
tf_subtract = tf.subtract(a, b)
tf_multiply = tf.multiply(a, b)
tf_divide = tf.divide(a, b)
tf_pow = tf.pow(a, b)
tf_mod = tf.mod(a, b)
tf_div = tf.div(a, b)

with tf.Session() as sess:
  print(sess.run(tf_add))
  print(sess.run(tf_subtract))
  print(sess.run(tf_multiply))
  print(sess.run(tf_divide))
  print(sess.run(tf_pow))
  print(sess.run(tf_mod))
  print(sess.run(tf_div))
