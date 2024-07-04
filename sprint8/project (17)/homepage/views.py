from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template_name = "homepage/index.html"
    ice_cream_list = (
        IceCream.objects.values('wrapper__title', "id", "title", "description")
        .filter(is_published__exact=True, is_on_main__exact=True, category__is_published=True)
        .order_by("title")[0:3]
    )
    context = {
        "ice_cream_list": ice_cream_list,
    }
    return render(request, template_name, context)
