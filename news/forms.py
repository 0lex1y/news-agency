from django.contrib.auth.forms import UserCreationForm


from news.models import Redactor


class RedactorsCreateForm(UserCreationForm):
    class Meta:
        model = Redactor
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "years_of_experience",
        )
