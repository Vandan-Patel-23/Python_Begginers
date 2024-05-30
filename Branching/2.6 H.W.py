address=str(input('Where are you shipping this product to:'))
days=int(input('How soon do you need this product(measured in days):'))
if days==0:
    base_charge=15
    print('Shipping fee will be $',base_charge)
elif days>=1 and days<=3:
    base_charge=10
    print('Shipping fee will be $',base_charge)
elif days>=4 and days<=6:
    base_charge=4.50
    print('Shipping fee will be $',base_charge)
else:
    base_charge=2
    print('Shipping fee will be $',base_charge)
item_weight=float(input('How heavy is your product?(in pounds)'))
if item_weight<0.5:
    charge_per_pound=0.1
    print('Weight fee per pound will be $',charge_per_pound)
elif item_weight>=0.5 and item_weight<=1:
    charge_per_pound=0.15
    print('Weight fee per pound will be $',charge_per_pound)
elif item_weight>=1.1 and item_weight<=3:
    charge_per_pound=0.25
    print('Weight fee per pound will be $',charge_per_pound)
else:
    charge_per_pound=0.40
    print('Weight fee per pound will be $',charge_per_pound)
total_weight_charge= charge_per_pound*item_weight
gift_wrap_charge=0
item_gift_wrapped = str(input('Do you want your gift wrapped?'))
if item_gift_wrapped=='Yes' or item_gift_wrapped=='yes':
    gift_wrap_charge=2.5
    print('Charge for gift wrap will be $',gift_wrap_charge)
print('\n\n\n\t\t\t\t    ExFed')
print('\n\t\t\tSHIPPING FEE:\t\t$',base_charge)
print('\n\t\t\tWEIGHT FEE:\t\t$',total_weight_charge)
print('\n\t\t\tGIFT WRAP FEE:\t\t$',gift_wrap_charge)
print('\n\t\t\tTOTAL:\t\t\t$',base_charge+total_weight_charge+gift_wrap_charge)
print('\n\n\t\t\tACCOUNT #\t\t************9999')
print('\n\t\t\tAPPROVED-PURCHASE')
print('\n\t\t\tSHIPPING TO:\t\t',address)
print('\n\t\t\tARRIVAL IN:',days,'day(s)')
