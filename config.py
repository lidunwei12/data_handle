"""
参数
"""


class Config:
    """
    zip_png配置参数

    """
    image_save_path = 'data/'
    new_image_path = 'temp/temp.png'
    PNG_ALLOWED_EXTENSIONS = set(['png'])
    """
    html转pdf 
    """
    pdf_save_path = 'temp/'
    html_file = 'data/temp.pdf'
    """
    flask主服务
    """
    port = 3301
