🌊 Storm Surge Visualization

This project provides functionality for extracting storm surge information from JSON files and visualizing it through Python scripts.



📂 Project Structure

Storm_Surge_Visualization/

├── storm_surge_json_extract.py       # Extract storm surge data from JSON files

├── storm_surge_json_selected.csv     # Example dataset after extraction

├── storm_surge_visualization.py      # Visualization script after filtering CSV data

├── Other_Attempt/                    # Other experimental code (some trials based on tutorials)

🚀 Features

Data Extraction: Filter and export key storm surge data from raw JSON files

Data Storage: Save extracted results into CSV format for further analysis

Visualization: Generate dynamic wave plots ranked by storm surge data.

  The ranking is displayed in groups of 8

  The higher the storm surge, the taller the wave

  Includes small physics-inspired effects (e.g., waves gradually decay or overlap with newly generated waves)


📊 Usage

1. Data Extraction
Run the following program to extract storm surge data from JSON files and save it as CSV:
  storm_surge_json_extract.py

2. Data Visualization
Use the extracted CSV file for visualization:
  storm_surge_visualization.py
  This will generate a storm surge ranking table.


📈 Example Output

Dynamic storm surge sequence table

<img width="800" height="400" alt="Figure_1" src="https://github.com/user-attachments/assets/e858da0f-b577-494f-885b-24efd015d2a4" />
