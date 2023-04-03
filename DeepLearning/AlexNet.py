# 数据集使用imagenet

import numpy as np
import torchvision
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


# 模型
class AlexNet(nn.Module):
    def __init__(self, n_classes=10):
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(
            # 3个卷积和池化交错层
            # 2d卷积函数
            nn.Conv2d(1,96,kernel_size=11,stride=4,padding=1),
            # 结束卷积使用Relu激活函数
            nn.ReLU(inplace=True),
            # 进行池化
            nn.MaxPool2d(kernel_size=3,stride=2),



        )
