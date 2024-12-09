from django.contrib.auth.models import Group
from Cleanzy.accounts.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def add_user_to_basic_group(sender, instance, created, **kwargs):
    if created:  # Only add the user to the group when the user is created
        group, created = Group.objects.get_or_create(name='Authorized User')
        instance.groups.add(group)
