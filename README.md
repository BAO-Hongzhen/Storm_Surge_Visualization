🌊 Storm Surge Visualization

本项目提供了从 JSON 数据中提取风暴潮信息，并通过 Python 脚本进行可视化展示的功能。

📂 项目结构

代码

Storm_Surge_Visualization/

├── storm_surge_json_extract.py       # 从 JSON 文件中提取风暴潮数据

├── storm_surge_json_selected.csv     # 提取后的示例数据

├── storm_surge_visualization.py      # 对CSV数据进行了筛选后的可视化脚本

├── Other_Attempt/                    # 其他尝试或实验性代码（基于tutorial的内容进行的一些小尝试）


🚀 功能特性

数据提取：从原始 JSON 文件中筛选并导出关键风暴潮数据

数据存储：将提取结果保存为 CSV 文件，方便后续分析

可视化展示：利用 Python 脚本绘制基于风暴潮数据排名的动态波形图，我将排名以8个为一组进行展示。同时，风暴潮高度越高，波的高度也会越高。我也制作了一些基于物理的小效果（如波会慢慢衰减或者与新产生的波进行叠加）。


📊 使用方法

1. 数据提取
运行以下程序，从 JSON 文件中提取风暴潮数据并保存为 CSV：
storm_surge_json_extract.py

2. 数据可视化
使用提取后的 CSV 文件进行可视化：
storm_surge_visualization.py
可生成风暴潮排名表。


📈 示例输出

风暴潮动态序列表

<img width="800" height="400" alt="Figure_1" src="https://github.com/user-attachments/assets/e858da0f-b577-494f-885b-24efd015d2a4" />
