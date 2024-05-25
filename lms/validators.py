from rest_framework.validators import ValidationError


class URLValidator:

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        for field in self.fields:
            tmp_val = dict(value).get(field)
            if tmp_val:
                if 'youtube.com' not in tmp_val:
                    raise ValidationError("Ссылки кроме youtube запрещены")
