import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8-white')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

# Data - Keep English titles
labels = [
    'Defensive Backbone\n(Jager, Bandit, Rook)\n50%', 
    'Utility / Flex Attackers\n(Twitch, Sledge, Thatcher)\n33%', 
    'Entry Fraggers\n(Ash)\n11%', 
    'Hard Breachers\n(Thermite, Hibana)\n6%'
]
percentages = [50, 33, 11, 6]
colors = ['#2c3e50', '#2980b9', '#e74c3c', '#d35400']
explode = (0.05, 0.05, 0.05, 0.05) 

fig, ax = plt.subplots(figsize=(14, 9))

# Draw Donut Chart
wedges, texts = ax.pie(
    percentages, 
    colors=colors, 
    explode=explode, 
    labels=labels,
    startangle=140, 
    labeldistance=1.15, # push standard labels a bit further out
    textprops={'fontsize': 11, 'fontweight': 'bold', 'color': '#2c3e50'},
    wedgeprops=dict(width=0.4, edgecolor='white', linewidth=2) 
)

# Center text
plt.text(0, 0, 'Διαχωρισμός\nΡόλων (EM)\n(100% Παικτών)', ha='center', va='center', fontsize=14, fontweight='bold', color='#34495e')

# Create a lot of space for annotations
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-1.5, 1.5)

# 1. Defenders (Wedge 0 - Dark Blue)
# Pie math: 140 to 320 degrees -> midpoint ~ 230 degrees. (Bottom Left)
# Standard label will be bottom-left. We place annotation at Bottom-Right.
ax.annotate('Επιβεβαίωση Apriori:\nΕνιαίο Αμυντικό Meta\n(Jager->Bandit, Rook->Doc)', 
            xy=(-0.5, -0.6), xytext=(1.0, -1.0),
            arrowprops=dict(arrowstyle="-|>", color='#2c3e50', connectionstyle="arc3,rad=0.2", lw=2),
            fontsize=11, fontstyle='italic', color='#2c3e50',
            bbox=dict(boxstyle="round,pad=0.4", fc="#f8f9f9", ec="#2c3e50", lw=1.5))

# 2. Hard Breachers (Wedge 3 - Orange)
# Pie math: 118 to 140 degrees -> midpoint ~ 129 degrees. (Top Left)
# Standard label will be top-left. We place annotation further top-left.
ax.annotate('Επιβεβαίωση Apriori:\nΒασική Συνέργεια Διάσπασης\n(Thermite + Hibana)', 
            xy=(-0.6, 0.6), xytext=(-1.8, 1.2),
            arrowprops=dict(arrowstyle="-|>", color='#d35400', connectionstyle="arc3,rad=0.1", lw=2),
            fontsize=11, fontstyle='italic', color='#d35400',
            bbox=dict(boxstyle="round,pad=0.4", fc="#f8f9f9", ec="#d35400", lw=1.5))

# 3. Entry Fraggers / Ash (Wedge 2 - Red)
# Pie math: 78 to 118 degrees -> midpoint ~ 98 degrees. (Top Center/Slight Left)
# Standard label will be top. We place annotation Top-Right.
ax.annotate('Επιβεβαίωση Apriori:\nΑπομονωμένο Solo Entry\n(Ash)', 
            xy=(-0.1, 0.8), xytext=(1.0, 1.2),
            arrowprops=dict(arrowstyle="-|>", color='#e74c3c', connectionstyle="arc3,rad=-0.2", lw=2),
            fontsize=11, fontstyle='italic', color='#e74c3c',
            bbox=dict(boxstyle="round,pad=0.4", fc="#f8f9f9", ec="#e74c3c", lw=1.5))

ax.set_title('Ανακάλυψη Υπο-πληθυσμών & Εξειδικευμένων Ρόλων (Αλγόριθμος EM)', 
             fontsize=16, fontweight='bold', pad=20, color='#2c3e50')

plt.tight_layout()
plt.savefig('../FINAL_IMAGES_FOR_WORD/Fig11_EM_Donut.png', dpi=300, bbox_inches='tight')
