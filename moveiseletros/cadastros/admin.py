from django.contrib import admin
from .models import Endereco, Cliente
from .models import Funcionario
from .models import Mercadoria

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import UserChangeFormAdmin, UserCreationForm

from .models import CustomUser

# Register your models here.

admin.site.register(Endereco)
admin.site.register(Funcionario)
admin.site.register(Mercadoria)
admin.site.register(Cliente)


@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('cpf', 'password')}),
        (u'Informacoes pessoais', {'fields': ('full_name', 'email', 'type')}),
        (u'Permissoes', {'fields': ('is_staff', 'is_active', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cpf', 'full_name', 'email', 'type', 'password1', 'password2')
        }),
    )
    form = UserChangeFormAdmin
    add_form = UserCreationForm
    list_display = ('cpf', 'full_name', 'email', 'type', 'is_staff')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('cpf', 'email')
    ordering = ('cpf', 'email')
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.unregister(Group)
