import streamlit as st
import time
from time import sleep

#　メニューごとに関数設定　初期画面と待ちボタン画面とアンケート画面と結果画面

number = 0
if 'number' not in st.session_state:
    st.session_state.number = number

def menu():

    #col1,col2 = st.columns

    #with col1:

    target_time = 60

    def up_timer(secs):
        for i in range(secs, -1, -1):
            print(i)
            sleep(1)
    print("時間です！")

    st.title('待ち時間シミュレーター')
    st.write('スタートボタンを押して、待ち時間をシミュレーションしてみましょう!')
    
    #with col2:
    st.write('時間いっぱい、1グループ進むたびに以下のボタンを押してください。')
    
    if st.button('1分間タイマースタート'):
        up_timer(target_time)
        
    if st.button('進んだ'):
        st.session_state.number += 1

    st.write('現在ボタンを押した回数:' + str(st.session_state.number) + '回')

    if st.button('1グループ分取り消す'):
        if st.session_state.number > 0:
            st.session_state.number -= 1

menu()