from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000

        client = razorpay.Client(
            auth=("rzp_test_2D74VQ8X9S0Sir", "vUTJE4nFOxXZGva7b00wIaR1"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
        return render(request, 'app/index.html',{'payment':payment})
    return render(request, 'app/index.html')

@csrf_exempt
def success(request):
    return render(request, "app/success.html") 


