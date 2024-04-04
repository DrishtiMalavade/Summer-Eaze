import streamlit as st
import speech_recognition as sr

r = sr.Recognizer()

st.set_page_config(page_icon="pages/favicon2.png")
def record_text():
    try:
        with sr.Microphone() as source2:
            st.write("Listening...")
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            return MyText

    except sr.RequestError as e:
        st.write(f"Could not request results; {e}")

    except sr.UnknownValueError as e:
        st.write(f"Unknown error has occurred; {e}")

    return None

def output_text(text):
    if text:
        with open("output.txt", "a") as f:
            f.write(text)
            f.write("\n")
        st.write("Recorded:", text)

def main():
    st.title("Live Transcript Recorder")

    text = record_text()
    if text:
        output_text(text)

if __name__ == "__main__":
    main()
