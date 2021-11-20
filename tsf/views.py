from django.shortcuts import render, redirect
from .models import CustomerDetailModel, TransactionDetailModel


# Create your views here.
def home(request):
    return render(request, 'homepage.html')


def customers(request):
    customers = CustomerDetailModel.objects.all()

    if request.method == 'POST':
        email = request.POST.get('email')
        send_email = request.POST.get('send_email')
        amount = request.POST.get('amount')

        try:
            amount = int(amount)
        except:
            pass

        for i in customers:
            if i.email == email:
                j = i
                id = i.id
                break

        for i in customers:
            if i.email == send_email and amount <= i.available_balance and amount >= 0:
                available_balance = i.available_balance - amount
                available_balance2 = j.available_balance + amount

                try:
                    query1 = TransactionDetailModel(
                        name=i.name, email=i.email, debit_amount=amount, credit_amount=0, account_balance=available_balance)
                    query2 = CustomerDetailModel(
                        id=i.id, available_balance=available_balance, email=i.email, name=i.name)
                    query3 = TransactionDetailModel(
                        name=j.name, email=j.email, debit_amount=0, credit_amount=amount, account_balance=available_balance2)
                    query4 = CustomerDetailModel(
                        id=j.id, available_balance=available_balance2, email=j.email, name=j.name)

                    query2.save()
                    query1.save()
                    query4.save()
                    query3.save()

                    return redirect('customers')

                except:
                    print('Transaction Failed')
                    break

            else:
                print("Invalid Data")

    context = {
        'customers': customers
    }

    return render(request, 'customerpage.html', context)


def transactions(request):
    transactions = TransactionDetailModel.objects.all()
    context = {'transactions': transactions}
    return render(request, 'transactionpage.html', context)
