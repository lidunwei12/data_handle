"""
png压缩主代码
"""
import os
import base64
from config import Config


def image_zip(file_name):
    """
    调用pngquant压缩
    :return: base64 压缩后的图像
    """
    os.system('pngquant --quality=65-80 ' + Config.image_save_path + file_name + ' --output=' + Config.new_image_path)
    with open(Config.new_image_path, 'rb')as f:
        image_data = base64.b64encode(f.read())
        image_data = image_data.decode()
    os.remove(Config.new_image_path)
    os.remove(Config.image_save_path+file_name)
    return {'status': 0, 'image': image_data}
