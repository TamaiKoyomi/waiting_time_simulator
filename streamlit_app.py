import streamlit as st
import time

# import asyncio
# import threading

'''# セッションステートの初期化
if 'number' not in st.session_state:
    st.session_state.number = 0

def async_timer(seconds):
    """スレッド内で実行するための関数"""
    asyncio.run(async_timer_inner(seconds))

async def async_timer_inner(seconds):
    print(f'非同期タイマー開始：{seconds}秒')
    await asyncio.sleep(seconds)
    print(f'非同期タイマー終了：{seconds}秒')'''

if 'start_time' not in st.session_state:
    st.session_state.start_time = None
    st.session_state.elapsed_time = 0

if st.button('スタート'):
    st.session_state.start_time = time.time()
    st.session_state.elapsed_time = 0

st.write('デバッグ'+str(st.session_state.start_time))

if st.button('ストップ'):
    if st.session_state.start_time is not None:
        st.session_state.elapsed_time += time.time() - st.session_state.start_time
        st.session_state.start_time = None

if st.session_state.start_time is not None:
    elapsed = st.session_state.elapsed_time + (time.time() - st.session_state.start_time)
else:
    elapsed = st.session_state.elapsed_time

st.write(f"経過時間:{elapsed:.2f}秒")

'''def menu():
    st.title('待ち時間シミュレーター')
    st.write('スタートボタンを押して、待ち時間をシミュレーションしてみましょう!')

    st.write('時間いっぱい、1グループ進むたびに以下のボタンを押してください。')

    if st.button('1分間タイマースタート'):
        t1 = threading.Thread(target=async_timer, args=(60,))
        t1.start()  # スレッドを開始

    if st.button('進んだ'):
        st.session_state.number += 1

    st.write('現在ボタンを押した回数: ' + str(st.session_state.number) + '回')

    if st.button('1グループ分取り消す'):
        if st.session_state.number > 0:
            st.session_state.number -= 1

menu()'''