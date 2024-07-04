from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import requests


# Create your views here.

def home(request):
    return render(request, 'home.html')

def iniciosesion(request):
    return render(request, 'iniciosesion.html')

def principal(request):
    return render(request, 'principal.html')

def footer(request):
    return render(request, 'footer.html')

def head(request):
    return render(request, 'head.html')


def catalogo(request):
    response = requests.get('http://127.0.0.1:8000/api/items/')
    if response.status_code == 200:
        items = response.json()
    else:
        items = []
    return render(request, 'catalogo.html', {'items': items})

def carrito(request):
    response = requests.get('http://127.0.0.1:8000/api/items/')
    if response.status_code == 200:
        items = response.json()
    else:
        items = []
    return render(request, 'carrito.html', {'items': items})

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('principal')
            except IntegrityError:
                return render(request, 'register.html', {
                    'form': UserCreationForm,
                    'error': 'Cuenta ya existente'
                })
        return render(request, 'register.html', {
            'form': UserCreationForm,
            'error': 'Contraseña no coinciden'
        })

def signout(request):
    logout(request)
    return redirect('principal')

def iniciosesion(request):
    if request.method == 'GET':
        return render(request, 'iniciosesion.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciosesion.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña es incorrecta'
            })
        else:
            login(request, user)
            return redirect('principal')
        
@login_required
def admin_panel(request):
    response = requests.get('http://127.0.0.1:8000/api/items/')
    if response.status_code == 200:
        products = response.json()
    else:
        products = []
    return render(request, 'admin.html', {'products': products})

@login_required
def product_admin_view(request):
    return render(request, 'admin.html')

@login_required
def manage_products(request, product_id=None):
    headers = {'Content-Type': 'application/json'}

    if request.method == 'GET':
        if product_id:
            response = requests.get(f'http://127.0.0.1:8000/api/items/{product_id}/')
            if response.status_code == 200:
                product = response.json()
                return JsonResponse(product)
            return JsonResponse({'error': 'Producto no encontrado'}, status=404)
        else:
            response = requests.get('http://127.0.0.1:8000/api/items/')
            if response.status_code == 200:
                products = response.json()
                return JsonResponse(products, safe=False)
            return JsonResponse({'error': 'Error al obtener los productos'}, status=500)

    elif request.method == 'POST':
        data = {
            'nombre': request.POST.get('nombre'),
            'descripcion': request.POST.get('descripcion'),
            'precio': request.POST.get('precio')
        }
        files = {'imagen': request.FILES.get('imagen')}
        response = requests.post('http://127.0.0.1:8000/api/items/', data=data, files=files, headers=headers)
        if response.status_code == 201:
            return JsonResponse({'status': 'Producto creado'}, status=201)
        return JsonResponse({'error': 'Error al crear el producto'}, status=response.status_code)

    elif request.method == 'PUT':
        data = {
            'nombre': request.POST.get('nombre'),
            'descripcion': request.POST.get('descripcion'),
            'precio': request.POST.get('precio')
        }
        files = {'imagen': request.FILES.get('imagen')} if 'imagen' in request.FILES else None
        response = requests.put(f'http://127.0.0.1:8000/api/items/{product_id}/', data=data, files=files, headers=headers)
        if response.status_code == 200:
            return JsonResponse({'status': 'Producto actualizado'})
        return JsonResponse({'error': 'Error al actualizar el producto'}, status=response.status_code)

    elif request.method == 'DELETE':
        response = requests.delete(f'http://127.0.0.1:8000/api/items/{product_id}/', headers=headers)
        if response.status_code == 204:
            return JsonResponse({'status': 'Producto eliminado'})
        return JsonResponse({'error': 'Error al eliminar el producto'}, status=response.status_code)
