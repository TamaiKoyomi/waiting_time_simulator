import streamlit as st

#　メニューごとに関数設定　初期画面と待ちボタン画面とアンケート画面と結果画面

def menu():
    st.session_state.number = 0
    st.title('待ち時間シミュレーター')
    st.write('スタートボタンを押して、待ち時間をシミュレーションしてみましょう!')
    if st.button('スタート'):
        count()
    

def count():
    st.write('自分の後ろに1人(1グループ)並ぶ度に下のボタンを押してください。')
    if st.button('人が来た'):
        st.session_state.number += 1

    st.write('現在ボタンを押した回数:' + str(st.session_state.number) + '回')

    if st.button('1人分取り消す'):
        if st.session_state.number > 0:
            st.session_state.number -= 1


count()