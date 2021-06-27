import datetime

from django.core.exceptions import ValidationError


def my_year_validator(value):
    if value < 1900 or value > datetime.datetime.now().year:
        raise ValidationError(
            ('%(value)s is not a correct year!'),
            params={'value': value},
        )
