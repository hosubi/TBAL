# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.header('T발 사랑해 :red[AICOPY]', divider='rainbow')

st.write('AICOPY 입니다 AI연코.:small_airplane:')
st.write('T도 사랑하자!.:exclamation:')

       
content = st.text_input('주제 입력 :memo:,오늘 너무 좋았어! 형식으로 입력!:satellite: 사랑은 응원합니다!')
prompt = '''너 이름은 'T발 사랑해'야!
MBTI에서 T 성향은 감정적인 대화를 못하는 편이야!
T성향을 가진 친구에게 감정적인 대화를 잘 알려줄 수 있어!
문장을 이야기하면 심리적으로 매력적인 대화로 번역 해줘! 
(짧고 유머러스하고 감동적인 문장으로 변경!이모티콘도 넣어줘!)


답변 양식 
( T발사랑해♥ 

1.
2. 
3. 

) 으로 해줘! (1줄 1답 + 3가지!)

주제 : '''


if st.button('T사랑 언어 번역!'):
    with st.spinner('정성스럽게 작성중! 시간이 걸릴 수 있습니다...'):
        result = chat_model.predict( prompt + content )
        st.write(result)

  


st.link_button("토스후원하기, :passenger_ship:", "https://toss.me/aicopy")
st.link_button("buy me a coffee, :coffee:", "https://www.buymeacoffee.com/aicopy")

st.subheader('추천글!', divider='rainbow') 
st.link_button("인스타 망한계정 살린 방법! :sleeping_accommodation:", "https://subad.kr/instafollower/")
st.link_button("블로그 최적화 도구! :heavy_check_mark:", "https://check.save-money.co.kr/blog-aicopy/")
st.link_button("광고문의 :coffee:", "https://open.kakao.com/o/s0ic2hMf")
