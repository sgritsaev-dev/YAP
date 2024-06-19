from django.shortcuts import render


def ice_cream_detail(request, pk):
    template = 'ice_cream/detail.html'
    return render(request, template)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    return render(request, template)