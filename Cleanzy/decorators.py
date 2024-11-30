from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect


# Custom check for group membership
def in_group(group_name):
    def check_user_group(user):
        return user.is_authenticated and user.groups.filter(name=group_name).exists()
    return check_user_group

# Apply to your view
@user_passes_test(in_group('Premium Users'))
def my_protected_view(request):
    return render(request, 'my_protected_page.html')

# Redirect unauthorized users (optional)
@user_passes_test(in_group('Premium Users'), login_url='/not-authorized/')
def another_protected_view(request):
    return render(request, 'another_page.html')