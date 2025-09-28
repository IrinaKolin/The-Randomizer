import streamlit as st
import random

st.title("🎲 Генератор случайных чисел")

# Ввод максимального числа
n = st.number_input("Введите максимальное число", min_value=1, value=10, step=1)

# Сохраняем последнее сгенерированное число в сессии
if "last_num" not in st.session_state:
    st.session_state.last_num = None

# Кнопка генерации
if st.button("Сгенерировать число"):
    st.session_state.last_num = random.randint(1, n)

# Если уже генерировали — показываем результат и даём выбор
if st.session_state.last_num is not None:
    st.success(f"Ваше число: **{st.session_state.last_num}**")
    st.write("Хотите сгенерировать ещё число?")
    if st.button("Да"):
        st.session_state.last_num = random.randint(1, n)
        st.success(f"Ваше новое число: **{st.session_state.last_num}**")
    else:
        st.info("Спасибо, что воспользовались нашим генератором чисел!")
