from django.http import HttpResponse


def home(request):
    return HttpResponse('welcome to my world')


def odd(request):
    x = 12
    if x % 2 == 0:
        return HttpResponse('even number')
    else:
        return HttpResponse('odd number')


def biggest(request):
    x = 12
    y = 130
    z = 30
    v = x if x > y and x > z else (z if z > x and z > y else y)
    return HttpResponse(f'the big number is {v}')


def prime(request):
    x = 97
    v = 1
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                v = 0
                break
    if v:
        return HttpResponse('prime number')
    else:
        return HttpResponse('Not prime number')


def fabinocis(request):
    x = 10
    a, b = 0, 1
    list = []
    for i in range(x):
        c = a + b
        list.append(a)
        a = b
        b = c

    return HttpResponse(f'{x} fabinocis number is {list}')


def amstrong(request):
    x = 153
    s = [int(i)**3 for  i in str(x)]
    s = sum(s)
    if x == s:
        return HttpResponse('its amstrong number')
    else:
        return HttpResponse('its not amstrong number')


def evennumber(request):
    list1 = [12,34,45,56,78,9,54]
    list2 = []
    for i in list1:
        if i%2==0:
            list2.append(i)
    return HttpResponse(f'{list2}')


def evenindex(request):
    list1 = [12,34,45,56,78,9,54]
    list2 = []
    for i in range(0,len(list1),2):
        list2.append(list1[i])
    return HttpResponse(f'even index numbers : {list2}')