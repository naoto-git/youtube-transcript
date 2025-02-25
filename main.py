import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import re

def get_video_id(url):
    """
    YouTube の URL から動画IDを抽出する関数
    """
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

def get_youtube_transcript(youtube_url, language=["ja"], translation=None):
    """
    指定された YouTube URL の字幕を取得する関数
    ※ translation 引数は、後で翻訳機能を追加するためのプレースホルダです
    """
    video_id = get_video_id(youtube_url)
    if video_id is None:
        return "無効な YouTube URL です。"
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=language)
        transcript_text = "\n".join([item["text"] for item in transcript_list])
        return transcript_text
    except Exception as e:
        return f"字幕取得中にエラーが発生しました: {str(e)}"

def main():
    st.title("YouTube 字幕取得アプリ")
    st.write("YouTube の URL を入力して、動画の字幕を取得します。")
    
    url = st.text_input("YouTube 動画の URL を入力してください")
    if url:
        transcript_text = get_youtube_transcript(youtube_url=url, language=["ja"], translation=None)
        st.subheader("取得した字幕")
        st.text_area("字幕", transcript_text, height=400)

if __name__ == "__main__":
    main()
