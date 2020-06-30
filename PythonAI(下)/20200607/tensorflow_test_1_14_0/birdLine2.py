import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#隨機產生100個棲息座標x_data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 8
noise_data = np.random.normal(0.0, 0.5, 100).astype(np.float32)



# 統計100點實際飛鳥棲息的偏移值
plt.hist(noise_data)
plt.show()


# 落點公式(把偏移值也考慮進去)
y_data = x_data * 8 + noise_data

# 最後畫出飛鳥實際棲息的分布圖
plt.plot(x_data, y_data, 'o', label='data: y_data=x_data*8 + noise_data')
plt.legend()
plt.show()