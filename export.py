import csv
import sys
import os
import datetime

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

        # 現在のタイムスタンプを取得 (例: 20240202_123456)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # 出力ファイルのパスを生成
    # CSVファイル名の先頭にタイムスタンプを付与
    output_file_base = os.path.splitext(os.path.basename(csv_file_path))[0]

    output_dir = 'out'
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
        except OSError as e:
            print(f"エラー: ディレクトリ '{output_dir}' の作成に失敗しました。")
            sys.exit(1)

    # 出力ファイルのパスを生成
    output_file_path = os.path.join(output_dir, f"{timestamp}_{output_file_base}.txt")

    # テキストファイルに書き込み
    with open(output_file_path, mode='w', encoding='utf-8') as file:
        file.write(text)

    print(f"ファイルが生成されました: {output_file_path}")

if __name__ == "__main__":
    main()