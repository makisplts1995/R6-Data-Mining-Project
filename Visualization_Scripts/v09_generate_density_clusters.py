import matplotlib.pyplot as plt
import numpy as np
import os

plt.style.use('seaborn-v0_8-white')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

# Data from Density-Based Clustering
labels = [
    'Intel & Trappers\n(Valkyrie, Nitro Cell)\n29%', 
    'Pure Assault\n(Ash, R4-C)\n29%', 
    'Entry Denial & Roamers\n(Bandit, Barbed Wire)\n21%', 
    'Recon & Support\n(Twitch, F2)\n21%'
]
percentages = [29, 29, 21, 21]
colors = ['#8e44ad', '#e74c3c', '#f39c12', '#3498db'] # Purple, Red, Orange, Blue
explode = (0.05, 0.05, 0.05, 0.05) 

fig, ax = plt.subplots(figsize=(14, 9))

# Draw Donut Chart
wedges, texts = ax.pie(
    percentages, 
    colors=colors, 
    explode=explode, 
    labels=labels,
    startangle=90, 
    labeldistance=1.15, 
    textprops={'fontsize': 11, 'fontweight': 'bold', 'color': '#2c3e50'},
    wedgeprops=dict(width=0.4, edgecolor='white', linewidth=2) 
)

# Center text
plt.text(0, 0, 'Συσταδοποίηση\nΠυκνότητας\n(Density-Based)', ha='center', va='center', fontsize=14, fontweight='bold', color='#34495e')

# Create a lot of space for annotations
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-1.5, 1.5)

# Annotations linking to Apriori
# 1. Valkyrie (Purple)
ax.annotate('Επιβεβαίωση Apriori:\nΙσχυρή σύνδεση Valkyrie\nμε Nitro Cell', 
            xy=(-0.5, 0.6), xytext=(-1.5, 1.2),
            arrowprops=dict(arrowstyle="-|>", color='#8e44ad', connectionstyle="arc3,rad=0.2", lw=2),
            fontsize=11, fontstyle='italic', color='#8e44ad',
            bbox=dict(boxstyle="round,pad=0.4", fc="#f8f9f9", ec="#8e44ad", lw=1.5))

# 2. Ash (Red)
ax.annotate('Επιβεβαίωση Apriori:\nAsh και R4-C αποτελούν\nτον απόλυτο Entry πυρήνα', 
            xy=(0.6, 0.5), xytext=(1.0, 1.2),
            arrowprops=dict(arrowstyle="-|>", color='#e74c3c', connectionstyle="arc3,rad=-0.2", lw=2),
            fontsize=11, fontstyle='italic', color='#e74c3c',
            bbox=dict(boxstyle="round,pad=0.4", fc="#f8f9f9", ec="#e74c3c", lw=1.5))

# 3. Bandit (Orange)
ax.annotate('Επιβεβαίωση Apriori:\nBandit και Barbed Wire\nως βασική άμυνα', 
            xy=(0.5, -0.6), xytext=(1.0, -1.2),
            arrowprops=dict(arrowstyle="-|>", color='#f39c12', connectionstyle="arc3,rad=0.2", lw=2),
            fontsize=11, fontstyle='italic', color='#f39c12',
            bbox=dict(boxstyle="round,pad=0.4", fc="#f8f9f9", ec="#f39c12", lw=1.5))

# 4. Twitch (Blue)
ax.annotate('Επιβεβαίωση Apriori:\nTwitch + Recon = \nΑπόλυτος Support ρόλος', 
            xy=(-0.6, -0.5), xytext=(-1.5, -1.2),
            arrowprops=dict(arrowstyle="-|>", color='#3498db', connectionstyle="arc3,rad=-0.2", lw=2),
            fontsize=11, fontstyle='italic', color='#3498db',
            bbox=dict(boxstyle="round,pad=0.4", fc="#f8f9f9", ec="#3498db", lw=1.5))

ax.set_title('Ανακάλυψη Υπο-ρόλων & Σύνδεση με Κανόνες Συσχέτισης (Density-Based)', 
             fontsize=16, fontweight='bold', pad=20, color='#2c3e50')

plt.tight_layout()
os.makedirs('FINAL_IMAGES_FOR_WORD', exist_ok=True)
plt.savefig('../FINAL_IMAGES_FOR_WORD/Fig09_Density_Clusters.png', dpi=300, bbox_inches='tight')
print("Density Clusters chart generated!")
