import streamlit as st

#　メニューごとに関数設定　初期画面と待ちボタン画面とアンケート画面と結果画面


def menu():
    #col1,col2 = st.columns

    #with col1:
    st.title('待ち時間シミュレーター')
    st.write('スタートボタンを押して、待ち時間をシミュレーションしてみましょう!')
    
    #with col2:
    st.write('時間いっぱい、1グループ進むたびに以下のボタンを押してください。')
    if st.button('進んだ'):
        st.session_state.number += 1

    st.write('現在ボタンを押した回数:' + str(st.session_state.number) + '回')

    if st.button('1グループ分取り消す'):
        if st.session_state.number > 0:
            st.session_state.number -= 1

menu()