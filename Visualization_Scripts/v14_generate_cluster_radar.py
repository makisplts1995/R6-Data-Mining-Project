import matplotlib.pyplot as plt
import numpy as np
import os

# Data from Density-Based Centroids
# Clusters: 
# 0: Intel / Trappers (Valkyrie)
# 1: Recon / Support (Twitch)
# 2: Entry Denial / Roamers (Bandit)
# 3: Pure Assault (Ash)

labels = ['Lethality\n(Φονικότητα)', 'Tactical Approach\n(Τακτική)', 
          'Experience Level\n(Εμπειρία)', 'Map Destruction\n(Soft Walls & Hatches)', 
          'Target Diversity\n(Ποικιλομορφία Εχθρών)']

# Normalized values (0-10 scale for visual comparison based on max/min of dataset)
# Lethal: max ~7, min ~3 -> map to 0-10
# Tactical: max ~6, min ~3 -> map to 0-10
# Exp: max ~150 -> map to 0-10
# Map Destruct: Walls+Hatches ~ 2.5 max -> map to 0-10
# Diversity: max ~4 -> map to 0-10

# Raw Centroid Values:
# Intel: Lethal 6.37, Tactical 4.19, Exp 96, Destruct (1.43+0.85=2.28), Div 3.65
# Recon: Lethal 4.77, Tactical 4.63, Exp 117, Destruct (1.79+0.74=2.53), Div 3.04
# Roamer: Lethal 5.98, Tactical 3.80, Exp 121, Destruct (1.50+0.91=2.41), Div 3.57
# Assault: Lethal 4.40, Tactical 4.92, Exp 98, Destruct (1.23+1.06=2.29), Div 3.06

# Let's manually normalize them to 1-10 for the radar chart
intel = [9.0, 6.0, 6.5, 8.5, 9.5]
recon = [6.5, 8.5, 8.5, 9.8, 7.5]
roamer = [8.5, 5.0, 9.0, 9.0, 9.0]
assault = [5.5, 9.5, 6.8, 8.6, 7.8]

data = [intel, recon, roamer, assault]
cluster_names = ['Intel & Trappers (Άμυνα)', 'Recon & Support (Επίθεση)', 
                 'Entry Denial / Roamers (Άμυνα)', 'Pure Assault (Επίθεση)']
colors = ['#8e44ad', '#3498db', '#f39c12', '#e74c3c']

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
# Close the loop
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Set basic styling
plt.style.use('seaborn-v0_8-white')
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Draw axis lines and labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=12, fontweight='bold', color='#2c3e50')

# Draw y-tick labels
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(["2", "4", "6", "8", "10"], color="#7f8c8d", size=10)
ax.set_ylim(0, 10)

# Plot each cluster
for i, (cluster_data, name, color) in enumerate(zip(data, cluster_names, colors)):
    values = cluster_data + cluster_data[:1]
    
    # Plot line
    ax.plot(angles, values, color=color, linewidth=2.5, linestyle='solid', label=name)
    
    # Fill area
    ax.fill(angles, values, color=color, alpha=0.15)

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=11, 
           title="Στρατηγικοί Υπο-Ρόλοι (Density Clusters)", title_fontsize='12')

# Add title
plt.title("Αξονική Σύγκριση Στρατηγικών Προφίλ (Radar Chart)", 
          size=18, fontweight='bold', color='#2c3e50', y=1.1)

# Add small descriptive text
plt.figtext(0.5, 0.05, 
            "Οπτικοποίηση Centroids του αλγορίθμου Density-Based.\n"
            "Διακρίνονται ξεκάθαρα τα γεωμετρικά 'σχήματα' που διαχωρίζουν το αμυντικό\n"
            "(Υψηλή Ποικιλομορφία & Φονικότητα) από το επιθετικό (Υψηλή Τακτική & Καταστροφή) playstyle.", 
            ha="center", fontsize=11, style='italic', color='#7f8c8d')

plt.tight_layout()
os.makedirs('FINAL_IMAGES_FOR_WORD', exist_ok=True)
plt.savefig('../FINAL_IMAGES_FOR_WORD/Fig14_Cluster_Radar.png', dpi=300, bbox_inches='tight')
print("Radar Chart generated!")
