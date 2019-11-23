"""
flask后端服务
"""
from flask import Flask, request
from flask_cors import *
import os
from config import Config
from src.zip_png import image_zip
from werkzeug import secure_filename
from log_file import logger as logging
from src.html_pdf import html_pdf_main
import base64

app = Flask(__name__)
CORS(app, supports_credentials=True)


def allowed_file(filename, exam_file):
    """
    验证上传的文件名是否符合要求，文件名必须带点并且符合允许上传的文件类型要求，两者都满足则返回 true
    :param filename:文件名字
    :param exam_file: 后缀检验
    :return:true false
    """
    return '.' in filename and filename.rsplit('.', 1)[1] in exam_file


@app.route("/image", methods=['POST'])
def zip_server():
    """
    png压缩服务，上传png文件，返回压缩后的png文件
    :return: jsonj结果
    """
    try:
        file = request.files['img']  # 获取上传的文件
        if file and allowed_file(file.filename, Config.PNG_ALLOWED_EXTENSIONS):  # 如果文件存在并且符合要求则为 true
            logging.info('get_task' + str(file.filename))
            filename = secure_filename(file.filename)  # 获取上传文件的文件名
            file.save(os.path.join(Config.image_save_path, filename))  # 保存文件
            result = image_zip(filename)
            logging.info('result success')
            return result
        else:
            logging.info('result' + 'no task')
            return {'status': 'no task'}
    except Exception as e:
        logging.exception('%s', e)
        return {'status': 1, 'error': e}


@app.route("/pdf", methods=['POST'])
def pdf_server(status, name):
    """
    html转pdf服务，提供html文件、网址、字符串，返回压缩后的pdf文件
    :return: jsonj结果
    """
    try:
        logging.info('get_task')
        if status == 'file':
            html_data = base64.b64decode(name)
            with open(Config.html_file, 'wb') as f:
                f.write(html_data)
        result = html_pdf_main(status, name)
        logging.info('result success')
        return result
    except Exception as e:
        logging.exception('%s', e)
        return {'status': 1, 'error': e}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=Config.port, debug=True)
