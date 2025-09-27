from matplotlib.widgets import Button
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import random

# 用于顺序选择波动线的计数器
wave_line_counter = 0


# --- 读取风暴潮数据 ---
data = pd.read_csv(r'./storm_surge_json_selected.csv')
surge_heights = data['Storm Surge Height'].values
datetimes = data['DateTime'].fillna('').values
storm_names = data['Tropical Cyclone'].fillna('').values

WIDTH, HEIGHT = 800, 400  # 增加窗口高度
ORIGINAL_HEIGHT = 180  # 线条分布高度保持原始
center_offset = (HEIGHT - ORIGINAL_HEIGHT) / 2
N_LINES = 8
LINE_LEN = 700
Y_MARGIN = 5
ys = np.linspace(Y_MARGIN, ORIGINAL_HEIGHT - Y_MARGIN, N_LINES)[::-1] + center_offset  # 反转，让排名第一在最下面

# --- 物理参数 ---
DECAY = 0.98  # 衰减系数
BASE_WAVE_SPEED = 1.0  # 基础波速（更快）
N_POINTS = LINE_LEN

# --- 弦的状态 ---
positions = np.zeros((N_LINES, N_POINTS))  # 当前位移
velocities = np.zeros((N_LINES, N_POINTS))  # 当前速度

# --- 初始化画布 ---

fig, ax = plt.subplots(figsize=(WIDTH/100, HEIGHT/100))
plt.subplots_adjust(left=0, right=1, top=1, bottom=0.15)
txt_station = ax.text(10, 10, 'Measurement Station: Quarry Bay/North Point', color='white', fontsize=10, ha='left', va='bottom', backgroundcolor='black', bbox=dict(facecolor='black', alpha=0.6, boxstyle='round,pad=0.2'))
# --- 左下角潮汐+时间文本 ---
## --- 生成按钮 ---
button_axes = []
buttons = []
button_labels = []
for i in range(16):
    start_rank = i * 8 + 1
    end_rank = start_rank + 7
    label = f"{start_rank}-{end_rank}"
    button_labels.append(label)
    left = 0.05 + (i % 8) * 0.11
    # 调转上下行位置：原本上面一行变为下面，下面一行变为上面
    bottom = 0.10 - (i // 8) * 0.08
    ax_btn = fig.add_axes([left, bottom, 0.09, 0.06])
    btn = Button(ax_btn, label, color='gray', hovercolor='lightblue')
    button_axes.append(ax_btn)
    buttons.append(btn)
ax.set_xlim(0, LINE_LEN)
ax.set_ylim(0, HEIGHT)
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.axis('off')



lines = []
name_texts = []
x = np.linspace(0, LINE_LEN, N_POINTS)
for y in ys:
    (line,) = ax.plot(x, np.full(N_POINTS, y), lw=1, color='white')
    lines.append(line)
    txt = ax.text(0, y, '', color='yellow', fontsize=10, ha='left', va='center', backgroundcolor='black', bbox=dict(facecolor='black', alpha=0.6, boxstyle='round,pad=0.2'))
    name_texts.append(txt)

# --- 左下角潮汐+时间文本 ---



# --- 动画更新函数 ---

# 当前按钮对应的排名区间
current_group = 0


def show_group(group_idx):
    global positions, velocities, current_group
    current_group = group_idx
    positions[:] = 0
    velocities[:] = 0
    # 初始化为静止状态，不生成初始波形
    for j in range(N_LINES):
        rank = group_idx * 8 + j
        line_idx = j
        positions[line_idx, :] = 0
        velocities[line_idx, :] = 0
        if rank < len(surge_heights):
            dt_str = str(datetimes[rank])
            year = ''
            if dt_str and len(dt_str) >= 4:
                year = dt_str[:4]
            name_texts[line_idx].set_text(f"{storm_names[rank]}  {surge_heights[rank]:.2f}m  {year}")
        else:
            name_texts[line_idx].set_text('')
        name_texts[line_idx].set_position((0, ys[line_idx]))


def animate(i):
    # 当前显示的8个排名，线条依次循环产生波
    ranks = [current_group * 8 + j for j in range(N_LINES)]
    wave_speed = BASE_WAVE_SPEED
    interval = 8  # 每隔8帧依次为一根线条产生新波
    active_idx = (i // interval) % N_LINES
    for j, rank in enumerate(ranks):
        line_idx = j
        if rank < len(surge_heights):
            surge = surge_heights[rank]
            dt = datetimes[rank]
            if i % interval == 0 and line_idx == active_idx:
                # 不清空该线条，多个波互不影响
                min_surge = np.nanmin(surge_heights)
                max_surge = np.nanmax(surge_heights)
                norm_surge = (surge - min_surge) / (max_surge - min_surge)
                amp = 10 + 80 * norm_surge
                pos = np.random.randint(N_POINTS//8, N_POINTS*7//8)
                width = 18  # 适中的波宽
                left = max(0, pos-width//2)
                right = min(N_POINTS, pos+width//2)
                x_gauss = np.linspace(-1, 1, right-left)
                positions[line_idx, left:right] += amp * np.hanning(right-left)

        else:
            name_texts[line_idx].set_text('')
        # 物理模拟：一维波动方程（简化）
        laplacian = np.zeros(N_POINTS)
        laplacian[1:-1] = positions[line_idx, :-2] - 2*positions[line_idx, 1:-1] + positions[line_idx, 2:]
        velocities[line_idx] += wave_speed * laplacian
        velocities[line_idx] *= DECAY  # 衰减
        positions[line_idx] += velocities[line_idx]
        positions[line_idx, 0] = 0
        positions[line_idx, -1] = 0
        # 超出窗口的波直接设为0
        ydata = ys[line_idx] + positions[line_idx]
        ydata = np.where((ydata < 0) | (ydata > HEIGHT), ys[line_idx], ydata)
        lines[line_idx].set_ydata(ydata)
        name_texts[line_idx].set_position((0, ys[line_idx]))
    return lines + name_texts + [txt_station]


# --- 交互式窗口 ---

# 按钮事件绑定
for idx, btn in enumerate(buttons):
    btn.on_clicked(lambda event, i=idx: show_group(i))

# 默认显示第一个分组
show_group(0)

ani = animation.FuncAnimation(fig, animate, frames=200, interval=120, blit=True)
plt.show()
