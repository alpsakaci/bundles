from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Account

@login_required(login_url="/admin/login")
def index(request):
    accounts = Account.get_user_accounts(request.user)
    context = {"accounts": accounts}

    return render(request, "secretpass/index.html", context)