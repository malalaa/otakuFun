from flask import Blueprint, send_from_directory, current_app

bp = Blueprint("media", __name__, url_prefix="/media")
#/media/avatar/abc.jpg
#部署的时候，在nginx中配置一个/media前装的urL
# 访向/media的时候，我们指定让他从media文件夹下寻找文件

@bp.route("/avatar/<filename>")
def get_avatar(filename):
    return send_from_directory(current_app.config['AVATARS_SAVE_PATH'], filename)


@bp.route("/post/<filename>")
def get_post_image(filename):
    return send_from_directory(current_app.config['POST_IMAGE_SAVE_PATH'], filename)


@bp.route("/banner/<filename>")
def get_banner_image(filename):
    return send_from_directory(current_app.config['BANNER_SAVE_PATH'], filename)
