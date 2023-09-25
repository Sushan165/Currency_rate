from django.shortcuts import render

def home(request):
    if request.GET.get("c") and request.GET.get("target") and request.GET.get("num"):
        c = request.GET.get("c")
        target = request.GET.get("target")
        num = float(request.GET.get("num"))
        
        # Specify the base currency and its rates
        if c == "BTC":
            base_currency = "BTC"
            rates = {
                "IND": 2206024.17 * num ,
                "USD": 26684.60 * num,
                "RUB": 2559720.25 * num
            }
        elif c == "ETH":
            base_currency = "ETH"
            rates = {
                "IND": 2206024.17 * num,
                "USD": 26684.60 * num,
                "RUB": 153133.86 * num
            }
        else:
            base_currency = "XRP"
            rates = {
                "IND": 42.54 * num,
                "USD": 0.51 * num,
                "RUB": 49.26 * num
            }
        
        # Get the conversion rate for the target currency
        converted_amount = rates.get(target, None)
        if converted_amount is not None:
            msg = f"{c} to {target}: {converted_amount}"
        else:
            msg = "Invalid target currency"
        
        return render(request, "home.html", {"msg": msg})
    else:
        return render(request, "home.html")
