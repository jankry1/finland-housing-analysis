Finland Housing Market Analysis (2015–2024)

This project presents a data analysis of the Finnish housing market using official statistics from Statistics Finland's open API. The primary focus is on the price trends of new dwellings measured by euros per square meter (EUR/m²) from 2015 to 2024.

📦 Project Structure

finland-housing-analysis/
├── data/
│   └── finland_housing_api_data.csv         # Raw dataset downloaded from the API
├── results/
│   ├── price_trend_finland.png              # Line plot for national trend
│   ├── price_by_plot_type.png               # Price vs. land ownership
│   └── price_by_region.png                  # Comparison of Helsinki & Tampere
├── src/
│   ├── get_data.py                          # API fetch and CSV export
│   ├── analyze_data.py                      # Data cleaning, visualization, and analysis
│   └── utils.py                             # Reusable helper functions
├── .gitignore
├── requirements.txt
└── README.md                                # Project overview (this file)

🔧 How to Run the Project

Clone the repository

git clone https://github.com/your-username/finland-housing-analysis.git
cd finland-housing-analysis

Install dependencies

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Fetch the latest data

python src/get_data.py

Run the analysis and generate graphs

python src/analyze_data.py

📊 Key Insights

Housing prices in Finland have been increasing steadily from 2015 to 2024, with a noticeable rise after 2020.

Ownership of land impacts pricing — dwellings on rented plots tend to have different trends than those on owned plots.

Helsinki vs. Tampere: Housing prices in Helsinki remain significantly higher than in other major cities.

🛠️ Tools and Technologies

Python 3.10+

pandas, matplotlib, seaborn for analysis and visualization

pyjstat, requests for API querying

🤝 Acknowledgements

Statistics source: Statistics Finland
