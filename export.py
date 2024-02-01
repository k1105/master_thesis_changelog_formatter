import csv
import sys
import os

def convert_csv_to_text(csv_file_path):
    # CSVファイルを開いてデータを読み込む
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)


    formatted_text = []
    current_number = None
    count = 0

    for row in data:
        if current_number != row['修正指示番号']:
            current_number = row['修正指示番号']
            count = 1
        else:
            count += 1

        formatted_text.append(f"## 修正{row['修正指示番号']}-{count}\n")
        formatted_text.append(f"**修正箇所**：{row['修正箇所']}\n")
        formatted_text.append(f"**修正前**：{row['修正前']}\n")
        formatted_text.append(f"**修正後**：{row['修正後']}\n")
        formatted_text.append(f"**修正の理由**：{row['修正理由']}\n")
        formatted_text.append("\n\n\n")

    # リストを文字列に変換
    final_text = "\n".join(formatted_text)

    return final_text

def main():
    # コマンドライン引数からCSVファイルのパスを取得
    if len(sys.argv) != 2:
        print("使用方法: python main.py [CSVファイルのパス]")
        sys.exit(1)

    csv_file_path = sys.argv[1]

    # CSVファイルをテキストに変換
    text = convert_csv_to_text(csv_file_path)

    # 出力ファイルのパスを生成 (CSVファイルと同じ名前で.txt拡張子)
    output_file_path = os.path.splitext(csv_file_path)[0] + '.txt'

    # テキストファイルに書き込み
    with open(output_file_path, mode='w', encoding='utf-8') as file:
        file.write(text)

    print(f"ファイルが生成されました: {output_file_path}")

if __name__ == "__main__":
    main()
