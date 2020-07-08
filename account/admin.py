from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Fields',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'role',
                ),
            },
        ),
    )


admin.site.register(Account, CustomUserAdmin)
