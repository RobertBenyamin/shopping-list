from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Robert Benyamin',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
