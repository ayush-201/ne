# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set professional style and context for presentation
sns.set_style("whitegrid")
sns.set_context("talk")
palette = "muted"

# Generate synthetic data for support response times across channels
np.random.seed(42)  # for reproducibility

channels = ["Email", "Phone", "Chat", "Social Media"]
data = {
    "Support_Channel": np.repeat(channels, 200),
    # Simulate response times (in minutes) with realistic distributions per channel
    "Response_Time": np.concatenate([
        np.random.normal(loc=120, scale=30, size=200),  # Email
        np.random.normal(loc=90, scale=25, size=200),   # Phone
        np.random.normal(loc=60, scale=20, size=200),   # Chat
        np.random.normal(loc=45, scale=15, size=200)    # Social Media
    ])
}

df = pd.DataFrame(data)

# Clip negative times to zero since response times cannot be negative
df["Response_Time"] = df["Response_Time"].clip(lower=0)

# Plot violinplot
plt.figure(figsize=(8, 8))  # 512x512 pixels approx at 64 dpi
ax = sns.violinplot(x="Support_Channel", y="Response_Time", data=df,
                    palette=palette, inner="quartile")

# Titles and labels
ax.set_title("Distribution of Customer Support Response Times by Channel")
ax.set_xlabel("Support Channel")
ax.set_ylabel("Response Time (minutes)")

# Save the figure with exact output size
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
