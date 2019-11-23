"""
html转pdf
"""
import pdfkit
from config import Config
import base64
import os


def html_pdf_main(status, name):
    """
    html文件、网址、字符串转pdf
    :param status: 类别
    :param name: 内容
    :return: 结果
    """
    try:
        if status == 'url':
            pdfkit.from_url(name, Config.pdf_save_path + 'out.pdf')
        if status == 'file':
            pdfkit.from_file(Config.html_file, Config.pdf_save_path + 'out.pdf')
            os.remove(name)
        if status == 'string':
            pdfkit.from_string(name, Config.pdf_save_path + 'out.pdf')
        with open(Config.pdf_save_path, 'rb')as f:
            pdf_data = base64.b64encode(f.read())
            pdf_data = pdf_data.decode()
        os.remove(Config.pdf_save_path + 'out.pdf')
        return {'status': 0, 'pdf': pdf_data}
    except Exception as e:
        return {'status': 0, 'error': e}

