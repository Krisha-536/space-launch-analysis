import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("launches.csv")
plt.style.use("dark_background")

# Data cleaning
df = df[df["success"].notna()]
df["success"] = df["success"].astype(int)

success_counts = df["success"].value_counts().sort_index()

plt.figure()
success_counts.plot(kind="bar", color=["#1f3b73", "#7b2cbf"])
plt.grid(alpha=0.1)
plt.title("Launch Success vs Failure", fontsize=14)
plt.xlabel("0 = Fail, 1 = Success")
plt.ylabel("Count")
plt.show()

plt.figure()
success_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    labels=["Failure", "Success"],
     colors=["#1f3b73", "#7b2cbf"]
)
plt.title("Launch Outcome Distribution", fontsize=14)
plt.ylabel("")
plt.show()

# Success rate calculation
success_rate = df["success"].mean() * 100
print(f"\nOverall Success Rate: {success_rate:.2f}%")

#Top rockets 
rocket_success = df.groupby("rocket")["success"].mean()
top_rockets = rocket_success.sort_values(ascending=False).head(10)

plt.figure()
top_rockets.plot(kind="bar", color="#3a0ca3")
plt.grid(alpha=0.1)
plt.title("Top 10 Rockets by Success Rate", fontsize=14)
plt.xlabel("Rocket")
plt.ylabel("Success Rate")
plt.xticks(rotation=45)
plt.show()

# Trend over time
df["date_utc"] = pd.to_datetime(df["date_utc"])
df["year"] = df["date_utc"].dt.year

yearly_success = df.groupby("year")["success"].mean()

plt.figure()
yearly_success.plot(marker="o", color="#c77dff")
plt.grid(alpha=0.1)
plt.title("Launch Success Rate Over Time", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Success Rate")
plt.show()

plt.figure()
sns.countplot(x="success", data=df, palette=["#1f3b73", "#7b2cbf"])
plt.grid(alpha=0.1)
plt.title("Launch Outcomes Count", fontsize=14)
plt.show()