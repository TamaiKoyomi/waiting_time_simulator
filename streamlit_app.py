import streamlit as st
import asyncio
import threading
import time

# Initialize session state for number
if 'number' not in st.session_state:
    st.session_state.number = 0

def async_timer(seconds):
    """Function to run the async timer within the thread."""
    asyncio.run(async_timer_inner(seconds))

async def async_timer_inner(seconds):
    print(f'非同期タイマー開始：{seconds}秒')
    await asyncio.sleep(seconds)
    print(f'非同期タイマー終了：{seconds}秒')

def menu():
    st.title('待ち時間シミュレーター')
    st.write('スタートボタンを押して、待ち時間をシミュレーションしてみましょう!')

    st.write('時間いっぱい、1グループ進むたびに以下のボタンを押してください。')

    if st.button('1分間タイマースタート'):
        t1 = threading.Thread(target=async_timer, args=(60,))
        t1.start()  # Start the thread

    if st.button('進んだ'):
        st.session_state.number += 1

    st.write('現在ボタンを押した回数: ' + str(st.session_state.number) + '回')

    if st.button('1グループ分取り消す'):
        if st.session_state.number > 0:
            st.session_state.number -= 1

menu()
