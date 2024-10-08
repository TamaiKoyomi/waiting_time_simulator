import streamlit as st
import asyncio
import threading
import time

#　メニューごとに関数設定　初期画面と待ちボタン画面とアンケート画面と結果画面

number = 0
if 'number' not in st.session_state:
    st.session_state.number = number

def menu():

    #col1,col2 = st.columns

    #with col1:

    

    async def async_timer(seconds):
        print(f'非同期タイマー開始：{seconds}秒')
        await asyncio.sleep(seconds)
        print(f'非同期タイマー終了：{seconds}秒')

    t1 = threading.Thread(target=async_timer, args=("t1",))

    st.title('待ち時間シミュレーター')
    st.write('スタートボタンを押して、待ち時間をシミュレーションしてみましょう!')
    
    #with col2:
    st.write('時間いっぱい、1グループ進むたびに以下のボタンを押してください。')
    
    if st.button('1分間タイマースタート'):
        asyncio.run(t1(5))

    if st.button('進んだ'):
        st.session_state.number += 1

    st.write('現在ボタンを押した回数:' + str(st.session_state.number) + '回')

    if st.button('1グループ分取り消す'):
        if st.session_state.number > 0:
            st.session_state.number -= 1

menu()