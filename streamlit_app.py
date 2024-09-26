import streamlit as st
import time

# セッションステートの初期化
if 'number' not in st.session_state:
    st.session_state.number = 0

def menu():
    st.title('待ち時間シミュレーター')
    st.write('スタートボタンを押して、待ち時間をシミュレーションしてみましょう!')
    st.write('時間いっぱい、1グループ進むたびに以下のボタンを押してください。')

    if st.button('1分間タイマースタート'):
        st.session_state.timer_running = True
        st.session_state.timer_start_time = time.time()
        st.session_state.timer_duration = 60  # 1分

    if 'timer_running' in st.session_state and st.session_state.timer_running:
        elapsed_time = time.time() - st.session_state.timer_start_time
        progress = elapsed_time / st.session_state.timer_duration

        # プログレスバーを表示
        st.progress(progress)

        if elapsed_time >= st.session_state.timer_duration:
            st.session_state.timer_running = False
            st.write('タイマーが終了しました!')

    if st.button('進んだ'):
        st.session_state.number += 1

    st.write('現在ボタンを押した回数: ' + str(st.session_state.number) + '回')

    if st.button('1グループ分取り消す'):
        if st.session_state.number > 0:
            st.session_state.number -= 1

menu()
