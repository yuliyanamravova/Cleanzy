from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect


# Custom check for group membership
def in_group(group_name):
    def check_user_group(user):
        return user.is_authenticated and user.groups.filter(name=group_name).exists()
    return check_user_group
