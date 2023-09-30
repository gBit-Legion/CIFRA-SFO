import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
import warnings


class ApvData:
    def __init__(self, apv_1_file, apv_2_file):
        self.apv_1_file = apv_1_file
        self.apv_2_file = apv_2_file
        self.merged_apv = None
        self.model = None
        self.result = None
        self.predictions = None

    def read_data(self):
        apv_1 = pd.read_csv(self.apv_1_file, usecols=['value'], parse_dates=True)
        apv_2 = pd.read_csv(self.apv_2_file, usecols=['ts'], parse_dates=True)
        self.merged_apv = pd.concat([apv_1, apv_2], axis=1)
        self.merged_apv['ts'] = pd.to_datetime(self.merged_apv['ts']).dt.tz_localize(None)
        self.merged_apv['ts'] = self.merged_apv['ts'].dt.strftime('%Y-%m-%d %H:%M:%S')
        self.merged_apv.set_index('ts', inplace=True)
        self.merged_apv = self.merged_apv.dropna()

    def build_model(self):
        warnings.simplefilter(action='ignore', category=Warning)
        self.model = SARIMAX(self.merged_apv, order=(2, 0, 0), seasonal_order=(2, 1, 0, 50))
        self.result = self.model.fit()

    def make_predictions(self):
        start = len(self.merged_apv)
        end = len(self.merged_apv) + len(self.merged_apv) - 1
        self.predictions = self.result.predict(start, end)
        return self.predictions, self.merged_apv
