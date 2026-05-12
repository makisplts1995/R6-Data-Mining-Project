import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.style.use('seaborn-v0_8-white')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

fig, ax = plt.subplots(figsize=(12, 7))
ax.axis('off')
ax.text(0.5, 0.85, 'Οι κάτωθι ανεξάρτητες μεταβλητές έλαβαν μηδενικό σκορ (0.0) κατά την αξιολόγηση Εντροπίας (InfoGain)\\nκαι απορρίφθηκαν προκειμένου να διασφαλιστεί η ευρωστία του μοντέλου.', 
        ha='center', va='center', fontsize=11, fontstyle='italic', color='#7f8c8d')

# Only 3 truly rejected features
rejected = [
    ("Win_Streak", "Απουσία\nΑυτοσυσχέτισης", "Οι διαδοχικές νίκες δεν παρουσιάζουν στατιστικά σημαντική εξάρτηση\nμε το αποτέλεσμα του επόμενου γύρου. Η χρήση της μεταβλητής\nθα εισήγαγε στο μοντέλο στατιστική μεροληψία (Σφάλμα του Παίκτη)."),
    ("My_Team_Score", "Στοχαστικός\nΘόρυβος", "Ως a priori ιστορικό σκορ προηγούμενων γύρων, παρουσιάζει μηδενική\nτακτική εξάρτηση. Λόγω της χωρικής ασυμμετρίας του παιχνιδιού,\nτο παρελθοντικό σκορ δεν προδικάζει το αποτέλεσμα της τρέχουσας μάχης."),
    ("Opponent_Score", "Απουσία\nΣυσχέτισης", "Ομοίως με το σκορ της ομάδας, η επίδοση στους προηγούμενους γύρους\nδεν αποτελεί αξιόπιστο προγνωστικό δείκτη, αποδεικνύοντας στατιστικά\nότι ο γύρος κρίνεται αποκλειστικά από την τρέχουσα τακτική προσέγγιση."),
]

start_y = 0.74
step_y = 0.186

for i, (feature, reason, desc) in enumerate(rejected):
    y = start_y - (i * step_y)
    
    # Draw a Red X
    ax.text(0.05, y, 'X', ha='center', va='center', fontsize=18, color='#e74c3c', fontweight='bold')
    
    # Feature Name
    ax.text(0.1, y, feature, ha='left', va='center', fontsize=12, fontweight='bold', color='#2c3e50')
    
    # Reason Box
    bbox_props = dict(boxstyle="round,pad=0.4", fc="#fdedec", ec="#e74c3c", lw=1)
    ax.text(0.35, y, reason, ha='center', va='center', fontsize=10, fontweight='bold', color='#c0392b', bbox=bbox_props)
    
    # Description
    ax.text(0.5, y, desc, ha='left', va='center', fontsize=10, color='#34495e', linespacing=1.4)

# ── Transformed (not deleted) ──────────────────────────────────────────
# Separator line
ax.axhline(0.19, color='#bdc3c7', linewidth=0.8, linestyle='--')

ax.text(0.05, 0.16, 'ΜΕΤΑΣΧΗΜΑΤΙΣΜΟΣ', ha='left', va='center', fontsize=10,
        fontweight='bold', color='#2980b9')

ax.text(0.05, 0.11, 'Clearance_Level', ha='left', va='center', fontsize=12,
        fontweight='bold', color='#2c3e50')
bbox_tr = dict(boxstyle='round,pad=0.4', fc='#eaf4fb', ec='#2980b9', lw=1)
ax.text(0.35, 0.11, 'Διακριτοποίηση\n(Discretization)', ha='center', va='center',
        fontsize=10, fontweight='bold', color='#2980b9', bbox=bbox_tr)
ax.text(0.5, 0.11,
        'Μετατράπηκε σε κατηγορική μεταβλητή 5 τιμών (Recruit → Elite)\n'
        'αποκλειστικά για τον ταξινομητή J48. Στο στάδιο του Clustering\n'
        'αντικαταστάθηκε από τη μεταβλητή Experience Gap.',
        ha='left', va='center', fontsize=10, color='#34495e')

# Conclusion
ax.text(0.5, 0.02, 'Κεντρικό Εύρημα: Η μηδενική αξία του ιστορικού καταρρίπτει τον παράγοντα της ψυχολογίας.\nΑποδεικνύεται στατιστικά ότι η νίκη καθορίζεται από την καθαρή τεχνικότητα και την εμπειρία.', 
    ha='center', va='center', fontsize=11, fontweight='bold', color='#27ae60',
        bbox=dict(boxstyle='square,pad=0.5', fc='#e8f8f5', ec='#27ae60', lw=2))

plt.tight_layout()
plt.savefig('../FINAL_IMAGES_FOR_WORD/Fig01_Feature_Graveyard.png', dpi=300, bbox_inches='tight')
