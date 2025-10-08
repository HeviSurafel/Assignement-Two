
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# ============================================================
# Task 1: Load and Explore the Dataset
# ============================================================

try:
    # Load the Iris dataset from sklearn
    iris_data = load_iris()

    # Create DataFrame
    df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
    df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)

    # Display first few rows
    print("🔹 First five rows of the dataset:")
    display(df.head())

    # Check dataset structure
    print("\n🔹 Dataset Information:")
    df.info()

    # Check for missing values
    print("\n🔹 Missing Values:")
    print(df.isnull().sum())

    # Handle missing values (if any)
    df.fillna(df.mean(numeric_only=True), inplace=True)
    print("\n✅ Missing values handled successfully (none found in this dataset).")

except FileNotFoundError:
    print("❌ Error: File not found. Please ensure the dataset exists.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")

# ============================================================
# Task 2: Basic Data Analysis
# ============================================================

print("\n📊 Basic Statistical Summary:")
display(df.describe())

# Group by species and find mean of numeric columns
grouped = df.groupby('species').mean(numeric_only=True)
print("\n🔹 Mean values grouped by species:")
display(grouped)

# Simple insights
print("\n💡 Observations:")
print("- Setosa species generally have smaller petals and sepals.")
print("- Virginica species have the largest petals.")
print("- Versicolor values fall in between.\n")

# ============================================================
# Task 3: Data Visualization
# ============================================================

sns.set(style="whitegrid")

# (1) Line Chart - Sepal Length Trend
plt.figure(figsize=(8,4))
plt.plot(df['sepal length (cm)'], color='teal', label='Sepal Length')
plt.title("Line Chart - Sepal Length Trend")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# (2) Bar Chart - Average Petal Length per Species
plt.figure(figsize=(6,4))
sns.barplot(x='species', y='petal length (cm)', data=df, palette='viridis')
plt.title("Bar Chart - Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# (3) Histogram - Sepal Width Distribution
plt.figure(figsize=(6,4))
plt.hist(df['sepal width (cm)'], bins=15, color='orange', edgecolor='black')
plt.title("Histogram - Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# (4) Scatter Plot - Sepal Length vs Petal Length
plt.figure(figsize=(6,4))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, palette='cool')
plt.title("Scatter Plot - Sepal vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title='Species')
plt.show()

print("✅ All visualizations generated successfully!")

# ============================================================
# Task 4: Findings and Observations
# ============================================================

print("""
📋 Key Findings:
1. The dataset is clean with no missing values.
2. The Setosa species have significantly smaller petals.
3. Virginica shows the largest petal and sepal dimensions.
4. Positive correlation exists between sepal and petal lengths.
""")
