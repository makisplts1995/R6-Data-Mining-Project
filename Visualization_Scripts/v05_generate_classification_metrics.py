import matplotlib.pyplot as plt
import numpy as np

# THE FINAL CHAMPION RESULTS
classifiers = ['J48 Cons. (Tuned)', 'J48 Optimized', 'AdaBoost (J48)', 'Random Forest', 'Naive Bayes']
accuracy = [60.78, 60.48, 57.10, 52.41, 51.78]
kappa = [0.2155, 0.2096, 0.1304, 0.0482, 0.0356]

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax1 = plt.subplots(figsize=(13, 7))

# Ορισμός Χρωμάτων: Emerald for the Champion, varying shades for the rest
colors = ['#2ecc71', '#16a085', '#f39c12', '#e67e22', '#c0392b']

x = np.arange(len(classifiers))
width = 0.5
bars = ax1.bar(x, accuracy, width, color=colors, edgecolor='black', linewidth=1.2, alpha=0.9)

ax1.set_ylabel('Ακρίβεια Πρόβλεψης (%)', fontsize=14, fontweight='bold', color='#2c3e50')
ax1.set_ylim(45, 66)  # Adjusted for the 60.78% peak
ax1.set_xticks(x)
ax1.set_xticklabels(classifiers, fontsize=11, fontweight='bold')
ax1.tick_params(axis='y', labelsize=12)

# Add value labels above bars
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.3,
             f'{height:.2f}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

# Kappa line on secondary axis
ax2 = ax1.twinx()
ax2.plot(x, kappa, color='#2980b9', marker='D', markersize=10, linewidth=3, linestyle='--', label='Kappa Statistic')
ax2.set_ylabel('Δείκτης Cohen\'s Kappa', fontsize=14, fontweight='bold', color='#2980b9')
ax2.set_ylim(0, 0.35)
ax2.tick_params(axis='y', labelsize=12, colors='#2980b9')

plt.title('Τελική Συγκριτική Αξιολόγηση Μοντέλων', fontsize=18, fontweight='bold', pad=20, color='#34495e')
ax1.axhline(y=50, color='gray', linestyle=':', linewidth=2, label='Τυχαία Πιθανότητα (50%)')

# Annotation for the final champion
ax1.annotate('ΒΕΛΤΙΣΤΟ ΜΟΝΤΕΛΟ:\n+10.78% Στατιστικό Πλεονέκτημα\n(J48 Consolidated)', xy=(0, 61), xytext=(1.5, 64),
            arrowprops=dict(facecolor='#2ecc71', shrink=0.05, width=2, headwidth=8),
            fontsize=12, fontweight='bold', color='#27ae60', ha='center',
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#2ecc71", lw=2))

ax1.legend(loc='upper right', bbox_to_anchor=(0.95, 0.95))
ax2.legend(loc='upper right', bbox_to_anchor=(0.95, 0.88))

plt.tight_layout()
plt.savefig('../FINAL_IMAGES_FOR_WORD/Fig05_Classification_Metrics.png', dpi=300, bbox_inches='tight')
print("GRAND FINALE GRAPH GENERATED: 60.78%")
