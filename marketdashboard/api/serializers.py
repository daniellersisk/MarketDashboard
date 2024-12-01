from rest_framework import serializers
from .models import Instrument

# Serializers are essential in Django REST Framework because they:

# Convert model instances into JSON for API responses.
# Parse and validate incoming JSON data for updates or inserts.
# Enforce data validation rules.
# Customize the structure and fields of your API.
# Enable nested relationships for related models.
# They streamline the process of creating APIs and make the backend more reliable and robust when communicating with frontends or external systems. Let me know if you’d like more examples or deeper insights into serializers!


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = '__all__'