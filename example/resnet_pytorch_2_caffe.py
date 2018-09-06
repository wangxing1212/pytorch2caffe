import sys
sys.path.insert(0,'.')
import torch
from torch.autograd import Variable
from torchvision.models import resnet
import pytorch_to_caffe

if __name__=='__main__':
    name='resnet18'
    resnet18=resnet.resnet18()
    resnet18.eval()
    input=Variable(torch.ones([1,3,224,224]))
     #input=torch.ones([1,3,224,224])
    pytorch_to_caffe.trans_net(resnet18,input,name)
    pytorch_to_caffe.save_prototxt('{}.prototxt'.format(name))
    pytorch_to_caffe.save_caffemodel('{}.caffemodel'.format(name))