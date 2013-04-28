from django.contrib import admin
from converter.models import Database

class DatabaseAdmin( admin.ModelAdmin ):
    list_display = ('name', 'version', 'username', 'active', 'created_on', )

    class Meta:
        model = Database

admin.site.register( Database, DatabaseAdmin)
