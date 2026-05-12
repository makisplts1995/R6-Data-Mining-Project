import matplotlib.pyplot as plt
import numpy as np
import os

# Data based on real Weka Information Gain metrics (Exact values from results/info_gain)
features = [
    r'$IG(Win | Win\_Streak)$',
    r'$IG(Win | Team\_Score)$',
    r'$IG(Win | Role)$',
    r'$IG(Win | Tactical\_Archetype)$',
    r'$IG(Win | Primary\_Weapon)$',
    r'$IG(Win | Team\_Exp\_Gap)$'
]

# Real IG values from WEKA
info_gain = [0.00000, 0.00000, 0.00031, 0.00039, 0.00088, 0.00573]
colors = ['#c0392b', '#c0392b', '#27ae60', '#27ae60', '#27ae60', '#27ae60']

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(11, 6.5))

# Σχεδιασμός γραφήματος Lollipop
ax.hlines(y=features, xmin=0, xmax=info_gain, color=colors, alpha=0.8, linewidth=3.5)
ax.scatter(info_gain, features, color=colors, s=180, zorder=3, edgecolors='white', linewidth=1.5)

# Προσθήκη ετικετών τιμών
for i, (v, c) in enumerate(zip(info_gain, colors)):
    if v == 0:
        ax.text(v + 0.0001, i, f'{v:.5f} Bits\n(Στατιστικός Θόρυβος)', color=c, va='center', fontweight='bold', fontsize=11)
    else:
        ax.text(v + 0.0001, i, f'{v:.5f} Bits', color='#2c3e50', va='center', fontweight='bold', fontsize=11)

# Ορισμός Τίτλων και Αξόνων
ax.set_title('Μαθηματική Απόδειξη: Information Gain (Entropy Reduction)', fontsize=16, fontweight='bold', color='#2c3e50', pad=20)
ax.set_xlabel('Information Gain σε Bits (Αποκοπή Αβεβαιότητας)', fontsize=13, fontweight='bold', color='#34495e')
ax.set_xlim(-0.0001, 0.0065)
ax.tick_params(axis='y', labelsize=13, colors='#2c3e50')
ax.tick_params(axis='x', labelsize=11, colors='#2c3e50')
ax.grid(True, linestyle='--', alpha=0.5, color='#bdc3c7')

# Add background shading to categorize the variables
ax.axhspan(-0.5, 1.5, color='#e74c3c', alpha=0.08)
ax.axhspan(1.5, 5.5, color='#27ae60', alpha=0.08)

# Add group labels
ax.text(0.005, 0.5, 'ΨΥΧΟΛΟΓΙΚΑ\nΧΑΡΑΚΤΗΡΙΣΤΙΚΑ\n(Μηδενικό Κέρδος)', fontsize=11, fontweight='bold', color='#c0392b', ha='center', va='center', 
        bbox=dict(facecolor='white', alpha=0.9, edgecolor='#c0392b', boxstyle='round,pad=0.4'))
ax.text(0.005, 3.5, 'ΤΑΚΤΙΚΑ\nΧΑΡΑΚΤΗΡΙΣΤΙΚΑ\n(Μέγιστο Κέρδος)', fontsize=11, fontweight='bold', color='#27ae60', ha='center', va='center', 
        bbox=dict(facecolor='white', alpha=0.9, edgecolor='#27ae60', boxstyle='round,pad=0.4'))

plt.tight_layout()
os.makedirs('FINAL_IMAGES_FOR_WORD', exist_ok=True)
plt.savefig('../FINAL_IMAGES_FOR_WORD/Fig07_Tactics_vs_Psychology.png', dpi=300, bbox_inches='tight')
print("Math lollipop chart generated!")
