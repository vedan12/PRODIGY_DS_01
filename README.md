# PRODIGY_DS_01 — Data Visualization: Bar Chart & Histogram

**Prodigy InfoTech — Data Science Internship, Task 01**

## Task
Create a bar chart or histogram to visualize the distribution of a categorical
or continuous variable, such as the distribution of ages or genders in a
population.

## Dataset
`world_population.csv` — the official sample dataset provided by Prodigy
InfoTech for this task. It contains World Bank population data for 217
countries/territories from 2001 to 2022, with 5 series per country: total
population, male population, female population, and male/female % of total.

## Approach
| Variable | Type | Chart used | Why |
|---|---|---|---|
| Country (2022 population) | Categorical | Bar chart | Top 15 most populous countries, ranked |
| Country population (all 217) | Continuous | Histogram (log scale) | Shows the overall shape of the global population distribution |
| Gender (world total, 2022) | Categorical | Bar chart (bonus) | Uses the male/female series already present in the dataset |

## Files
- `task1_visualization.py` — loads, cleans, and visualizes the data
- `world_population.csv` — the provided dataset
- `output/top15_population_bar_chart.png` — bar chart of top 15 countries
- `output/population_distribution_histogram.png` — histogram of all countries' populations
- `output/gender_distribution_bar_chart.png` — bonus bar chart of world male vs. female population

## How to run
```bash
pip install pandas matplotlib seaborn
python task1_visualization.py
```

## Data Cleaning Note
The raw CSV stacks 5 different series per country in the same table (identified
by the `Series Name` column). Before analysis, the data is **filtered to one
series at a time** (e.g. `"Population, total"`) — without this step, counts
from different series get mixed together and produce incorrect results.

## Key Insights
- **India (1.417B)** narrowly overtook **China (1.412B)** as the world's most
  populous country by 2022.
- The **population distribution across all 217 countries is heavily
  right-skewed** — most countries have a modest population (under ~30M),
  while a small handful of countries (India, China, USA...) account for a
  disproportionate share of the world's people. A log scale on the x-axis
  makes this shape visible.
- The global gender split is close to even: **~3.99B male vs. ~3.94B
  female** in 2022.

---
*Part of the Data Science Internship @ Prodigy InfoTech (Oct 2026)*
#ProdigyInfoTech
