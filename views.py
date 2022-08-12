from django.shortcuts import render, redirect


def main_page(request):
    return render(request, 'index.html')


def resume(request):
    return render(request, 'resume.pdf')
