from django import forms

TICKER_CHOICES=(
    ("1", " "),
    ("2", "Apple"),
    ("3", "Microsoft"),
    ("4", "Google"),
)

class TickerForm(forms.Form):
    company = forms.ChoiceField(choices=TICKER_CHOICES,
                                    widget=forms.Select(attrs={'onchange': 'tickerform.submit();'}))
    
class BuyForm(forms.Form):
    buy_quantity = forms.IntegerField()