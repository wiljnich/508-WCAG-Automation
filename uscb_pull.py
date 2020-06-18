import requests
import pandas as pd

def main():
    cws = pd.read_csv('data/cws.csv')
    sc = pd.read_csv('data/state_codes.csv',  converters={'State Code': lambda x: str(x)})
    cc = pd.read_csv('data/county_codes.csv',  converters={'County Code': lambda x: str(x),'State Code': lambda x: str(x) })
    temp = cws['Counties Served'].str.split(',').apply(pd.Series, 1).stack()
    temp.index = temp.index.droplevel(-1)
    temp.name = 'Counties Served'
    del cws['Counties Served']
    cws = cws.join(temp)
    cws = pd.merge(sc, cws.rename(columns={'Primacy Agency':'State Name'}), on='State Name',  how='right')
    cws = pd.merge(cc, cws.rename(columns={'Counties Served':'Name'}), on= ['State Code','Name'],  how='right')
    
    a = cws['State Code'].tolist()
    b = cws['County Code'].tolist()
    total = []
    esl = []
    for x, y in zip(a,b):
        try:
            total.append(requests.get("https://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=county:"+y+"&in=state:"+x+"&LAN7=1")
                         .json()[1][0])
            esl.append(requests.get("https://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=county:"+y+"&in=state:"+x+"&LAN7=3")
                       .json()[1][0])
        except:
            total.append(0)
            esl.append(0)

    cws['Total'] = pd.Series(total).values.astype(int)
    cws['ESL'] = pd.Series(esl).values.astype(int)
    cws['Ratio'] = test['Total']/test['ESL']

    cws.to_csv('access_report_results.csv', encoding='utf-8')

if __name__ == "__main__":
    main()