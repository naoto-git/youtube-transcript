import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import re

@st.cache_data(show_spinner=False)
def get_transcript(video_id, languages):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
    # 各字幕セグメント内の改行をスペースに置換し、セグメント間はスペースで結合
    transcript_text = " ".join([item["text"].replace("\n", " ") for item in transcript_list])
    return transcript_text

def get_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

def get_youtube_transcript(youtube_url, languages=["ja", "en"]):
    video_id = get_video_id(youtube_url)
    if video_id is None:
        return "無効な YouTube URL です。"
    try:
        transcript_text = get_transcript(video_id, languages)
        return transcript_text
    except Exception as e:
        return f"字幕取得中にエラーが発生しました: {str(e)}"

def main():
    st.title("YouTube 字幕取得")
    st.write("YouTube の URL を入力して、動画の字幕を取得します。")
    
    url = st.text_input("YouTube 動画の URL を入力してください")
    if st.button("字幕取得"):
        transcript_text = get_youtube_transcript(youtube_url=url, languages=["ja", "en"])
        st.subheader("取得した字幕")
        # カスタムCSSを注入して、コードブロックの自動折返しを解除
        st.markdown(
            """
            <style>
            .stCodeBlock pre {
                white-space: nowrap;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.code(transcript_text, language="plaintext")

if __name__ == "__main__":
    main()
