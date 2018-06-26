import urllib.request


URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=1min&apikey=1KHURQ9BHAVA20QT&datatype=csv'
# URL = 'https://finance.yahoo.com/quote/?s={}=X&f=p'
# https://finance.yahoo.com/quote/MXN=X?p=MXN=X


def get_rate(pair,  url_tmplt=URL):
    with urllib.request.urlopen(url_tmplt.format(pair)) as res:
    # with urllib.request.urlopen(url_tmplt.format()) as res:
        body = res.read()
        body = str(body.strip()).split(',')
    # outq.put((pair, float(body.strip())))
    return(pair, float(body[9]))
