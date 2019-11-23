"""
flask后端服务
"""
from flask import Flask, request
import os
from config import Config
from src.zip_png import image_zip
from werkzeug import secure_filename
import logging

app = Flask(__name__)
handler = logging.FileHandler('log/app.log', encoding='UTF-8')
# 设置日志文件，和字符编码
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
handler.setFormatter(logging_format)
app.logger.addHandler(handler)


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
            app.logger.info('get_task'+str(file.filename))
            filename = secure_filename(file.filename)  # 获取上传文件的文件名
            file.save(os.path.join(Config.image_save_path, filename))  # 保存文件
            result = image_zip(filename)
            app.logger.info('result' + str(result))
            return result
        else:
            app.logger.info('result' + 'no task')
            return {'status': 'no task'}
    except Exception as e:
        app.logger.exception('%s', e)
        return {'status': 1, 'error': e}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=Config.port, debug=True)
