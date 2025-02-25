# YouTube 字幕取得アプリ

このアプリは、Streamlit と youtube-transcript-api を利用して、
入力された YouTube 動画の URL から字幕を取得し、表示する Web アプリです。

## セットアップ方法

1. **リポジトリをクローン（またはコードをダウンロード）**
2. **仮想環境の作成・有効化**
   - Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
3. **依存パッケージのインストール**
   ```bash
   pip install -r requirements.txt
