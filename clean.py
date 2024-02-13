import pandas as pd
import argparse

def cleaning(input1,input2,output):
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
    merge_data = pd.merge(df1,df2,left_on="respondent_id", right_on="id")
    merge_data = merge_data.dropna()
    merge_data = merge_data[~merge_data['job'].str.contains('insurance|Insurance')]
    merge_data.drop('id', axis=1, inplace=True)
    merge_data.to_csv(output, index=False)

    file_shape = merge_data.shape
    print("Output file shape:", file_shape)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input1", help="respondent_contact")
    parser.add_argument("input2", help="respondent_other")
    parser.add_argument("output", help="output file")
    args = parser.parse_args()
    cleaning(args.input1, args.input2, args.output)