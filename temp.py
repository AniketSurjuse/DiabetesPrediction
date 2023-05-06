import pickle
pkl_file = open("bengaluru_house_prices_model.pickle", "rb")
model = pickle.load(pkl_file)
pkl_file.close()
