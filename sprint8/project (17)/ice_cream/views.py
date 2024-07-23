from django.shortcuts import get_object_or_404, render

from ice_cream.models import IceCream


def ice_cream_detail(request, pk):
    template_name = 'ice_cream/detail.html'
    ice_cream = get_object_or_404(
<<<<<<< HEAD
        IceCream.objects.filter(is_published=True, category__is_published=True),
=======
        IceCream.objects.values(
            'title', 'description'
        ).filter(is_published=True),
>>>>>>> 632c33d309d7e0d6f2eb13f5dbd36bb5e0f4f1e7
        pk=pk
    )
    context = {
        'ice_cream': ice_cream,
    }
    return render(request, template_name, context)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
<<<<<<< HEAD
    ice_cream_list = IceCream.objects.select_related('category').filter(
        is_published=True,
        category__is_published=True
    ).order_by('category')

    context = {'ice_cream_list': ice_cream_list}
=======
    context = {}
>>>>>>> 632c33d309d7e0d6f2eb13f5dbd36bb5e0f4f1e7
    return render(request, template, context)