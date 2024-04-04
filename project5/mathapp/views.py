from django.shortcuts import render

def surfacearea(request):
    context = {}
    context['area'] = "0"
    context['r'] = "0"
    context['h'] = "0"

    if request.method == 'POST':
        print("POST method is used")
        r = request.POST.get('radius', '0')
        h = request.POST.get('height', '0')
        print('Radius=', r)
        print('Height=', h)

        try:
            r = float(r)
            h = float(h)
            area = (2 * 3.14159 * r * h) + (2 * 3.14159 * r * r)
            context['area'] = round(area, 2)
            context['r'] = str(r)
            context['h'] = str(h)
            print('Area=', area)
        except ValueError:
            print('Invalid input for radius or height.')

    return render(request, 'mathapp/math.html', context)
