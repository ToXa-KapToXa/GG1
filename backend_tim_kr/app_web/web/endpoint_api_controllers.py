import traceback
from flask import Blueprint, request, make_response, jsonify

from . import logger, db_operator, user_admin
from .handlers.global_values import *

module = Blueprint(name='api_page', import_name=__name__, url_prefix='/api')


@module.route('/registration', methods=['POST'])
def registration():
    try:
        coming_json = request.json
        if coming_json['password'] != coming_json['second_password']:
            response_json = JSON_ERROR_BAD_REQUEST.copy()
            response_json['detail'] = "Пароли не совпадают!"
            return make_response(jsonify(response_json), response_json['response_code'])

        is_new_user = db_operator.registration(email=coming_json['email'],
                                               password=coming_json['password'])
        if not is_new_user:
            response_json = JSON_ERROR_BAD_REQUEST.copy()
            response_json['detail'] = "Почта занята!"
            return make_response(jsonify(response_json), response_json['response_code'])

        return make_response(jsonify(JSON_SUCCESS_POST), JSON_SUCCESS_POST['response_code'])
    except Exception as e:
        logger.error(LOG_ERROR.format(FUNC='api/registration method handler', ERROR=str(e)))
        logger.debug(LOG_ERROR_DETAILS.format(ERROR=traceback.format_exc()))


@module.route('/auth', methods=['POST'])
def auth():
    try:
        coming_json = request.json
        is_success, user_id = db_operator.auth(email=coming_json['email'],
                                               password=coming_json['password'])
        if not is_success:
            response_json = JSON_ERROR_BAD_REQUEST.copy()
            response_json['detail'] = "Неверно указан логин или пароль!"
            return make_response(jsonify(response_json), response_json['response_code'])

        user_session = user_admin.add_session(user_id=user_id)
        response_json = JSON_SUCCESS_POST.copy()
        response_json['session'] = user_session

        return make_response(jsonify(response_json), response_json['response_code'])
    except Exception as e:
        logger.error(LOG_ERROR.format(FUNC='api/auth method handler', ERROR=str(e)))
        logger.debug(LOG_ERROR_DETAILS.format(ERROR=traceback.format_exc()))


@module.route('/logout', methods=['POST'])
def logout():
    try:
        coming_json = request.json

        user_admin.delete_session(user_session=coming_json['user_session'])

        return make_response(jsonify(JSON_SUCCESS_POST), JSON_SUCCESS_POST['response_code'])
    except Exception as e:
        logger.error(LOG_ERROR.format(FUNC='api/logout method handler', ERROR=str(e)))
        logger.debug(LOG_ERROR_DETAILS.format(ERROR=traceback.format_exc()))


@module.route('/check/<string:user_session>', methods=['GET'])
def check(user_session):
    try:
        user_id = user_admin.check_session(user_session=user_session)
        if user_id is None:
            response_json = JSON_ERROR_BAD_REQUEST.copy()
            response_json['detail'] = "Пользователь не активен"
            return make_response(jsonify(response_json), response_json['response_code'])

        response_json = JSON_SUCCESS_GET.copy()
        response_json['data'] = user_id
        return make_response(jsonify(response_json), response_json['response_code'])
    except Exception as e:
        logger.error(LOG_ERROR.format(FUNC='api/check/<user_session> method handler', ERROR=str(e)))
        logger.debug(LOG_ERROR_DETAILS.format(ERROR=traceback.format_exc()))


@module.route('/product', methods=['GET'])
def product():
    try:
        all_product = db_operator.product()
        response_json = JSON_SUCCESS_GET.copy()
        response_json['data'] = all_product
        return make_response(jsonify(response_json), response_json['response_code'])
    except Exception as e:
        logger.error(LOG_ERROR.format(FUNC='api/product method handler', ERROR=str(e)))
        logger.debug(LOG_ERROR_DETAILS.format(ERROR=traceback.format_exc()))


@module.route('/product/with_id/<int:product_id>', methods=['GET'])
def product_with_id(product_id):
    try:
        all_product = db_operator.product_with_id(product_id)
        response_json = JSON_SUCCESS_GET.copy()
        response_json['data'] = all_product
        return make_response(jsonify(response_json), response_json['response_code'])
    except Exception as e:
        logger.error(LOG_ERROR.format(FUNC='api/product/with_id/<int:product_id> method handler', ERROR=str(e)))
        logger.debug(LOG_ERROR_DETAILS.format(ERROR=traceback.format_exc()))


@module.route('/product/category/<string:category>', methods=['GET'])
def product_with_category(category):
    try:
        all_product = db_operator.product_with_category(category)
        response_json = JSON_SUCCESS_GET.copy()
        response_json['data'] = all_product
        return make_response(jsonify(response_json), response_json['response_code'])
    except Exception as e:
        logger.error(LOG_ERROR.format(FUNC='api/product/category/<string:category> method handler', ERROR=str(e)))
        logger.debug(LOG_ERROR_DETAILS.format(ERROR=traceback.format_exc()))


@module.route('/product/hit', methods=['GET'])
def product_with_hit():
    try:
        all_product = db_operator.product_with_hit()
        response_json = JSON_SUCCESS_GET.copy()
        response_json['data'] = all_product
        return make_response(jsonify(response_json), response_json['response_code'])
    except Exception as e:
        logger.error(LOG_ERROR.format(FUNC='api/product/hit method handler', ERROR=str(e)))
        logger.debug(LOG_ERROR_DETAILS.format(ERROR=traceback.format_exc()))


@module.route('/product/sale', methods=['GET'])
def product_with_sale():
    try:
        all_product = db_operator.product_with_sale()
        response_json = JSON_SUCCESS_GET.copy()
        response_json['data'] = all_product
        return make_response(jsonify(response_json), response_json['response_code'])
    except Exception as e:
        logger.error(LOG_ERROR.format(FUNC='api/product/hit method handler', ERROR=str(e)))
        logger.debug(LOG_ERROR_DETAILS.format(ERROR=traceback.format_exc()))


@module.route('/add_bucket', methods=['POST'])
def add_bucket():
    try:
        coming_json = request.json
        db_operator.add_bucket(coming_json['user_id'], coming_json['product_id'])
        return make_response(jsonify(JSON_SUCCESS_POST), JSON_SUCCESS_POST['response_code'])
    except Exception as e:
        logger.error(LOG_ERROR.format(FUNC='api/add_bucket method handler', ERROR=str(e)))
        logger.debug(LOG_ERROR_DETAILS.format(ERROR=traceback.format_exc()))


@module.route('/delete_bucket/<int:user_id>/<int:product_id>', methods=['DELETE'])
def delete_bucket(user_id, product_id):
    try:
        db_operator.delete_bucket(user_id, product_id)
        return make_response(jsonify(JSON_SUCCESS_DELETE), JSON_SUCCESS_DELETE['response_code'])
    except Exception as e:
        logger.error(LOG_ERROR.format(FUNC='api/delete_bucket/<user_id>/<product_id> method handler', ERROR=str(e)))
        logger.debug(LOG_ERROR_DETAILS.format(ERROR=traceback.format_exc()))


@module.route('/get_bucket/<int:user_id>', methods=['GET'])
def get_bucket(user_id):
    try:
        bucket = db_operator.get_bucket(user_id)
        response_json = JSON_SUCCESS_GET.copy()
        response_json['data'] = bucket
        return make_response(jsonify(response_json), response_json['response_code'])
    except Exception as e:
        logger.error(LOG_ERROR.format(FUNC='api/add_bucket method handler', ERROR=str(e)))
        logger.debug(LOG_ERROR_DETAILS.format(ERROR=traceback.format_exc()))
