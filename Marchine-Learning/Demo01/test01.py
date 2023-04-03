# 神经网络
import numpy as np

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

from tensorflow.keras.losses import BinaryCrossentropy

if __name__ == '__main__':
    x = np.array([[200.0, 17.0],
                  [120.0, 5.0],
                  [425.0, 20.0],
                  [212.0, 18.0]])
    y = np.array([1, 0, 0, 1])

    layer_1 = Dense(units=3, activation='sigmoid')  # 三层隐藏层，激活函数为sigmoid
    a1 = layer_1(x)

    layer_2 = Dense(units=1, activation='sigmoid')
    a2 = layer_2(a1)

    model = Sequential([layer_1, layer_2])

    model.compile(loss=BinaryCrossentropy())  # 需要参数
    model.fit(x, y, epochs=100)

    x_new = np.array([[200.0, 17.0],
                      [120.0, 5.0]])

    print(model.predict(x_new))
