import streamlit as st

#　メニューごとに関数設定　初期画面と待ちボタン画面とアンケート画面と結果画面

number = 0

def menu():
    st.title('待ち時間シミュレーター')
    st.write('スタートボタンを押して、待ち時間をシミュレーションしてみましょう!')
    if st.button('スタート'):
        count()
    

def count():
    st.write('自分の後ろに1人(1グループ)並ぶ度に下のボタンを押してください。')
    if st.button('人が来た'):
        number += 1

    st.write('現在ボタンを押した回数:' + str(number) + '回')

    if st.button('1人分取り消す'):
        if number > 0:
            number -= 1


menu()