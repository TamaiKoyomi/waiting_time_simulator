import streamlit as st
import time

st.title('待ち時間シミュレーター')

def menu():
    
    st.write('並ぶ前に何分くらい待つのか知りたいですか? それとも、今並んでいる行列があと何分で自分の番になるのか知りたいですか?')

    col1 , col2 = st.columns(2)

    with col1:
        if st.button('前'):
            st.session_state.screen = 1

    with col2:
        if st.button('後'):
            st.session_state.screen = 5

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

    st.session_state.u = st.session_state.inf / 180
    l = st.session_state.back / 180
    
    r = l / st.session_state.u
    bunbo = 1-r
    left = r / bunbo
    right = 1 / st.session_state.u

    result = int(left * right)

    if st.session_state.u < l:
        st.session_state.screen = 4
    
    st.write('この列の平均待ち時間: ' + str(result) + '秒')

def number():
    st.write('発散プログラム')
    st.write('待ち行列理論が適用できないためほかの方法で待ち時間を算出します')
    st.write('今何グループ並んでいますか?')
    population = st.number_input('Input any number…', 0)

    half = population / 2
    time = int(st.session_state.u * half)

    st.title('この列の待ち時間 約'+ str(time) + '秒')

def inf_aft():
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
            st.session_state.screen = 6

def num_aft():
    st.session_state.u = st.session_state.inf / 180
    
    st.write('今何グループ並んでいますか?')
    population = st.number_input('Input any number…', 0)

    half = population / 2
    time = int(st.session_state.u * half)

    st.title('この列の待ち時間 約'+ str(time) + '秒')

if 'screen' not in st.session_state:
    st.session_state.screen = 0

if st.session_state.screen == 0:
    menu()
elif st.session_state.screen == 1:
    front_bef()
elif st.session_state.screen == 2:
    back_bef()
elif st.session_state.screen == 3:
    cal()
elif st.session_state.screen == 4:
    number()
elif st.session_state.screen == 5:
    inf_aft()
elif st.session_state.screen == 6:
    num_aft()