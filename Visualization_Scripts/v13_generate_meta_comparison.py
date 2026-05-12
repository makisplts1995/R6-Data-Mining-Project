import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def draw_box(ax, x, y, title, subtitle, pct, color):
    """Draws a styled box with text for the cluster"""
    # Background Box
    box = patches.FancyBboxPatch((x, y), 3.0, 1.2, 
                                 boxstyle="round,pad=0.1,rounding_size=0.15",
                                 facecolor=color, edgecolor='white', lw=2, alpha=0.9, zorder=3)
    # Add shadow
    shadow = patches.FancyBboxPatch((x+0.05, y-0.05), 3.0, 1.2, 
                                 boxstyle="round,pad=0.1,rounding_size=0.15",
                                 facecolor='gray', alpha=0.3, zorder=2)
    ax.add_patch(shadow)
    ax.add_patch(box)
    
    # Texts
    ax.text(x + 1.5, y + 0.8, title, ha='center', va='center', fontsize=10, fontweight='bold', color='white', zorder=4)
    ax.text(x + 1.5, y + 0.45, subtitle, ha='center', va='center', fontsize=8, color='white', zorder=4)
    ax.text(x + 1.5, y + 0.15, f"Πληθυσμός: {pct}%", ha='center', va='center', fontsize=9, fontweight='bold', color='#f1c40f', zorder=4)

fig, ax = plt.subplots(figsize=(18, 11))
ax.set_xlim(-1.0, 17.0)
ax.set_ylim(-3.5, 8.5)
ax.axis('off')

# Set background color
fig.patch.set_facecolor('#fdfefe')

# Main Title
ax.text(8.25, 7.5, 'Ολιστική Μετα-Ανάλυση Αλγορίθμων Συσταδοποίησης (4 Μοντέλα)', 
        ha='center', va='center', fontsize=18, fontweight='bold', color='#2c3e50')
ax.text(8.25, 7.1, 'Εξέλιξη της Ανάλυσης: K-Means -> Hierarchical -> EM -> Density-Based', 
        ha='center', va='center', fontsize=12, style='italic', color='#7f8c8d')

# X positions for the 4 columns
col1_x = 0.5
col2_x = 4.5
col3_x = 8.5
col4_x = 12.5

# Headers for columns
ax.text(col1_x + 1.5, 6.2, 'K-Means (KDE)\n[Προφίλ Απόδοσης]', ha='center', va='center', fontsize=12, fontweight='bold', color='#27ae60')
ax.text(col2_x + 1.5, 6.2, 'Hierarchical (Ward)\n[Οικοσύστημα Παικτών]', ha='center', va='center', fontsize=12, fontweight='bold', color='#e67e22')
ax.text(col3_x + 1.5, 6.2, 'Expectation-Maximization\n[Μακρο-Ρόλοι]', ha='center', va='center', fontsize=12, fontweight='bold', color='#2980b9')
ax.text(col4_x + 1.5, 6.2, 'Density-Based (MakeDensity)\n[Τακτικοί Υπο-Ρόλοι]', ha='center', va='center', fontsize=12, fontweight='bold', color='#8e44ad')

# Draw column dividers
ax.plot([4, 4], [0.5, 6.5], color='#bdc3c7', linestyle='--', lw=1.5)
ax.plot([8, 8], [0.5, 6.5], color='#bdc3c7', linestyle='--', lw=1.5)
ax.plot([12, 12], [0.5, 6.5], color='#bdc3c7', linestyle='--', lw=1.5)

# ----------------- COLUMN 1: K-MEANS -----------------
draw_box(ax, col1_x, 4.5, "Lethal Novices", "(Υψηλή Φονικότητα)", 25, "#27ae60")
draw_box(ax, col1_x, 3.1, "Tactical Veterans", "(Υψηλή Τακτική)", 25, "#27ae60")
draw_box(ax, col1_x, 1.7, "Elite Tacticians", "(Ισορροπημένα Υψηλό)", 5, "#27ae60")
draw_box(ax, col1_x, 0.3, "The Expendables", "(Αρχάριοι & Αδύναμοι)", 45, "#7f8c8d")

# ----------------- COLUMN 2: HIERARCHICAL -----------------
draw_box(ax, col2_x, 4.5, "Mainstream Player", "(Τυπικές Στρατηγικές)", 50, "#e67e22")
draw_box(ax, col2_x, 3.1, "Support / Anchor", "(Αμυντική Προσέγγιση)", 28, "#e67e22")
draw_box(ax, col2_x, 1.7, "Entry Fraggers", "(Άκρως Επιθετικοί)", 13, "#e67e22")
draw_box(ax, col2_x, 0.3, "The Specialists", "(Ιδιαίτερα Μοτίβα)", 9, "#e67e22")

# ----------------- COLUMN 3: EM -----------------
draw_box(ax, col3_x, 4.5, "Defensive Backbone", "(Jager, Bandit, Rook)", 50, "#2980b9")
draw_box(ax, col3_x, 3.1, "Flex / Utility Attack", "(Twitch, Sledge)", 33, "#2980b9")
draw_box(ax, col3_x, 1.7, "Entry Fraggers", "(Ash, Solo Push)", 11, "#2980b9")
draw_box(ax, col3_x, 0.3, "Hard Breachers", "(Thermite, Hibana)", 6, "#2980b9")

# ----------------- COLUMN 4: DENSITY-BASED -----------------
draw_box(ax, col4_x, 4.5, "Pure Assault", "(Ash, R4-C)", 29, "#8e44ad")
draw_box(ax, col4_x, 3.1, "Intel / Trappers", "(Valkyrie, Nitro Cell)", 29, "#8e44ad")
draw_box(ax, col4_x, 1.7, "Recon / Support", "(Twitch, F2)", 21, "#8e44ad")
draw_box(ax, col4_x, 0.3, "Entry Denial", "(Bandit, Barbed Wire)", 21, "#8e44ad")

# Conceptual Connecting Arrows (Left to Right)
arrow_props = dict(arrowstyle="->", color="#bdc3c7", lw=2, alpha=0.5, connectionstyle="arc3,rad=0.0")

y_pos = [5.1, 3.7, 2.3, 0.9]
for y in y_pos:
    ax.annotate("", xy=(col2_x, y), xytext=(col1_x + 3.0, y), arrowprops=arrow_props)
    ax.annotate("", xy=(col3_x, y), xytext=(col2_x + 3.0, y), arrowprops=arrow_props)
    ax.annotate("", xy=(col4_x, y), xytext=(col3_x + 3.0, y), arrowprops=arrow_props)

# --- APRIORI MATCHES FOOTER ---
# Draw a large footer box for Apriori Confirmations
footer_y = -3.2
footer_h = 2.6
footer_box = patches.FancyBboxPatch((-0.5, footer_y), 17.0, footer_h, 
                             boxstyle="round,pad=0.1,rounding_size=0.15",
                             facecolor='#34495e', edgecolor='#f39c12', lw=2, alpha=0.95, zorder=3)
ax.add_patch(footer_box)

ax.text(8.0, footer_y + 2.1, '[ ΜΑΘΗΜΑΤΙΚΕΣ ΕΠΙΒΕΒΑΙΩΣΕΙΣ ΜΕΣΩ ΚΑΝΟΝΩΝ ΣΥΣΧΕΤΙΣΗΣ APRIORI ]', 
        ha='center', va='center', fontsize=13, fontweight='bold', color='#f1c40f', zorder=4)

# Text for matches
t1 = "1. K-Means (Lethal Novices) ➔ Apriori_1 (Rule #108): [Ash] + [Novice] (Conf: 66%)"
t2 = "2. K-Means (Elite Tacticians) ➔ Apriori_1 (Rule #18): [Thermite Vet] ➔ [Thatcher] (Conf: 50%)"
t3 = "3. EM (Defensive Backbone) ➔ Apriori_2 (Rule #1): [Anchor] + [Roamer] ➔ [Trapper] + [Intel] (Lift: 3.20)"
t4 = "4. Density (Pure Assault) ➔ Apriori_2 (Rule #69): [Assault] ➔ [Demolition] (Lift: 1.18)"

ax.text(8.0, footer_y + 1.5, t1, ha='center', va='center', fontsize=12, color='white', zorder=4)
ax.text(8.0, footer_y + 1.1, t2, ha='center', va='center', fontsize=12, color='white', zorder=4)
ax.text(8.0, footer_y + 0.7, t3, ha='center', va='center', fontsize=12, color='white', zorder=4)
ax.text(8.0, footer_y + 0.3, t4, ha='center', va='center', fontsize=12, color='white', zorder=4)

plt.tight_layout()
os.makedirs('FINAL_IMAGES_FOR_WORD', exist_ok=True)
plt.savefig('../FINAL_IMAGES_FOR_WORD/Fig13_Meta_Comparison.png', dpi=300, bbox_inches='tight')
print("All 4 algorithms comparison chart generated!")
