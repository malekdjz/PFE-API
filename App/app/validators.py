from django.core.exceptions import ValidationError

def validate_file_size(value):
    if value.size <= 10485760:
        return value
    raise ValidationError('Max file size is 10MB')

