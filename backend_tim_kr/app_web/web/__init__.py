from flask import Flask, make_response, jsonify
from flask_cors import CORS

from .database.db_operator import DBOperator
from .handlers.user_operator import UserOperator

logger = None
db_operator = None
user_admin = None


def create_api(flask_log: bool,
               logging_cgf_path: str,
               db_host: str,
               db_port: int,
               db_login: str,
               db_password: str,
               ) -> Flask:
    """
    Функция инициализаций прикладных алгоритмов к API.

    Функция отвечает за создание различных обработчиков, таких как:
        - logger: Обработчик логирования
        - db_operator: Обработчик базы данных
        - user_admin: Обработчик авторизаций

    Arguments:
        flask_log (bool): Если True, то встроенное логирование Flask будет
            отключено, иначе останется включенным.
        logging_cgf_path (str): Путь до файла с конфигурацией логирования.
        db_host (str): Хост базы данных.
        db_port (int): Порт базы данных.
        db_login (str): Логин пользователя для взаимодействия с базой данных.
        db_password (str): Пароль пользователя для взаимодействия с базой
            данных.

    Returns:
         Flask: Объект класса, который необходим для создания приложения.
    """
    global logger, db_operator, user_admin

    app = Flask(__name__)
    CORS(app)

    # Инициализация логирования
    from .initialization_logger import get_logger
    logger = get_logger(
        logging_cfg_path=logging_cgf_path,
        flask_log=flask_log,
        flask_app=app,
    )

    # Инициализация Базы данных
    db_operator = DBOperator(
        logger=logger,
        db_host=db_host,
        db_port=db_port,
        db_login=db_login,
        db_password=db_password,
    )

    # Инициализация обработчика авторизаций
    user_admin = UserOperator(
        logger=logger
    )

    from . import endpoint_api_controllers as api_control
    from .handlers.global_values import JSON_ERROR_NOT_FOUND

    # Подключение endpoint`ов
    app.register_blueprint(api_control.module)

    @app.errorhandler(404)
    def not_found(_error):
        """
        Обработчик 404 ошибки

        При возникновении ситуации, когда пользователь обращается по URL к
        которому не существует обработчика, сработает данный обработчик. В
        ответ он вернёт JSON с ошибкой (HTTP код 404). JSON формируется из
        шаблонов файла `global_values`.

        Arguments:
            _error: Обязательный параметр декоратора.

        Returns:
            Response - JSON с ошибкой и 404 HTTP код.
        """
        return make_response(jsonify(JSON_ERROR_NOT_FOUND), JSON_ERROR_NOT_FOUND['response_code'])

    return app
