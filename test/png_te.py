import requests
from ignore_file import Config


def png_test(file):
    """
    png模拟请求测试
    :param file: png文件路径
    :return: 结果
    """
    files = {'img': open(file, 'rb')}
    print(files)
    r = requests.post('http://' + Config.ip + ':'+str(Config.port) + '/image', files=files)
    print(r.text)


png_test('../data/20190930124444.png')
