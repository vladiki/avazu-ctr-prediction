import pandas as pd

def load_df(filename):
    df = pd.read_csv(filename, header=0)
    df = df.drop(['site_id', 'app_id', 'device_id', 'device_ip', 'site_domain',
                  'site_category', 'app_domain', 'app_category', 'device_model'], axis=1)
    return df