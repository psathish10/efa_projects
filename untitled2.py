# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1711Mz4iTHbI4E6TpBeMFlC-rO5NgNUHX
"""

# Commented out IPython magic to ensure Python compatibility.

!git clone https://github.com/ultralytics/yolov5  # clone
# %cd yolov5
# %pip install -qr requirements.txt  # install

import torch
import utils
display = utils.notebook_init()  # checks

!unzip -q ../ob.zip -d ../

!python train.py --img 640 --batch 16 --epochs 3 --data sar.yaml --weights yolov5s.pt --nosave --cache

