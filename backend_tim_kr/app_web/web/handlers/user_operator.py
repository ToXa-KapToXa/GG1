import logging


class UserOperator:
    def __init__(self, logger: logging.Logger):
        self.logger = logger
        self.user_to_session = {}

    def add_session(self, user_session, user_id):
        self.user_to_session[user_id] = user_session

    def check_session(self, user_session):
        if user_session in self.user_to_session.values():
            for key in self.user_to_session.keys():
                if self.user_to_session[key] == user_session:
                    return key
        return None

    def delete_session(self, user_session):
        if user_session in self.user_to_session.values():
            for key in self.user_to_session.keys():
                if self.user_to_session[key] == user_session:
                    del self.user_to_session[key]
                    break
