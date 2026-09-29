"""
PRODIGY_DS_01
--------------
Task: Create a bar chart or histogram to visualize the distribution of a
categorical or continuous variable, such as the distribution of ages or
genders in a population.

Dataset: world_population.csv — the official sample dataset provided by
Prodigy InfoTech for Task 1 (World Bank population data, 2001-2022, by
country). It contains 5 series per country: total/male/female population
counts, and male/female % of total population.

This script demonstrates BOTH chart types on this real data:
  1. A BAR CHART  -> Top 15 most populous countries in 2022 (categorical: Country)
  2. A HISTOGRAM  -> Distribution of 2022 total population across all countries (continuous)
Bonus: a gender split bar chart using the male/female series already in the data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# ---------------------------------------------------------
# 1. Load and inspect the data
# ---------------------------------------------------------
raw = pd.read_csv("world_population.csv")

print("Raw shape:", raw.shape)
print("Series Name values:", raw["Series Name"].unique().tolist())
print("Missing values total:", raw.isnull().sum().sum())

# The file stacks 5 different series per country (total/male/female
# population, and male/female %). We must filter to ONE series at a time
# before analyzing — otherwise counts get mixed across series.
total_pop = raw[raw["Series Name"] == "Population, total"][["Country Name", "2022"]]
total_pop = total_pop.rename(columns={"2022": "Population_2022"}).dropna()

print("\nAfter filtering to 'Population, total':", total_pop.shape)
print(total_pop.head())

# ---------------------------------------------------------
# 2. BAR CHART — Top 15 most populous countries (categorical: Country)
# ---------------------------------------------------------
top15 = total_pop.sort_values("Population_2022", ascending=False).head(15)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=top15,
    x="Population_2022",
    y="Country Name",
    hue="Country Name",
    palette="viridis",
    legend=False,
)
plt.title("Top 15 Most Populous Countries (2022)", fontsize=14, fontweight="bold")
plt.xlabel("Population")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("output/top15_population_bar_chart.png", dpi=150)
plt.close()
print("\nSaved output/top15_population_bar_chart.png")

# ---------------------------------------------------------
# 3. HISTOGRAM — Distribution of total population across all countries
# ---------------------------------------------------------
# A histogram bins the continuous population values into ranges, revealing
# the overall SHAPE of the distribution (most countries are small; a few
# are extremely large — hence the log scale on the x-axis).
plt.figure(figsize=(9, 5.5))
sns.histplot(total_pop["Population_2022"], bins=30, color="#4C72B0", log_scale=(True, False))
plt.title("Distribution of Country Populations Worldwide (2022)", fontsize=14, fontweight="bold")
plt.xlabel("Population (log scale)")
plt.ylabel("Number of Countries")
plt.tight_layout()
plt.savefig("output/population_distribution_histogram.png", dpi=150)
plt.close()
print("Saved output/population_distribution_histogram.png")

# ---------------------------------------------------------
# 4. BONUS BAR CHART — World male vs female population (categorical: Gender)
# ---------------------------------------------------------
male_pop = raw[raw["Series Name"] == "Population, male"]["2022"].sum()
female_pop = raw[raw["Series Name"] == "Population, female"]["2022"].sum()

gender_df = pd.DataFrame({
    "Gender": ["Male", "Female"],
    "Population": [male_pop, female_pop]
})

plt.figure(figsize=(6, 5))
sns.barplot(data=gender_df, x="Gender", y="Population", hue="Gender", palette="Set2", legend=False)
plt.title("World Population by Gender (2022)", fontsize=14, fontweight="bold")
plt.ylabel("Total Population")
for i, v in enumerate(gender_df["Population"]):
    plt.text(i, v + v * 0.01, f"{v:,.0f}", ha="center", fontweight="bold")
plt.tight_layout()
plt.savefig("output/gender_distribution_bar_chart.png", dpi=150)
plt.close()
print("Saved output/gender_distribution_bar_chart.png")

# ---------------------------------------------------------
# 5. Summary
# ---------------------------------------------------------
print("\nSummary statistics (2022 total population, all countries):")
print(total_pop["Population_2022"].describe())
print(f"\nMost populous: {top15.iloc[0]['Country Name']} ({top15.iloc[0]['Population_2022']:,.0f})")
print(f"World male population 2022: {male_pop:,.0f}")
print(f"World female population 2022: {female_pop:,.0f}")
print("Done!")
