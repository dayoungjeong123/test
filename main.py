import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

## 시뮬레이션 설정
st.title("외계 행성 중력 렌즈 시뮬레이터 🔭")
st.write(
    "이 시뮬레이터는 외계 행성에 의한 중력 렌즈 현상을 **개념적으로** 보여줍니다."
    "행성 각도와 행성 거리를 조절하여 배경별의 광도 변화를 확인해보세요."
)

st.sidebar.header("파라미터 조절")

# 행성 각도 슬라이더 (도 단위)
planet_angle_deg = st.sidebar.slider(
    "행성 각도 (도)", min_value=0, max_value=360, value=180, step=10
)
# 행성 각도를 라디안으로 변환
planet_angle_rad = np.deg2rad(planet_angle_deg)

# 행성 거리 슬라이더 (천문 단위, AU)
# 실제 값에 따라 적절한 범위로 조절할 수 있습니다.
planet_distance_au = st.sidebar.slider(
    "행성 거리 (AU)", min_value=0.1, max_value=10.0, value=1.0, step=0.1
)

---

## 중력 렌즈 효과 시각화 (개념적)

# 여기서는 중력 렌즈 효과를 단순화하여 시각적으로 보여줍니다.
# 실제 중력 렌즈 현상(아인슈타인 링 등)을 구현하려면 더 복잡한 물리 모델이 필요합니다.

col1, col2 = st.columns(2)

with col1:
    st.subheader("외계 행성 및 배경별")
    fig_space, ax_space = plt.subplots(figsize=(6, 6))

    # 배경별 (고정)
    ax_space.plot(0, 0, 'o', markersize=15, color='gold', label='배경별')

    # 행성 (각도와 거리에 따라 위치 변경)
    planet_x = planet_distance_au * np.cos(planet_angle_rad)
    planet_y = planet_distance_au * np.sin(planet_angle_rad)
    ax_space.plot(planet_x, planet_y, 'o', markersize=10, color='darkgray', label='외계 행성')

    ax_space.set_xlim(-10, 10)
    ax_space.set_ylim(-10, 10)
    ax_space.set_aspect('equal', adjustable='box')
    ax_space.set_xlabel("X (AU)")
    ax_space.set_ylabel("Y (AU)")
    ax_space.set_title(f"행성 위치: ({planet_x:.2f}, {planet_y:.2f}) AU")
    ax_space.grid(True)
    ax_space.legend()
    st.pyplot(fig_space)

with col2:
    st.subheader("배경별 광도 변화")

    # 광도 변화를 시뮬레이션하기 위한 단순화된 모델
    # 행성이 배경별에 가까워질수록 광도가 증가하는 경향을 보여줍니다.
    # 이 부분은 실제 중력 렌즈 광도 곡선과는 다를 수 있습니다.
    
    # 배경별과 행성 사이의 거리
    distance_between = np.sqrt(planet_x**2 + planet_y**2)

    # 거리에 따른 광도 변화 (예시: 거리가 0에 가까워질수록 광도 증가)
    # 실제 중력 렌즈에서는 행성이 배경별을 거의 가릴 때 광도가 최대로 증가합니다.
    # 여기서는 간단히 1/거리 + 기본 광도 개념으로 시뮬레이션합니다.
    
    # 0으로 나누는 것을 방지
    if distance_between < 0.1: # 아주 가까울 때 최대치로
        light_intensity = 5.0
    else:
        light_intensity = 1.0 + (1.0 / distance_between) # 거리가 멀어질수록 1에 가까워짐

    # 시간 흐름에 따른 광도 변화 시뮬레이션 (간단한 예시)
    # 실제로는 렌즈 이벤트를 시간에 따라 추적해야 합니다.
    time_points = np.linspace(0, 10, 100) # 100개의 시간 포인트
    
    # 현재 행성 각도와 거리에 따른 피크 지점을 표시
    # 여기서는 시뮬레이션의 현재 상태를 나타내는 광도 값을 하나의 점으로 보여줍니다.
    
    # 간단한 가상의 광도 곡선
    # 행성이 특정 지점을 통과할 때 광도 피크가 나타나는 것을 가정
    peak_time = 5.0
    time_offset = (planet_angle_deg / 360.0) * 10.0 # 각도에 따라 피크 시간 조절
    
    # 피크가 나타나는 구간을 더 명확하게 보여주기 위한 가중치
    light_curve = 1.0 + np.exp(-((time_points - (peak_time + time_offset))**2) / (2 * 1.5**2)) * light_intensity
    
    fig_light, ax_light = plt.subplots(figsize=(6, 6))
    ax_light.plot(time_points, light_curve, color='blue')
    ax_light.plot(time_points[int(len(time_points)/2)], light_curve[int(len(time_points)/2)], 'ro', markersize=8, label=f'현재 광도: {light_intensity:.2f}')

    ax_light.set_xlabel("시간 (가상)")
    ax_light.set_ylabel("상대 광도")
    ax_light.set_title("배경별 광도 변화 (시뮬레이션)")
    ax_light.set_ylim(0.8, 6.0) # 광도 범위 조정
    ax_light.grid(True)
    ax_light.legend()
    st.pyplot(fig_light)

st.markdown("---")
st.write(
    "**참고:** 이 시뮬레이터는 중력 렌즈 현상을 **개념적으로** 보여주기 위한 것입니다."
    "실제 중력 렌즈 광도 곡선은 아인슈타인 링, 마이크로렌즈링 이벤트 등 복잡한 물리 모델을 기반으로 계산됩니다."
    "더 정교한 시뮬레이터를 위해서는 아인슈타인 방정식, 렌즈 방정식 등을 이용한 심층적인 물리 모델링이 필요합니다."
)
