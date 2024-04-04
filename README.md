# Ex.05 Design a Website for Server Side Processing
## Date:02-04-2024

## AIM:
To design a website to find surface area of a Right Cylinder in server side.

## FORMULA:
Surface Area = 2Πrh + 2Πr<sup>2</sup>
<br>r --> Radius of Right Cylinder
<br>h --> Height of Right Cylinder

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html

<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Surface Area</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <style type="text/css">
        body {
            background-color: violet;
        }
        .edge {
            width: 100%;
            max-width: 1440px;
            margin: 0 auto;
            padding-top: 250px;
            padding-left: 300px;
        }
        .box {
            border: thick dashed blue;
            width: 500px;
            min-height: 300px;
            font-size: 20px;
            background-color: blue;
            padding: 20px;
            box-sizing: border-box;
        }
        .formelt {
            color: yellowgreen;
            text-align: center;
            margin-top: 7px;
            margin-bottom: 6px;
        }
        h1 {
            color: rgb(255, 0, 179);
            text-align: center;
            padding-top: 20px;
        }
        .input-container {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="edge">
        <div class="box">
            <h1>Surface Area of Right Cylinder</h1>
            <form method="POST">
                {% csrf_token %}
                <div class="input-container">
                    <div class="formelt">
                        Radius : <input type="text" name="radius" value="{{ r }}"></input>(in m)
                    </div>
                </div>
                <div class="input-container">
                    <div class="formelt">
                        Height : <input type="text" name="height" value="{{ h }}"></input>(in m)
                    </div>
                </div>
                <div class="formelt">
                    <input type="submit" value="Calculate"></input>
                </div>
                <div class="formelt">
                    Area : <input type="text" name="area" value="{{ area }}"></input>m<sup>2</sup>
                </div>
            </form>
        </div>
    </div>
</body>
</html>
```
```
views.py

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

```
```
urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('surfacearea/', views.surfacearea, name="surfacearea"),
    path('', views.surfacearea, name="surfacearearoot")
]
```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot 2024-04-04 214148.png>)

## HOMEPAGE:
![alt text](<Screenshot 2024-04-04 214116.png>)

## RESULT:
The program for performing server side processing is completed successfully.
