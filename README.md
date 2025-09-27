🌊 Storm Surge Visualization
一个用于 风暴潮数据提取与可视化 的工具库。 本项目提供了从 JSON 数据中提取风暴潮信息，并通过 Python 脚本进行可视化展示的功能，帮助研究人员和开发者更直观地理解风暴潮的影响。

📂 项目结构
代码
Storm_Surge_Visualization/
│
├── storm_surge_json_extract.py       # 从 JSON 文件中提取风暴潮数据
├── storm_surge_visualization.py      # 可视化脚本
├── storm_surge_json_selected.csv     # 提取后的示例数据
├── Other_Attempt/                    # 其他尝试或实验性代码
🚀 功能特性
数据提取：从原始 JSON 文件中筛选并导出关键风暴潮数据

数据存储：将提取结果保存为 CSV 文件，方便后续分析

可视化展示：利用 Python 脚本绘制风暴潮趋势图、空间分布图等

可扩展性：支持根据需求修改提取字段和可视化样式

🔧 环境依赖
请确保已安装以下依赖：

Python 3.8+

常用库：

bash
pip install pandas matplotlib seaborn
📊 使用方法
1. 数据提取
运行以下命令，从 JSON 文件中提取风暴潮数据并保存为 CSV：

bash
python storm_surge_json_extract.py
2. 数据可视化
使用提取后的 CSV 文件进行可视化：

bash
python storm_surge_visualization.py
可生成风暴潮随时间变化的曲线图、空间分布图等。

📈 示例输出
风暴潮时间序列图

风暴潮空间分布热力图

（你可以在这里放一些运行结果的截图）

📌 TODO
[ ] 增加更多可视化图表（如三维可视化）

[ ] 支持交互式可视化（Plotly / Bokeh）

[ ] 增加对不同数据源的兼容性

🤝 贡献
欢迎提交 Issue 或 Pull Request 来改进本项目。

📜 许可证
本项目基于 MIT License 开源。
