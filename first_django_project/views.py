from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


def person_info(request, name, age):
    return render(request, 'person_info.html', {'name': name, 'age': age})


def post_example(request):
    post_data = None
    if request.method == 'POST':
        post_data = request.POST.get('data_input')
    return render(request, 'index.html', {'post_data': post_data})


def my_endpoint(request):
    post_message = None

    if request.method == 'POST':
        post_data = request.POST.get('data_input', 'No data provided')
        print("POST data received:", post_data)

        post_message = f"Received POST data: {post_data}"

        return redirect('my-endpoint')

    return render(request, 'endpoint.html', {'post_message': post_message})


