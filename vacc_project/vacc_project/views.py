from django.shortcuts import render

def about(request):
   return render(request, 'about.html')

def help_page(request):
   return render(request, 'help.html')
