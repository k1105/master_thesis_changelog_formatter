### Abstract
修論の修正をスプレッドシート上で管理しておくと、所定の形式でエクスポートしてくれるよ

### Usage
1. ``sample.csv``の形式でcsvファイルを作成。google spreadsheet上で作成した場合は、「ファイル -> ダウンロード -> .csv形式」を選択
2. このフォルダ直下（sample.csv）と同じ階層にcsvファイルを置く
3. ``python export.py (ファイル名).csv``を実行
4. ``out``ディレクトリ内に、``(タイムスタンプ)_(csvのファイル名).txt``ファイルが作成されている。マークダウン形式で記述されているので、マークダウンが読み込めるエディタ（notionなど）に貼り付けると、スタイル情報が復元される。
5. スタイルが復元されたテキストを、お好きなエディタで編集。

### Option
``export.py``は、スプレッドシート上の「修正指示番号」列の番号に基づき、「1-1」、「1-2」、「1-3」と、修正指示番号が同じものをグルーピングして連番で出力するもの。

``export_ignore_index.py``は、「修正指示番号」列を無視して、純粋に連番の見出しをつけて出力するもの。
