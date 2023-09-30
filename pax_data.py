import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

class PaxData:
    def __init__(self, filename):
        self.filename = filename
        self.pax = None
        self.slices = None
        self.slices_count = None

    def read_data(self):
        self.pax = pd.read_csv(self.filename, usecols=['ts', 'pax_arrival_profile'], parse_dates=True)
        self.pax['ts'] = pd.to_datetime(self.pax['ts']).dt.tz_localize(None)
        self.pax['ts'] = self.pax['ts'].dt.strftime('%Y-%m-%d %H:%M:%S')
        self.pax.set_index('ts', inplace=True)

    def slice_data(self, slice_size=300):
        self.slices = [self.pax[i:i + slice_size] for i in range(0, len(self.pax), slice_size)]
        self.slices_count = len(self.slices)

    def fit_model(self, i):
        model = SARIMAX(self.slices[i], order=(2, 0, 0), seasonal_order=(2, 1, 0, 50))
        result = model.fit()
        return result

    def predict(self, result, i):
        start = len(self.slices[i])
        end = len(self.slices[i]) + len(self.slices[i + 1]) - 1
        predictions = result.predict(start, end)
        df_predictions = self.slices[i + 1].copy()
        predictions.index = df_predictions.index
        df_predictions['pax_arrival_profile'] = predictions
        return df_predictions, self.slices