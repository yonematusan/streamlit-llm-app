from dotenv import load_dotenv
load_dotenv()


from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import SystemMessage, HumanMessage
llm = ChatOpenAI(model_name="gpt-4o-mini", tempreature=0)
messages_1= [
    SystemMessage(content="あなたは健康に関する専門家です。"),
    HumanMessage(content="健康のためにまずすべきことは何ですか？"),
]
result_1 = llm(messages_1)
print(result_1)

messages_2= [
    SystemMessage(content="あなたは法律に関する専門家です。"),
    HumanMessage(content="月の残業時間は何時間までですか？"),
]
result_2 = llm(messages_2)
print(result_2)


import streamlit as st
st.title("######LLM App")

st.write("#### これはLLMを使ったアプリケーションです。")
st.write("健康か法律に関する質問を入力してください。")
st.write("質問の例: タンパク質を多く摂れる食事は？")
st.write("#### AかBの選択肢を選んでください。")

selected_item = st.radio(
    "選択肢を選んでください。Aは健康、Bは法律に関する質問です。",
    ("A", "B"),
    index=0,
)

st.divider()

if selected_item == "A":
    input_message = st.text_input("健康に関することを入力してください。:")
    st.write("選択肢Aが選ばれました。")
    messages_1 = [
        SystemMessage(content="あなたは健康に関する専門家です。"),
        HumanMessage(content="健康のためにまずすべきことは何ですか？"),
    ]
    messages_1.append(SystemMessage(content="あなたは健康に関する専門家です。"))    
    messages_1.append(HumanMessage(content=input_message))
    result_1 = llm(messages_1)
    st.write(result_1.content)

else:
    input_message = st.text_input("何でも入力してください。:")
    st.write("選択肢Bが選ばれました。")
    messages_2 = [
        SystemMessage(content="あなたは法律に関する専門家です。"),
        HumanMessage(content="月の残業時間は何時間までですか？"),
    ]
    messages_2.append(SystemMessage(content="あなたは法律に関する専門家です。"))    
    messages_2.append(HumanMessage(content=input_message))
    result_2 = llm(messages_2)

if st.button("送信"):
    st.divider()

    if selected_item == "A":
        input_message = st.text_input("何でも入力してください。:")
        st.write("選択肢Aが選ばれました。")
        messages_1.append(HumanMessage(content=input_message))
        result_1 = llm(messages_1)
        st.write(result_1.content)

    else:
        input_message = st.text_input("何でも入力してください。:")
        st.write("選択肢Bが選ばれました。")
        messages_2.append(HumanMessage(content=input_message))
        result_2 = llm(messages_2)
        st.write(result_2.content)

    