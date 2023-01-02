from nepse_data.automation import Automate

def main(script_name, output_dir):
    automation = Automate(script_name)
    final_df = automation.price_history()

    #filename to save price history
    file_name = script_name+".csv"
    
    #save to data folder
    final_df.to_csv(output_dir + file_name, encoding='utf-8', index=False)
    return("success")

if __name__ == "__main__":
    script_name = "nica"
    output_dir = 'data/'
    main(script_name, output_dir)