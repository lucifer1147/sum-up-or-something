from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from drf_extra_fields.fields import Base64ImageField

User = get_user_model()

class CreateUserSerializer(UserCreateSerializer):
    profile_photo = Base64ImageField()
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = '__all__'