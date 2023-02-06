from rest_framework import serializers
from globalmessages.models import GlobalMessage

class GlobalMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalMessage
        fields = '__all__'

        