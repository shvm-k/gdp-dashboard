import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="India Wealth Inequality", layout="centered")
st.title("💰 Wealth Distribution in India")
st.markdown("""
This chart shows how India's total wealth is distributed among different income groups.
""")

# Data
groups = ['Bottom 50%', 'Next 40%', 'Next 9%', 'Top 1%']
values = [3.4, 24.1, 32.4, 40.1]
colors = ['#4daf4a', '#377eb8', '#ff7f00', '#e41a1c']

# Plot
fig, ax = plt.subplots()
bars = ax.bar(groups, values, color=colors)

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 1, f"{height}%", ha='center')

ax.set_ylabel("Wealth Share (%)")
ax.set_ylim(0, 50)

st.pyplot(fig)

st.caption("📊 Data: World Inequality Report | Built by Shivam")
