# from pybaseball import playerid_lookup, statcast_pitcher

# import matplotlib.pyplot as plt
# import seaborn as sns

# player_ids = playerid_lookup("Greg", "Maddux")

# print(player_ids)

# data = statcast_pitcher("2008-04-01", "2008-10-31", 118120)

# if data.empty :
#     print("데이터가 없습니다.")
# else :
#     plt.figure(figsize=(10, 6))

#     sns.boxplot(data=data, x = 'pitch_type', y = 'release_speed')

#     plt.title("Greg Maddux Pitch Speed by Type(2008 Season)")
#     plt.xlabel("Pitch Type")
#     plt.ylabel("Speed (mph)")
#     plt.show()



# 컴퓨터는 위에서 아래로 코드를 읽는데, **그래프를 그리는 줄(32번째 줄)**에 도착했을 때 아직 data = ... 로 시작하는 줄을 만나지 못했거나, 그 줄이 실행되지 않은 것입니다.

# 가장 흔한 원인은 다음과 같습니다.

# 데이터 가져오는 코드를 지웠거나 주석(#) 처리했을 때

# 데이터 가져오는 코드가 if문 안에 갇혀 있어서 실행되지 않았을 때

# Greg Maddux의 2008년 데이터를 안전하게 가져와서 그래프까지 그리는 완성된 전체 코드를 드립니다. 이 코드를 복사해서 기존 내용을 모두 지우고 붙여넣어 보세요.


import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from pybaseball import statcast_pitcher
import matplotlib.font_manager as fm
import os

font_path = os.path.join(os.getcwd(), "NanumGothic.ttf")

import matplotlib.font_manager as fm
import os

# 1. 폰트 파일의 경로 지정 (같은 폴더에 있다고 가정)
# 리눅스 환경에서도 경로를 잘 찾도록 os 모듈 사용
font_path = os.path.join(os.getcwd(), "NanumGothic.ttf")

# 2. 폰트 파일이 실제로 있는지 확인 (디버깅용)
if os.path.exists(font_path):
    # 3. Matplotlib에 폰트 추가
    fm.fontManager.addfont(font_path)
    
    # 4. 폰트 설정 (폰트 파일의 내부 이름을 가져와서 설정)
    font_name = fm.FontProperties(fname=font_path).get_name()
    plt.rc('font', family=font_name)
else:
    st.error("폰트 파일을 찾을 수 없습니다. GitHub에 NanumGothic.ttf가 올라갔는지 확인하세요.")

# 5. 마이너스 기호(-) 깨짐 방지
plt.rc('axes', unicode_minus=False)


# 1. 제목 설정
st.title("⚾ Greg Maddux 투구 분석 (2008)")

# 2. 데이터 가져오기 (이 부분이 반드시 실행되어야 합니다!)
# Greg Maddux ID: 118120
# 중요: Statcast 데이터가 있는 2008년만 조회해야 에러가 안 납니다.
with st.spinner('데이터를 불러오는 중입니다... 잠시만 기다려주세요.'):
    try:
        data = statcast_pitcher("2008-04-01", "2008-10-31", 118120)
    except Exception as e:
        st.error(f"데이터를 가져오는데 실패했습니다: {e}")
        data = None

# 3. 데이터가 잘 들어왔는지 확인 후 그래프 그리기
# (data 변수가 없거나 비어있으면 그래프를 그리지 않도록 막아주는 안전장치)
if data is not None and not data.empty:
    st.success(f"데이터 로드 성공! 총 {len(data)}개의 투구 정보를 찾았습니다.")

    # 그래프 그리기 (Streamlit 권장 방식: fig, ax 사용)
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # ax=ax 옵션을 넣어주어야 경고가 뜨지 않습니다.
    sns.boxplot(data=data, x='pitch_type', y='release_speed', ax=ax)
    
    ax.set_title("Greg Maddux Pitch Speed by Type (2008 Season)")
    ax.set_xlabel("Pitch Type")
    ax.set_ylabel("Speed (mph)")
    
    # 웹 화면에 출력
    st.pyplot(fig)

else:
    st.warning("데이터가 없습니다. 날짜나 선수 ID를 확인해주세요.")