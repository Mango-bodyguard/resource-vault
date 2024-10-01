import os
import csv

def create_folders_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            folder_path = os.path.join(*row)
            try:
                os.makedirs(folder_path, exist_ok=True)
                print(f'フォルダ "{folder_path}" を作成しました。')
            except Exception as e:
                print(f'フォルダ "{folder_path}" の作成に失敗しました: {e}')

if __name__ == "__main__":
    csv_file_path = input("フォルダ階層を指定したCSVファイルのパスを入力してください: ")
    create_folders_from_csv(csv_file_path)