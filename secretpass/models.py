from django.db import models
from django.contrib.auth.models import User
from .crypto import encrypt_password, decrypt_password


class Account(models.Model):
    owner = models.ForeignKey(User, related_name="account", on_delete=models.CASCADE)
    service = models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    password = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(Account, self).save(*args, **kwargs)

    @staticmethod
    def create(owner, service, username, password):
        account = Account.objects.create(
            owner=owner, service=service, username=username, password=encrypt_password(password)
        )
        account.save()

        return account

    @staticmethod
    def get_user_accounts(user):
        return (
            Account.objects.filter(owner=user, is_deleted=False)
            .order_by("date_created")
            .reverse()
        )

    @staticmethod
    def search_account(user, query):
        return Account.objects.filter(
            models.Q(owner=user)
            & models.Q(is_deleted=False)
            & (models.Q(service__icontains=query) | models.Q(username__icontains=query))
        )

    def __str__(self):
        return (
            "["
            + self.owner.username
            + "] - "
            + self.service
            + " - "
            + self.username
            + " - "
            + self.password
        )
