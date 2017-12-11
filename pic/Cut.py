#-*- coding:utf-8 -*-

import os
from PIL import Image

def get_imlist(path):
    """返回目录中所有png图像的文件名列表"""
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(".png")]

def save_change(save_dir,n,x1,y1,x2,y2):
    box = (x1,y1,x2,y2)
    region = pil_im.crop(box)

    out = region.resize((128,128))
    save_dir = save_dir + str(n) + ".png"
    print save_dir
    out.save(save_dir)


if __name__ == "__main__":

    """
    读取的图片的路径： /home/xuna/桌面/pic/img_2/
    结果的图片的路径：/home/xuna/桌面/pic/res/
    """
    path = "/home/xuna/桌面/pic/img_2/"
    listdir = get_imlist(path)

    for dir in listdir:
        infile = os.path.splitext(dir)[0]
        infile = infile.replace("img_2","res")
        save_dir = infile + "_"
        print save_dir

        pil_im = Image.open(dir)
        #pil_im.show()

        save_change(save_dir,1, 8, 44, 72, 105)
        save_change(save_dir,2, 80, 44, 144, 105)
        save_change(save_dir,3, 150, 44, 216, 105)
        save_change(save_dir,4, 223, 44, 287, 105)

        save_change(save_dir,5,8,116,72,180)
        save_change(save_dir,6,79,116,144,180)
        save_change(save_dir,7,151,116,216,180)
        save_change(save_dir,8,223,116,287,180)
