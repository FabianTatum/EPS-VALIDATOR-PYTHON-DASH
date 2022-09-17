import glob
import pandas as pd


def extract_xlsx(files_path='./in/*.xlsx'):
    files = glob.glob(files_path)
    df_columns = pd.read_excel(files[0]).columns
    df = pd.DataFrame(columns=df_columns, dtype='object')
    for file in files:
        rows = pd.read_excel(file)
        df = pd.concat([df, rows], ignore_index=True)
    df.to_csv(f'{files_path[:5]}total_rows.csv', index=False)
    df = pd.read_csv(f'{files_path[:5]}total_rows.csv')
    return df