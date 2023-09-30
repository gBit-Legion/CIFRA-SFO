from pax_data import PaxData
import warnings
warnings.simplefilter(action='ignore', category=Warning)

pax_data = PaxData("arrival_profile_data.csv")
pax_data.read_data()
pax_data.slice_data()

for i in range(3):
    result = pax_data.fit_model(i)
    df_predictions = pax_data.predict(result, i+1)
    print(df_predictions)