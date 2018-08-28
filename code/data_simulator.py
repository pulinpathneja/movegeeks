import pandas as pd
import logging
import time, datetime

logging.basicConfig(level=logging.INFO)

COLUMNS = None
def read_data():
    global COLUMNS
    df = pd.read_csv('Bangalore-CAS-alerts/bangalore-cas-alerts.csv')
    df = df.drop_duplicates()
    
    COLUMNS = df.columns
    return df

def data_generator():
    df = read_data()
    for row in df.iloc[:10,:].values:
        row[-1] = str(datetime.datetime.now())
        time.sleep(1)
        logging.info({k:v for k, v in zip(COLUMNS,row)})
        yield row
        
def main():
    df = pd.DataFrame()
    df = df.from_records([row for row in data_generator()], columns=COLUMNS)
    #print df.head()
    df.to_csv('data_constructed.csv', index=False)

if __name__ == '__main__':
    main()
