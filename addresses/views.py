from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from addresses.models import Building
from django.db.models import Q
from .forms import *


def full_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            addresses_list = []
            addresses_ids = []
            address = form.cleaned_data['address']
            try:
                exact_address = Building.objects.get(Q(full_address=address) | Q(short_address=address))
                addresses_list.append(exact_address.full_address)
                addresses_ids.append(exact_address.id)
            except ObjectDoesNotExist:
                address = address.split(",")
                #Нейронка


            result = dict(zip(addresses_list,addresses_ids))
            return render(request, 'full_address.html', {'form': form, 'result': result})
    else:
        form = AddressForm()
        return render(request, 'full_address.html', {'form': form})
