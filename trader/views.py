from django.shortcuts import render
import yfinance as yahooFinance
import plotly.express as px
from .forms import TickerForm
from .models import Shares




def index(request):
    form = TickerForm(request.GET or None)




    aapl_close = yahooFinance.download("AAPL", period="1y", actions=True).Close
    aapl_last_quote = round(aapl_close.iloc[-1], 2)
    aapl_date = aapl_close.index
    aapl_x_data = aapl_date
    aapl_y_data = aapl_close
    fig_appl = px.line(
        x=aapl_x_data,
        y=aapl_y_data,   
    ).update_layout(title_text="Apple", title_x=0.5, xaxis_title="date", yaxis_title="close price", width=500, height=350, plot_bgcolor='#E6E3E6',
        paper_bgcolor="#ECEDE8", font=dict(family="Noto Sans, sans-serif", color="#3C3E58"),
    ).update_traces(line_color ='#56A25D')
    appl_chart = fig_appl.to_html()

    msft_close = yahooFinance.download("MSFT", period="1y", actions=True).Close
    msft_last_quote = round(msft_close.iloc[-1], 2)
    msft_date = msft_close.index
    msft_x_data = msft_date
    msft_y_data = msft_close
    fig_msft = px.line(
        x=msft_x_data,
        y=msft_y_data,
    ).update_layout(title_text="Microsoft", title_x=0.5,xaxis_title="date", yaxis_title="close price", width=500,height=350, plot_bgcolor='#E6E3E6',
        paper_bgcolor="#ECEDE8", font=dict(family="Noto Sans, sans-serif", color="#3C3E58")
    ).update_traces(line_color ='#56A25D')
    
    msft_chart = fig_msft.to_html()

    goog_close = yahooFinance.download("GOOG", period="1y", actions=True).Close
    goog_last_quote = round(goog_close.iloc[-1], 2)
    goog_date = goog_close.index
    goog_x_data = goog_date
    goog_y_data = goog_close
    fig_goog = px.line(
        x=goog_x_data,
        y=goog_y_data,
        
    ).update_layout(title_text="Google", title_x=0.5, xaxis_title="date", yaxis_title="close price",width=500, height=350, plot_bgcolor='#E6E3E6',
                    paper_bgcolor="#ECEDE8", font=dict(family="Noto Sans, sans-serif", color="#3C3E58")
    ).update_traces(line_color ='#56A25D')
    
    goog_chart = fig_goog.to_html()


    shares_list = []
    apple_share = Shares(share_name = "AAPL", share_quantity=0,  shares_owned=0, 
                total_price=0 , share_price= aapl_last_quote )
    microsoft_share = Shares(share_name = "MSFT", share_quantity=0,  shares_owned=0, 
                total_price=0, share_price= msft_last_quote )
    google_share = Shares(share_name = "GOOG", share_quantity=0,  shares_owned=0, 
                total_price=0, share_price= goog_last_quote )
    
    shares_list.append(apple_share)
    shares_list.append(microsoft_share)
    shares_list.append(google_share)

    
    
    



    if request.method == "GET" and form.is_valid():  # Check if form is submitted and valid
        ticker = form.cleaned_data["company"]

        if ticker == "2":
            return render(request, 'index.html', {'aapl_plot_div': appl_chart, "aapl_last_quote":aapl_last_quote, 
                                        "msft_last_quote":msft_last_quote,
                                        "goog_last_quote":goog_last_quote,
                                        "form":form, "shares":shares_list})
        elif ticker == "3":
            return render(request, 'index.html', {'msft_plot_div': msft_chart, "aapl_last_quote":aapl_last_quote, 
                                        "msft_last_quote":msft_last_quote,
                                        "goog_last_quote":goog_last_quote,
                                        "form":form,"shares":shares_list})
        elif ticker == "4":
            return render(request, 'index.html', {'goog_plot_div': goog_chart,"aapl_last_quote":aapl_last_quote, 
                                        "msft_last_quote":msft_last_quote,
                                        "goog_last_quote":goog_last_quote,
                                        "form":form,"shares":shares_list})

        
        

    return render(request, 'index.html', {
                                        "aapl_last_quote":aapl_last_quote, 
                                        "msft_last_quote":msft_last_quote,
                                        "goog_last_quote":goog_last_quote,
                                        "form":form,"shares":shares_list})


