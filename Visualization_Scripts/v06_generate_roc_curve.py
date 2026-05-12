import matplotlib.pyplot as plt
import numpy as np
import os

def parse_arff(filepath):
    fpr = []
    tpr = []
    data_section = False
    with open(filepath, 'r') as f:
        for line in f:
            if line.startswith('@data'):
                data_section = True
                continue
            if data_section and line.strip() and not line.startswith('%'):
                parts = line.strip().split(',')
                try:
                    f_val = float(parts[5])
                    t_val = float(parts[6])
                    fpr.append(f_val)
                    tpr.append(t_val)
                except ValueError:
                    pass
    return fpr, tpr

# Ορισμός Ετικετών
models = {
    'Βέλτιστο Μοντέλο: J48 Cons. (AUC: 0.650)': ('results/j48c.arff', '#27ae60', '-', 3, 0.9),
    'J48 Optimized (AUC: 0.648)': ('results/j48-60.arff', '#f39c12', '--', 2.5, 0.9),
    'Random Forest (Baseline: 0.582)': ('results/rf.arff', '#c0392b', '-.', 2, 0.8)
}

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(11, 8))

# Plot all curves
for label, (path, color, ls, lw, alpha) in models.items():
    if os.path.exists(path):
        fpr, tpr = parse_arff(path)
        if fpr and tpr:
            sorted_indices = np.argsort(fpr)
            fpr = np.array(fpr)[sorted_indices]
            tpr = np.array(tpr)[sorted_indices]
            ax.plot(fpr, tpr, label=label, color=color, linestyle=ls, linewidth=lw, alpha=alpha)

# Random guess line
ax.plot([0, 1], [0, 1], color='#7f8c8d', linestyle=':', linewidth=1.5, label='Τυχαία Πρόβλεψη (AUC: 0.500)')

# Styling
ax.set_title('Καμπύλη ROC: Τακτική Υπεροχή έναντι Τυχαιότητας', fontsize=18, fontweight='bold', pad=20, color='#2c3e50')
ax.set_xlabel('False Positive Rate (1 - Specificity)', fontsize=13, fontweight='bold', color='#34495e')
ax.set_ylabel('True Positive Rate (Sensitivity)', fontsize=13, fontweight='bold', color='#34495e')
ax.set_xlim([0.0, 1.0])
ax.set_ylim([0.0, 1.05])
ax.tick_params(axis='both', labelsize=11, colors='#2c3e50')
ax.grid(True, linestyle='--', alpha=0.5, color='#bdc3c7')

# Legend styling
legend = ax.legend(loc="lower right", fontsize=12, frameon=True, shadow=True, facecolor='white', edgecolor='#bdc3c7')
plt.setp(legend.get_texts(), color='#2c3e50')

# --- THE Βασικά Στοιχεία Γραφήματος: INSET ZOOM ---
# Create an inset axes to zoom in on the 'elbow' where models diverge
axins = ax.inset_axes([0.15, 0.50, 0.35, 0.35])
axins.set_facecolor('#f8f9fa')

for label, (path, color, ls, lw, alpha) in models.items():
    if os.path.exists(path):
        fpr, tpr = parse_arff(path)
        if fpr and tpr:
            sorted_indices = np.argsort(fpr)
            fpr = np.array(fpr)[sorted_indices]
            tpr = np.array(tpr)[sorted_indices]
            axins.plot(fpr, tpr, color=color, linestyle=ls, linewidth=lw, alpha=alpha)

# Zoom box limits
x1, x2 = 0.20, 0.45
y1, y2 = 0.35, 0.60
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
axins.tick_params(colors='#2c3e50', labelsize=9)
axins.grid(True, linestyle=':', alpha=0.6, color='#bdc3c7')

# Draw lines connecting the inset to the main plot
ax.indicate_inset_zoom(axins, edgecolor="#34495e", alpha=0.6, linewidth=1.5)

# Fill the specific area between the random guess (diagonal) and the optimal curve
try:
    fpr_opt, tpr_opt = parse_arff('results/j48c.arff')
    sorted_indices = np.argsort(fpr_opt)
    fpr_opt = np.array(fpr_opt)[sorted_indices]
    tpr_opt = np.array(tpr_opt)[sorted_indices]
    
    # Fill between the curve (tpr_opt) and the diagonal (fpr_opt)
    ax.fill_between(fpr_opt, tpr_opt, fpr_opt, alpha=0.15, color='#27ae60')
    
    # Add a bold annotation pointing to this "gained" area, moved right to avoid the zoom box
    ax.annotate('ΤΑΚΤΙΚΟ ΠΛΕΟΝΕΚΤΗΜΑ\n(Στατιστικό Κέρδος έναντι Τυχαιότητας)', 
                xy=(0.55, 0.65), xytext=(0.75, 0.85),
                arrowprops=dict(facecolor='#27ae60', shrink=0.05, width=2, headwidth=8),
                fontsize=11, fontweight='bold', color='#27ae60', ha='center',
                bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#27ae60", lw=2))
except:
    pass

plt.tight_layout()
os.makedirs('FINAL_IMAGES_FOR_WORD', exist_ok=True)
plt.savefig('../FINAL_IMAGES_FOR_WORD/Fig06_ROC_Curve.png', dpi=300, bbox_inches='tight')
print("Τελικό ROC Curve generated!")
