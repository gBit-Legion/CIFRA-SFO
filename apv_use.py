from apv_data import ApvData

model = ApvData("arrival_profile_value.csv", "arrival_profile_data.csv")
model.read_data()
model.build_model()
model.make_predictions()
model.plot_predictions()