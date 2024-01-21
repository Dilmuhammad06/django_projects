from django.shortcuts import render


def main(request):
    return render(request,'myapp/main.html')

def features(request):
    return render(request,'myapp/features.html')

def pricing(request):
    return render(request,'myapp/pricing.html')
