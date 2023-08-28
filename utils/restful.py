# Restful API
from flask import jsonify


class HttpCode(object):
    # 响应正常
    ok = 200
    # 没有登录导致的错误
    unloginerror = 401
    # 没有权限错误
    permissionerror = 403
    # 客户端参数错误
    paramserror = 400
    # 服务器错误
    severerror = 500


def _restful_result(code, message, data):
    return jsonify({"message": message or "", "data": data or {}, "code": code})


def ok(message=None, data=None):
    return _restful_result(code=HttpCode.ok, message=message, data=data)


def unlogin_error(message="没有登录!"):
    return _restful_result(code=HttpCode.unloginerror, message=message, data=None)


def permission_error(message="没有权限!"):
    return _restful_result(code=HttpCode.permissionerror, message=message, data=None)


def params_error(message="客户端参数错误"):
    return _restful_result(code=HttpCode.paramserror, message=message, data=None)


def sever_error(message="服务器错误"):
    return _restful_result(code=HttpCode.severerror, message=message, data=None)