import torch

ckpt = torch.load('yolov5m-seg.pt')
torch.save(ckpt, 'yolov5m-seg-update.pt')