from .models import VersionSetting, Voice, FlatVersionSettings, ChittiSettings, VasiSettings, EatNPlaySettings
from rest_framework import serializers

class VersionSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VersionSetting
        fields = '__all__'

class VoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voice
        fields = '__all__'

class FlatVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlatVersionSettings
        fields = '__all__'

class ChittiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChittiSettings
        fields = '__all__'

class VasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = VasiSettings
        fields = '__all__'

class EatNPlaySettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EatNPlaySettings
        fields = '__all__'
