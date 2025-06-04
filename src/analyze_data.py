import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import check_data_quality, normalize_column, filter_outliers

# Load dataset
df = pd.read_csv("data/finland_housing_api_data.csv")

# Perform data quality check
check_data_quality(df)

# Filter rows for price per square meter
df_price = df[df["Information"] == "Price per square meter (eur/m2)"].copy()
df_price = df_price.dropna(subset=["value"])
df_price["value"] = pd.to_numeric(df_price["value"], errors="coerce")

# Normalize categorical columns
df_price = normalize_column(df_price, "Region")
df_price = normalize_column(df_price, "Form of ownership of plot")

# Remove outliers
df_price = filter_outliers(df_price, "value", 500, 10000)

# Set style
sns.set_theme(style="whitegrid")

# Chart 1: National average price trend
fig1 = plt.figure(figsize=(10, 6))
sns.lineplot(
    data=df_price[df_price["Region"] == "Whole Country"],
    x="Year",
    y="value",
    marker="o"
)
plt.title("Average Price per m² in New Dwellings (Finland, 2015–2024)")
plt.xlabel("Year")
plt.ylabel("Price per m² (€)")
plt.xticks(rotation=45)
plt.tight_layout()
fig1.savefig("results/price_trend_finland.png")
plt.close(fig1)

# Chart 2: Price by plot ownership type
fig2 = plt.figure(figsize=(10, 6))
sns.lineplot(
    data=df_price[df_price["Region"] == "Whole Country"],
    x="Year",
    y="value",
    hue="Form of ownership of plot",
    marker="o"
)
plt.title("Price per m² by Plot Ownership Type (Finland)")
plt.xlabel("Year")
plt.ylabel("Price per m² (€)")
plt.legend(title="Plot Ownership")
plt.xticks(rotation=45)
plt.tight_layout()
fig2.savefig("results/price_by_plot_type.png")
plt.close(fig2)

# Chart 3: Price trends by selected regions
top_regions = ["Helsinki", "Tampere"]
region_data = df_price[df_price["Region"].isin(top_regions)]

plt.figure(figsize=(12, 6))
sns.lineplot(
    data=region_data,
    x="Year",
    y="value",
    hue="Region",
    marker="o"
)
plt.title("Average Price per m² in New Dwellings by Region (2015–2024)")
plt.xlabel("Year")
plt.ylabel("Price per m² (€)")
plt.xticks(rotation=45)
plt.legend(title="Region")
plt.tight_layout()
plt.savefig("results/price_by_region.png")
plt.show()