import streamlit as st
import time

st.title('待ち時間シミュレーター')

def menu():
    st.write('並ぶ前に何分くらい待つのか知りたいですか? それとも、今並んでいる行列があと何分で自分の番になるのか知りたいですか?')
    if st.button('前'):
        st.session_state.screen = 1

def front_bef():
    st.write('スタートボタンを押してから、3グループ分進んだらストップボタンを押してください。')

    if 'start_time' not in st.session_state:
        st.session_state.start_time = None
        st.session_state.elapsed_time = 0

    if st.button('スタート'):
        st.session_state.start_time = time.time()
        st.session_state.elapsed_time = 0
    
    if st.session_state.start_time is not None:
        elapsed = st.session_state.elapsed_time + (time.time() - st.session_state.start_time)
        st.write('3グループ目が進むまで、しばしお待ちください……')
    else:
        elapsed = st.session_state.elapsed_time

    if st.button('ストップ'):
        if st.session_state.start_time is not None:
            st.session_state.elapsed_time += time.time() - st.session_state.start_time
            st.session_state.start_time = None
            st.session_state.inf = elapsed
            st.session_state.screen = 2

def back_bef():
    st.write('スタートボタンを押してから、3グループ並んだらストップボタンを押してください。')

    if 'start_time' not in st.session_state:
        st.session_state.start_time = None
        st.session_state.elapsed_time = 0

    if st.button('スタート'):
        st.session_state.start_time = time.time()
        st.session_state.elapsed_time = 0
    
    if st.session_state.start_time is not None:
        elapsed = st.session_state.elapsed_time + (time.time() - st.session_state.start_time)
        st.write('3グループ目が並ぶまで、しばしお待ちください……')
    else:
        elapsed = st.session_state.elapsed_time

    if st.button('ストップ'):
        if st.session_state.start_time is not None:
            st.session_state.elapsed_time += time.time() - st.session_state.start_time
            st.session_state.start_time = None
            st.session_state.back = elapsed
            st.session_state.screen = 3

def cal():
    st.write('計算結果')
    st.write(st.session_state.inf)
    st.write(st.session_state.back)

if 'screen' not in st.session_state:
    st.session_state.screen = 0

if st.session_state.screen == 0:
    menu()
elif st.session_state.screen == 1:
    front_bef()
elif st.session_state.screen == 2:
    back_bef()
elif st.session_state.screen == 3:
    st.write('計算結果の処理ページ')