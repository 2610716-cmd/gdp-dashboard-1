import streamlit as st

# 웹 페이지 제목 설정
st.title("🎓 간단 성적 분석")
st.write("각 과목의 점수를 입력하면 평균 점수와 최종 학점을 계산해 줍니다.")

st.divider()  # 구분선

# 과목 리스트
subjects = ["1", "2", "3"]
scores = []

# 1. 입력부: 반복문을 통해 각 과목의 점수를 입력받는 위젯 생성
st.subheader("📝 점수 입력")
for s in subjects:
    # min_value, max_value로 입력 범위를 제한하고, 기본값(value)을 0으로 설정
    score = st.number_input(
        f"{s}번 과목 점수", 
        min_value=0, 
        max_value=100, 
        value=0, 
        step=1,
        key=f"subject_{s}"  # 위젯 고유 키 지정
    )
    scores.append(score)

st.divider()

# 2. 로직부: 계산 및 학점 산출 (사용자가 버튼을 누르면 계산 시작)
if st.button("📊 성적 계산하기"):
    
    # 평균 계산
    avg = sum(scores) / len(scores)

    # 학점 조건문
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    else:
        grade = "D"

    # 3. 출력부: 웹 화면에 결과 표시
    st.subheader("🎯 계산 결과")
    
    # 깔끔한 시각화를 위해 컬럼 나누기
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="평균 점수", value=f"{avg:.2f} 점")
    with col2:
        st.metric(label="최종 등", value=f"{grade} 등급")
        
    # 등급에 따른 안내 메시지 (st.success, st.info 등 활용)
    if grade in ["A", "B"]:
        st.success(f"훌륭합니다! 최종 등급은 **{grade}**입니다. 🎉")
    elif grade == "C":
        st.info(f"수고하셨습니다. 최종 등급은 **{grade}**입니다. 👍")
    else:
        st.error(f"조금 더 분발해보세요! 최종 등급은 **{grade}**입니다. 💪")