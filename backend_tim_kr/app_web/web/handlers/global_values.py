# <-- JSON ошибки --> #
JSON_ERROR_BAD_REQUEST = {  # 400
    'result': 0,
    'response_code': 400,
    'error': 'Bad request',
    'detail': ''
}
JSON_ERROR_UNAUTHORIZED = {  # 401
    'result': 0,
    'response_code': 401,
    'error': 'Unauthorized',
    'detail': 'This request requires an access key.'
}
JSON_ERROR_FORBIDDEN = {  # 403
    'result': 0,
    'response_code': 403,
    'error': 'Forbidden',
    'detail': 'You don`t have access to this resource.'
}
JSON_ERROR_NOT_FOUND = {  # 404
    'result': 0,
    'response_code': 404,
    'error': 'Page not found',
    'detail': 'Page with URL: {URL} not found.'
}

JSON_ERROR_SERVER_ERROR = {  # 500
    'result': 0,
    'response_code': 500,
    'error': 'Internal Server Error',
    'detail': 'The server has encountered a situation that it does not know how to handle.'
}

# <-- JSON успех --> #
JSON_SUCCESS_POST = {  # 200
    'result': 1,
    'response_code': 200,
    'success': 'Post request success',
}

JSON_SUCCESS_DELETE = {  # 200
    'result': 1,
    'response_code': 200,
    'success': 'Delete request success',
}

JSON_SUCCESS_GET = {  # 200
    'result': 1,
    'response_code': 200,
    'success': 'Get request success',
    'data': 'CHANGE_THIS_PLEASE'
}


LOG_ERROR = 'An error occurred with the {FUNC}: {ERROR}'
LOG_ERROR_DETAILS = 'Error details:\n{ERROR}'


# <-- Функции заполнения сложных шаблонов --> #
def create_json_error_bad_request(error: str) -> dict:
    return_json = JSON_ERROR_BAD_REQUEST.copy()
    return_json['detail'] = JSON_ERROR_BAD_REQUEST['detail'].format(ERROR=error)
    return return_json


def create_json_error_not_found(url: str, documentation: str) -> dict:
    return_json = JSON_ERROR_NOT_FOUND.copy()
    return_json['detail'] = JSON_ERROR_NOT_FOUND['detail'].format(URL=url, DOCUMENTATION=documentation)
    return return_json
