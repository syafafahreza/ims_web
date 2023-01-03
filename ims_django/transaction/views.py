from django.shortcuts import render
from django.contrib.auth.decorators import *


# Create your views here.
@login_required(login_url='login')
@permission_required('transaction.view_transaction_history')
def transaction_view(request):
    '''
        Return transaction history page.
    '''
    page_title = 'Transaction'
    context = {'title': page_title}
    return render(request, 'transaction.html', context)
