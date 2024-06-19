from django.shortcuts import render


def test_rendering(request):
    template = 'catalog/block_content_rendered.html'
    return render(request, template)