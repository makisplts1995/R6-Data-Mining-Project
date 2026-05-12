import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
import os

def draw_bezier(ax, p1, p2, color, alpha=0.5, lw=4):
    """Draws a bezier curve from p1 to p2"""
    # Control points for a smooth S-curve
    cp1 = (p1[0] + (p2[0] - p1[0]) * 0.5, p1[1])
    cp2 = (p1[0] + (p2[0] - p1[0]) * 0.5, p2[1])
    
    verts = [p1, cp1, cp2, p2]
    codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
    
    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor='none', edgecolor=color, lw=lw, alpha=alpha)
    ax.add_patch(patch)

def draw_box(ax, center_x, center_y, text, width=4, height=0.8, bgcolor='#e8f6f3', text_color='black', edge_color='#bdc3c7'):
    """Draws a rounded rectangle with text"""
    box = patches.FancyBboxPatch((center_x - width/2, center_y - height/2), 
                                 width, height, 
                                 boxstyle="round,pad=0.1,rounding_size=0.2",
                                 facecolor=bgcolor, edgecolor=edge_color, lw=1.5, zorder=3)
    ax.add_patch(box)
    ax.text(center_x, center_y, text, ha='center', va='center', 
            fontsize=10, fontweight='bold', color=text_color, zorder=4)

def draw_apriori(ax, center_x, center_y, text, color='#d35400'):
    """Draws a small Apriori rule box"""
    box = patches.FancyBboxPatch((center_x - 1.5, center_y - 0.4), 
                                 3, 0.8, 
                                 boxstyle="round,pad=0.1,rounding_size=0.1",
                                 facecolor='white', edgecolor=color, lw=1.5, zorder=5)
    ax.add_patch(box)
    ax.text(center_x, center_y, text, ha='center', va='center', 
            fontsize=9, fontweight='bold', color=color, zorder=6)

fig, ax = plt.subplots(figsize=(15, 9))
ax.set_xlim(0, 15)
ax.set_ylim(0, 6)
ax.axis('off')

# Title
ax.text(7.5, 5.5, 'Συγκριτική Διαδραστική Ανάλυση Clustering (Bipartite Mapping)', 
        ha='center', va='center', fontsize=16, fontweight='bold', color='#2c3e50')
ax.text(2.5, 4.8, 'Αλγόριθμος K-Means\n(Προφίλ Απόδοσης)', ha='center', va='center', fontsize=12, fontweight='bold', color='#27ae60')
ax.text(12.5, 4.8, 'Αλγόριθμος Density-Based\n(Εξειδίκευση Υπο-Ρόλων)', ha='center', va='center', fontsize=12, fontweight='bold', color='#2980b9')

# Left side nodes (K-Means)
left_x = 2.5
y_positions = [4, 3, 2, 1]
left_texts = [
    'Lethal Novices\n(Υψηλή Φονικότητα)',
    'Elite Tacticians\n(Ισορροπημένα Υψηλό)',
    'Tactical Veterans\n(Υψηλή Τακτική)',
    'The Expendables\n(Χαμηλά και τα 2)'
]

for y, text in zip(y_positions, left_texts):
    draw_box(ax, left_x, y, text, bgcolor='#eafaf1')

# Right side nodes (Density-Based - REAL DATA)
right_x = 12.5
right_texts = [
    'Pure Assault\n(Ash, R4-C)',
    'Recon / Support\n(Twitch, F2)',
    'Entry Denial / Roamers\n(Bandit, Barbed Wire)',
    'Intel / Trappers\n(Valkyrie, Nitro Cell)'
]

for y, text in zip(y_positions, right_texts):
    draw_box(ax, right_x, y, text, bgcolor='#ebf5fb')

# Connections and Apriori Rules
# 1. Lethal Novices -> Pure Assault
draw_bezier(ax, (left_x + 2, 4), (right_x - 2, 4), '#e74c3c', alpha=0.6, lw=6)
draw_apriori(ax, 7.5, 4.2, 'Κανόνας Apriori:\nΗ Ash επιχειρεί\nαπομονωμένα.')

# 2. Elite Tacticians -> Recon / Support
draw_bezier(ax, (left_x + 2, 3), (right_x - 2, 3), '#f39c12', alpha=0.6, lw=6)
draw_apriori(ax, 7.5, 3.2, 'Κανόνας Apriori:\nΒασική συνέργεια\nDrone & Support.')

# 3. Tactical Veterans -> Entry Denial / Roamers
draw_bezier(ax, (left_x + 2, 2), (right_x - 2, 2), '#95a5a6', alpha=0.6, lw=6)

# 4. The Expendables -> Intel / Trappers
draw_bezier(ax, (left_x + 2, 1), (right_x - 2, 1), '#bdc3c7', alpha=0.6, lw=6)

# Cross connections to show mixing of lower tier players
draw_bezier(ax, (left_x + 2, 2), (right_x - 2, 1), '#bdc3c7', alpha=0.3, lw=4)
draw_bezier(ax, (left_x + 2, 1), (right_x - 2, 2), '#bdc3c7', alpha=0.3, lw=4)

draw_apriori(ax, 7.5, 1.5, 'Κανόνας Apriori:\nΕνιαία Άμυνα\n(Valkyrie/Bandit).')

os.makedirs('FINAL_IMAGES_FOR_WORD', exist_ok=True)
plt.savefig('../FINAL_IMAGES_FOR_WORD/Fig12_Density_Mapping.png', dpi=300, bbox_inches='tight')
print("Bipartite Mapping chart generated!")
