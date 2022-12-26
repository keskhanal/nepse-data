from nepse_data import Automate

automation = Automate("nica")

final_df = automation.price_history()

file_name = "test.csv"
final_df.to_csv("data/" + file_name, encoding='utf-8', index=False)