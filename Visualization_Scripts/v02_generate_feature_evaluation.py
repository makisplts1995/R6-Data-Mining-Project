import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# =====================================================
# ΑΚΡΙΒΗ ΔΕΔΟΜΕΝΑ από τα αποτελέσματα του χρήστη
# Κανονικοποίηση (Normalization) 0-100 βάσει του μέγιστου κάθε αλγορίθμου
# =====================================================

features = [
    'Exp. Gap', 'Map Name', 'Skill Rank', 'Hatches', 'Floor Level', 
    'Primary Weapon', 'Operator Name', 'Exp. Level', 'Prev. Rnd Deaths', 'Cluster'
]

# === RAW SCORES (ακριβώς όπως τα έδωσε το WEKA) ===

# InfoGain raw: max = 0.00573009 (Experience_Gap)
ig_raw = {
    'Exp. Gap': 0.00573009,
    'Map Name': 0.00012728,
    'Skill Rank': 0.00099558,
    'Hatches': 0,
    'Floor Level': 0,
    'Primary Weapon': 0.00088745,
    'Operator Name': 0.00080154,
    'Exp. Level': 0.00078446,
    'Prev. Rnd Deaths': 0.00005045,
    'Cluster': 0.00038987,
}

# GainRatio raw: max = 0.007386 (Experience_Gap)
gr_raw = {
    'Exp. Gap': 0.007386,
    'Map Name': 0.000666,
    'Skill Rank': 0.000757,
    'Hatches': 0,
    'Floor Level': 0,
    'Primary Weapon': 0.001402,
    'Operator Name': 0.001006,
    'Exp. Level': 0.001195,
    'Prev. Rnd Deaths': 0.001291,
    'Cluster': 0.000393,
}

# ReliefF raw: max = 0.01279535 (Map_Name)
# Negative values treated as 0
rf_raw = {
    'Exp. Gap': 0.00181922,
    'Map Name': 0.01279535,
    'Skill Rank': 0.00214257,
    'Hatches': 0.00517955,
    'Floor Level': 0.00422507,
    'Primary Weapon': 0,  # was -0.00008 (αρνητικό)
    'Operator Name': 0,   # was ~0 (αρνητικό)
    'Exp. Level': 0.00316380,
    'Prev. Rnd Deaths': 0.00100120,
    'Cluster': 0.00090108,
}

# === NORMALIZATION (0-100) ===
ig_max = max(ig_raw.values())
gr_max = max(gr_raw.values())
rf_max = max(rf_raw.values())

infogain = [round(ig_raw[f] / ig_max * 100, 1) for f in features]
gainratio = [round(gr_raw[f] / gr_max * 100, 1) for f in features]
relieff = [round(rf_raw[f] / rf_max * 100, 1) for f in features]

print("InfoGain (normalized):", infogain)
print("GainRatio (normalized):", gainratio)
print("ReliefF (normalized):", relieff)

df = pd.DataFrame({
    'Feature': features,
    'InfoGain': infogain,
    'Gain Ratio': gainratio,
    'ReliefF': relieff
})

# === ΣΧΕΔΙΑΣΗ ===
sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(figsize=(14, 8))

y = np.arange(len(features))
width = 0.25

bars1 = ax.barh(y + width, df['InfoGain'], width, label='Information Gain (Εντροπία)', color='#3498db', edgecolor='white', linewidth=0.5)
bars2 = ax.barh(y, df['Gain Ratio'], width, label='Gain Ratio (Εξισορρόπηση)', color='#2ecc71', edgecolor='white', linewidth=0.5)
bars3 = ax.barh(y - width, df['ReliefF'], width, label='ReliefF (Αλληλεπιδράσεις)', color='#e74c3c', edgecolor='white', linewidth=0.5)

ax.set_yticks(y)
ax.set_yticklabels(features, fontweight='bold', fontsize=12)
ax.set_xlabel('Κανονικοποιημένο Σκορ Σημαντικότητας (0-100%)', fontweight='bold', fontsize=12)
ax.set_title('Συγκριτική Αξιολόγηση Χαρακτηριστικών\nμέσω Τριών Αλγορίθμων Feature Selection', 
             fontsize=18, fontweight='bold', pad=25, color='#2c3e50')

ax.legend(title='Αλγόριθμος Αξιολόγησης', title_fontsize='11', fontsize='10', 
          loc='lower right', framealpha=0.9)

ax.invert_yaxis()
ax.set_xlim(0, 115)  # Χώρος για τα νούμερα
ax.grid(axis='x', linestyle='--', alpha=0.5)

# Προσθήκη τιμών στις μπάρες (μόνο αν > 0)
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        w = bar.get_width()
        if w > 0:
            ax.text(w + 0.8, bar.get_y() + bar.get_height()/2, f'{w:.1f}', 
                    va='center', fontsize=8, color='#555555')

# Highlight: ReliefF Discovery (Geometric Features)
ax.annotate('Ανακάλυψη ReliefF:\nΓεωμετρικά Χαρακτηριστικά', 
            xy=(40, 3.3), xytext=(70, 5.5),
            arrowprops=dict(facecolor='#c0392b', shrink=0.05, width=1.5, headwidth=7, 
                           connectionstyle="arc3,rad=-0.15"),
            fontsize=11, fontweight='bold', color='#c0392b', 
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#e74c3c", lw=1.5))

# Footnote: Normalization explanation
fig.text(0.5, -0.02, 
         '* Τα σκορ κανονικοποιήθηκαν (Min-Max Normalization, 0-100%) ανά αλγόριθμο, '
         'ώστε να καταστεί δυνατή η οπτική σύγκριση μεταξύ μεθόδων με διαφορετικές κλίμακες.',
         ha='center', fontsize=9, fontstyle='italic', color='#7f8c8d',
         bbox=dict(boxstyle='round,pad=0.3', fc='#f8f9fa', ec='#dcdde1', lw=0.5))

plt.tight_layout()
plt.subplots_adjust(bottom=0.08)  # Χώρος για το footnote
output_path = 'c:/Users/30693/Downloads/r6/master_feature_evaluation.png'
plt.savefig('../FINAL_IMAGES_FOR_WORD/Fig02_Feature_Importance.png', dpi=300, bbox_inches='tight')
print(f"\nMaster visualization saved to {output_path}")
