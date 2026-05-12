import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

plt.style.use('seaborn-v0_8-white')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

def create_apriori_viz(filename, title_text, rules, subtitle, color_theme):
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_facecolor('#fdfefe')
    
    y_pos = np.arange(len(rules))
    confs = [r[1] for r in rules]
    labels = [r[0] for r in rules]
    lifts = [r[2] for r in rules]
    
    bars = ax.barh(y_pos, confs, color=color_theme, edgecolor='white', alpha=0.8, height=0.6)
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=11, fontweight='bold', color='#2c3e50')
    ax.set_xlabel('Confidence (%)', fontsize=12, fontweight='bold')
    ax.set_title(title_text, fontsize=16, fontweight='bold', pad=20, color='#2c3e50')
    
    # Add data labels
    for i, bar in enumerate(bars):
        width = bar.get_width()
        ax.text(width + 1, bar.get_y() + bar.get_height()/2, 
                f'Conf: {width}% | Lift: {lifts[i]}', 
                va='center', fontsize=10, fontweight='bold', color='#34495e')

    ax.invert_yaxis()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    os.makedirs('../FINAL_IMAGES_FOR_WORD', exist_ok=True)
    plt.savefig(f'../FINAL_IMAGES_FOR_WORD/{filename}', dpi=300, bbox_inches='tight')
    plt.close()

# Micro Rules (Operators/Gadgets)
micro_rules = [
    ("Thermite -> Thatcher", 50.1, 1.62),
    ("Thatcher -> Thermite", 33.5, 1.62),
    ("Valkyrie -> Nitro Cell", 72.4, 1.45),
    ("Bandit -> Barbed Wire", 68.2, 1.32),
    ("Ash -> Breach Charge", 45.8, 1.21)
]

# Macro Rules (Tactical/Psychology)
macro_rules = [
    ("Anchor+Roamer -> Trapper+Intel", 68.0, 3.20),
    ("Support_ATK=2 -> Assault=1", 55.0, 1.43),
    ("Recon=2 -> Support_ATK=1", 47.0, 1.36),
    ("Shield=1 -> Assault=1", 45.0, 1.28),
    ("Assault=1 -> Demolition=1", 44.0, 1.18)
]

create_apriori_viz('Fig03_Apriori_Micro_Rules.png', 
                   'Apriori Association Rules: Micro-Tactical (Operators & Gadgets)', 
                   micro_rules, '', '#e67e22')

create_apriori_viz('Fig04_Apriori_Macro_Synergies.png', 
                   'Apriori Association Rules: Macro-Tactical (Role Synergies)', 
                   macro_rules, '', '#2980b9')

print("Apriori visualizations regenerated!")
