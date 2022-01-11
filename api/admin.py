from django.contrib import admin
from . models import VersionSetting, Voice, FlatVersionSettings, ChittiSettings, VasiSettings, EatNPlaySettings

# Register your models here.
class VoiceAdmin(admin.ModelAdmin):
    list_per_page = 200
    list_display = ['bot_id', 'speech_to_text', 'type', 'output', 'time', 'language']
    readonly_fields = ('bot_id', 'speech_to_text', 'type', 'output', 'time', 'file', 'language')

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Voice, VoiceAdmin)
admin.site.register(VersionSetting)
admin.site.register(FlatVersionSettings)
admin.site.register(ChittiSettings)
admin.site.register(VasiSettings)
admin.site.register(EatNPlaySettings)
