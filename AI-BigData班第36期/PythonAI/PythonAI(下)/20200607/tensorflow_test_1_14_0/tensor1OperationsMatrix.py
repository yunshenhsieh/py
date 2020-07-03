import tensorflow as tf

# 二維張量
matrix1 = tf.constant( [ [ 3, 3] ] )

#二維張量
matrix2 = tf.constant( [ [2], [2] ] )

matmul = tf.matmul(matrix1, matrix2) #矩陣的乘法
add = matrix1+matrix2 #矩陣相加
subtract = matrix1-matrix2 #矩陣相減
multiply = matrix1*matrix2 #矩陣相乘
divide = matrix1/matrix2 #矩陣相除
pow = matrix1**matrix2 #矩陣次方
mod = matrix1%matrix2 #矩陣求餘數
div = matrix1//matrix2 #矩陣求商數

# 啟動 Session
with tf.Session() as sess:
    print("matrix1為{}矩陣, 數值為{}".format(matrix1.get_shape().as_list(), sess.run(matrix1)))
    print("matrix2為{}矩陣, 數值為{}".format(matrix2.get_shape().as_list(), sess.run(matrix2)))
    print("matmul為{}矩陣, 數值為{}".format(matmul.get_shape().as_list(), sess.run(matmul)))

    print("add為{}矩陣, 數值為{}".format(add.get_shape().as_list(), sess.run(add)))
    print("subtract為{}矩陣, 數值為{}".format(subtract.get_shape().as_list(), sess.run(subtract)))
    print("multiply為{}矩陣, 數值為{}".format(multiply.get_shape().as_list(), sess.run(multiply)))
    print("divide為{}矩陣, 數值為{}".format(divide.get_shape().as_list(), sess.run(divide)))

    print("pow為{}矩陣, 數值為{}".format(pow.get_shape().as_list(), sess.run(pow)))
    print("mod為{}矩陣, 數值為{}".format(mod.get_shape().as_list(), sess.run(mod)))
    print("div為{}矩陣, 數值為{}".format(div.get_shape().as_list(), sess.run(div)))
