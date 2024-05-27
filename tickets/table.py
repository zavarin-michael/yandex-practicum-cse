from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

from yandex_practicum_cse import settings


class UserModel(Model):
    """
    A DynamoDB User
    """
    class Meta:
        aws_access_key_id = settings.AWS_ACCESS_KEY_ID
        aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY
        host = settings.YDB_HOST
        table_name = "dynamodb_user"
        region = 'ru-central1'

    name = UnicodeAttribute(range_key=True)
    comment = UnicodeAttribute(hash_key=True)
