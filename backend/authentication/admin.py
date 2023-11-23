from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as OriginalUserAdmin
from authentication.models import Person
from django.contrib.auth.models import User

class UserAdmin(OriginalUserAdmin):
    # Sobrescreva o método 'add_fieldsets' para incluir 'groups', 'is_active', 'is_superuser' e 'user_permissions'
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_active', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

class GroupAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']


class PersonAdmin(admin.ModelAdmin):
    list_display = ['user', 'saldo']  # os campos que você deseja mostrar na lista
    search_fields = ['user__username', 'saldo']  # campos que podem ser pesquisados
    list_filter = ['saldo'] 


admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
# Desregistre o admin original de User e registre o novo
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Person, PersonAdmin)
