import re

from authentication.db_models.users import Users

from rest_framework_jwt.settings import api_settings


class UserHelpers:
    @staticmethod
    def generate_token(user: Users):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    @staticmethod
    def split_email(email):
        m = re.search(r'(.+)@(.+)\.(.+)\.(.+)', email)
        if m:
            return m.groups()[-2:] == ('edu', 'tr')
        return False
