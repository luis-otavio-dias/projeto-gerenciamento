from students.models import Students


def validate_token(token):
    return Students.objects.filter(token=token).first()
