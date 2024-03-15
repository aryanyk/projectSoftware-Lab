import requests
from flask import Flask, render_template

app = Flask(__name__)

def get_stock_data(symbol):
  api_key = 'BO5DKIE2IIDZTP6W'  # Replace 'YOUR_API_KEY_HERE' with your actual API key
  url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
  response = requests.get(url)
  data = response.json()
  return data['Time Series (Daily)']

# Route to display stock chart on a web page
@app.route('/stock/<symbol>')
def stock_chart(symbol):
  stock_data = get_stock_data(symbol)
  dates = list(stock_data.keys())
  prices = [float(stock_data[date]['4. close']) for date in dates]
  return render_template('stock_chart.html', symbol=symbol, dates=dates, prices=prices)


def get_news():
  api_key = '3fd8f6493ce143ecb8b71534c91622b7'  # Replace 'YOUR_API_KEY' with your actual API key for news API
  url = f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api_key}'
  response = requests.get(url)
  data = response.json()
  return data['articles']

# Route to display news on a webpage
@app.route('/news')
def news_section():
  news_data = get_news()

  return render_template('news.html', news=news_data)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/')
def index():
  return render_template('home.html')

  

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)
