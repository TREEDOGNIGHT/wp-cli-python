from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def users(request):
    a = ['asd', 'ddd', '244']

    return render(
        request,
        'users/users.html',
        {
            'data': a
        }
    )



def groups(request):

    a = ['asd', 'ddd', '244']

    return render(
        request,
        'users/groups.html',
        {
            'data': a
        }
    )
