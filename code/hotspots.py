import pandas as pd
import logging
import data_simulator as ds

logging.basicConfig(level=logging.DEBUG)

def run_data_simulator():
    ds.main()
    
def read_data(fname):
    logging.info("Reading File")
    df = pd.read_csv(fname)
    return df.drop_duplicates()
    
def calculate_deviations(df, speed_dict):
    logging.debug("Calculating")
    deviations = df.apply(lambda x: speed_dict['deviceCode_pyld_speed'][x['deviceCode_pyld_alarmType']] - x['deviceCode_pyld_speed'], axis=1)
    df['hotspot_magnitude'] = deviations
    return df

def main():
    
    #Running Data Simulator
    run_data_simulator()
    
    #Reading Data
    df = read_data('Bangalore-CAS-alerts/bangalore-cas-alerts.csv')
    
    #Constructing Empty dataframe
    deviated_df = pd.DataFrame()
    
    ward_names = pd.unique(df['deviceCode_location_wardName'])
    
    logging.info("Calculating Deviations for each ward")
    
    """
    For each ward, calculating mean vehicle speed for respective alarm type and calculating deviation of 
    each record/input   based on the mean values.
    """
    for ward in ward_names:
        df_ = df[df['deviceCode_location_wardName']==ward]
        speed_dict = df_[['deviceCode_pyld_alarmType', 'deviceCode_pyld_speed']].groupby('deviceCode_pyld_alarmType').agg('mean').to_dict()
        temp = calculate_deviations(df_, speed_dict)
        deviated_df = deviated_df.append(calculate_deviations(df_, speed_dict))
    
    #Scaling data 0-100
    deviated_df['hotspot_magnitude'] *= 100.0/deviated_df['hotspot_magnitude'].min()
    deviated_df['hotspot_magnitude'] = deviated_df['hotspot_magnitude'].apply(lambda x: x if x>0 else 0)
    
    #Rating behaviour of Drivers 0-10
    rating = deviated_df[['deviceCode_deviceCode',  'hotspot_magnitude']].groupby('deviceCode_deviceCode').agg('mean').reset_index()
    rating['hotspot_magnitude'] *= 10.0/rating['hotspot_magnitude'].max()
    rating['hotspot_magnitude'] = 10 - rating['hotspot_magnitude']
    
    #Exporting
    logging.info("Exporting...")
    deviated_df.to_csv('hotspots.csv', index=False)
    rating.to_csv('rating.csv', index=False)
    
if __name__ == '__main__':
    main()