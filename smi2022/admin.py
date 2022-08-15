from django.contrib import admin

from .models import TemaPublik, NameSmi, VidSmi, TonPublik, VidPublik, VidMeropriyatia, VidReklama, Otdel
from .models import GurnalSmi, GurnalSocNet, PressRelease, ReklamaSmi, SmiOtdels


class OtdelAdmin(admin.ModelAdmin):
    list_display = ('otdel', 'kontrol')
    list_display_links = ('otdel', 'kontrol')
    # search_fields = ('nom','snils','fam','name','fname','dr')


class SmiOtdelsAdmin(admin.ModelAdmin):
    list_display = ('otdel', 'date_smiotdel')
    list_display_links = ('otdel', 'date_smiotdel')


class PressReleaseAdmin(admin.ModelAdmin):
    list_display = ('name_press', 'temapublik', 'date_press')
    list_display_links = ('name_press',)


class GurnalSmiAdmin(admin.ModelAdmin):
    list_display = ('nsmi', 'vsmi', 'name_publik', 'temapublik', 'vidpublik', 'tonpublik', 'date_publik', 'url_publik')
    list_display_links: str = ('name_publik',)

class GurnalSocNetAdmin(admin.ModelAdmin):
    list_display = ('nsmi', 'vsmi', 'name_publiksn', 'temapublik', 'vidpublik', 'tonpublik', 'date_publiksn', 'url_publiksn')
    list_display_links: str = ('name_publiksn',)


admin.site.register(TemaPublik)
admin.site.register(NameSmi)
admin.site.register(VidSmi)
admin.site.register(TonPublik)
admin.site.register(VidPublik)
admin.site.register(VidMeropriyatia)
admin.site.register(VidReklama)
admin.site.register(Otdel, OtdelAdmin)
admin.site.register(GurnalSmi, GurnalSmiAdmin)
admin.site.register(GurnalSocNet, GurnalSocNetAdmin)
admin.site.register(PressRelease, PressReleaseAdmin)
admin.site.register(ReklamaSmi)
admin.site.register(SmiOtdels, SmiOtdelsAdmin)

# Register your models here.
