import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Colors for quadrants
colors = ['#e8f4f8', '#fdf2e9', '#f4f6f7', '#fbeee6']
# Add colored quadrants
ax.add_patch(patches.Rectangle((-10, 0), 10, 10, facecolor=colors[0], alpha=0.7)) # Top-Left
ax.add_patch(patches.Rectangle((0, 0), 10, 10, facecolor=colors[1], alpha=0.7))  # Top-Right
ax.add_patch(patches.Rectangle((-10, -10), 10, 10, facecolor=colors[2], alpha=0.7)) # Bottom-Left
ax.add_patch(patches.Rectangle((0, -10), 10, 10, facecolor=colors[3], alpha=0.7))  # Bottom-Right

# Axes lines
ax.axhline(0, color='black', linewidth=2)
ax.axvline(0, color='black', linewidth=2)

# Labels
ax.set_xlabel('<-- Αμυντική Τακτική (Defenders)      |      Επιθετική Τακτική (Attackers) -->', fontsize=14, fontweight='bold', labelpad=20)
ax.set_ylabel('<-- Αρχάριοι (Novice)      |      Έμπειροι (Elite) -->', fontsize=14, fontweight='bold', labelpad=20)
ax.set_title('Matrix Στρατηγικών Προφίλ (K-Means) & Τακτικής Συνέργειας (Apriori)', fontsize=18, fontweight='bold', pad=20)

# Quadrant 1: Elite Defenders (Top-Left)
ax.text(-5, 6, 'Cluster 0: Veteran Roamers\n(25% του πληθυσμού)', ha='center', va='center', fontsize=14, fontweight='bold', color='#2980b9')
ax.text(-5, 2, 'Apriori Rule:\n[Jager] -> [Bandit] (Conf: 85%)\nΙσχυρό Αμυντικό Backbone', ha='center', va='center', fontsize=11, style='italic', bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5'))

# Quadrant 2: Elite Attackers (Top-Right)
ax.text(5, 6, 'Cluster 1: Elite Tacticians\n(5% του πληθυσμού - 65% Win Rate)', ha='center', va='center', fontsize=14, fontweight='bold', color='#d35400')
ax.text(5, 2, 'Apriori Rule:\n[Thermite] -> [Thatcher] (Conf: 92%)\nΑπόλυτη Τακτική Συνέργεια', ha='center', va='center', fontsize=11, style='italic', bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5'))

# Quadrant 3: Novice Defenders (Bottom-Left)
ax.text(-5, -4, 'Cluster 2: Novice Anchors\n(25% του πληθυσμού)', ha='center', va='center', fontsize=14, fontweight='bold', color='#7f8c8d')
ax.text(-5, -8, 'Apriori Rule:\n[Rook] -> [Doc] (Conf: 78%)\nΠαθητική Στατική Άμυνα', ha='center', va='center', fontsize=11, style='italic', bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5'))

# Quadrant 4: Novice Attackers (Bottom-Right)
ax.text(5, -4, 'Cluster 3: Novice Rushers\n(45% του πληθυσμού)', ha='center', va='center', fontsize=14, fontweight='bold', color='#c0392b')
ax.text(5, -8, 'Apriori Rule:\n[Ash] -> [Solo Entry] (Conf: 60%)\nΥψηλή Επιθετικότητα, Μικρή Συνέργεια', ha='center', va='center', fontsize=11, style='italic', bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5'))

ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout()
plt.savefig('../FINAL_IMAGES_FOR_WORD/Fig10_KMeans_Matrix.png', dpi=300, bbox_inches='tight')
