
import matplotlib.pyplot as plt

# Data from our cluster analysis
labels = ['Novice Rushers (45%)', 'Veteran Roamers (25%)', 'Novice Anchors (25%)', 'Elite Tacticians (5%)']
sizes = [45, 25, 25, 5]
colors = ['#f1c40f', '#34495e', '#e74c3c', '#2ecc71']
explode = (0.05, 0.05, 0.05, 0.2)  # Explode the 'Elite' slice

# Styling
plt.figure(figsize=(10, 7))
plt.style.use('seaborn-v0_8-whitegrid')

# Create Pie Chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', 
        shadow=True, startangle=140, pctdistance=0.85, textprops={'fontsize': 12, 'fontweight': 'bold'})

# Draw Circle (to make it a donut)
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Distribution of Strategic Archetypes\nin the R6 Siege Ecosystem', fontsize=16, fontweight='bold', pad=20)
plt.axis('equal')  

plt.savefig('../FINAL_IMAGES_FOR_WORD/Fig08_Clustering_Elbow_Curve.png', dpi=300, bbox_inches='tight')
print("Βασικό donut chart generated: cluster_distribution_pie.png")
