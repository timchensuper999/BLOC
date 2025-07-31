from bloc_core import add_to_cluster
from steme_core import embed
memories = [
    {"content": "I believe in freedom", "importance": 0.9},
    {"content": "Order must be preserved", "importance": 0.8},
    {"content": "Everyone deserves autonomy", "importance": 0.7}
]

clusters = [{
        'name': "Freedom",
        'centroid': embed("I support freedom"),
        'net_importance': 0
    }]
meta_clusters = [
    # Core Values
    "Freedom", "Order", "Equality", "Justice", "Authority",
    "Discipline", "Autonomy", "Loyalty", "Obedience", "Responsibility",
    
    # Social & Ethical Norms
    "Honesty", "Trust", "Respect", "Fairness", "Tradition",
    "Conformity", "Rebellion", "Integrity", "Compassion", "Tolerance",

    # Emotionally Charged Beliefs
    "Fear", "Hope", "Anger", "Love", "Shame",
    "Pride", "Envy", "Guilt", "Gratitude", "Disgust",

    # Political/Ideological Anchors
    "Democracy", "Meritocracy", "Anarchy", "Technocracy", "Collectivism",
    "Individualism", "Nationalism", "Capitalism", "Socialism", "Liberalism",

    # Philosophical / Abstract
    "Truth", "Meaning", "Purpose", "Faith", "Doubt",
    "Control", "Chaos", "Growth", "Sacrifice", "Power",

    # Action-Oriented
    "Protection", "Creation", "Destruction", "Escape", "Control"
]
for mem in memories:
    add_to_cluster(mem, clusters,meta_clusters,0.7)

print("\nClustered Memory:")
for c in clusters:
    print("Cluster Name: ",c['name'], " | Cluster Centroid: ", c['centroid'][:3], " | Cluster Importance: ",c['net_importance'])
