import streamlit as st
import time

st.title('待ち時間シミュレーター')

def menu():
    st.write('並ぶ前に何分くらい待つのか知りたいですか? それとも、今並んでいる行列があと何分で自分の番になるのか知りたいですか?')
    col1,col2 = st.columns

    with col1:
        if st.button('並ぶ前'):
            st.session_state.screen = 1

    with col2:
        if st.button('並んだ後'):
            st.session_state.screen = 2

def front_bef():
    st.write('スタートボタンを押してから、3グループ分進んだらストップボタンを押してください。')
    if 'start_time' not in st.session_state:
        st.session_state.start_time = None
        st.session_state.elapsed_time = 0

    if st.button('スタート'):
        st.session_state.start_time = time.time()
        st.session_state.elapsed_time = 0

    if st.button('ストップ'):
        if st.session_state.start_time is not None:
            st.session_state.elapsed_time += time.time() - st.session_state.start_time
            st.session_state.start_time = None

    if st.session_state.start_time is not None:
        elapsed = st.session_state.elapsed_time + (time.time() - st.session_state.start_time)
        st.session_state.inf = elapsed
        screen = 2
    else:
        elapsed = st.session_state.elapsed_time

    st.write(f"経過時間:{elapsed:.2f}秒")

if 'screen' not in st.session_state:
    st.screen = 0

if st.screen == 0:
    menu()
elif st.screen == 1:
    front_bef()
elif st.screen == 2:
    st.write('うわあああ')