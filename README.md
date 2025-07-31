# BLOC-kit

**“Beliefs are not stored. They are clustered.”**

---

## 🧩 Belief & Label-Oriented Clustering (BLOC)

**BLOC** is a minimal clustering engine for managing belief states, reflections, and memory identity in AI cognition systems. It was designed to support:
- Conceptual clustering of agent memories
- Dynamic identity evolution based on semantic similarity
- Meaning formation through accumulation

It uses cosine similarity over pre-embedded memory content (via [STEME](https://github.com/timchensuper999/STEME) or similar engines).

---

## 🔧 Core API

- `add_to_cluster(memory, clusters)`  
   Adds a new memory to the best-fitting semantic cluster, or creates a new one if no match meets the similarity threshold. Each memory is expected to contain:
   ```python
   {
       "content": "I believe in freedom",
       "importance": 0.9
   }
  ```
Clusters are dynamically updated with:
- Recalculated centroids
- Accumulated importance
- Memory membership

--- 

## 💡 Example Usage
```python
from bloc_core import add_to_cluster

memories = [
    {"content": "I believe in freedom", "importance": 0.9},
    {"content": "Order must be preserved", "importance": 0.8},
    {"content": "Everyone deserves autonomy", "importance": 0.7}
]

clusters = []
for mem in memories:
    clusters = add_to_cluster(mem, clusters)

print("\nClustered Memory:")
for c in clusters:
    print(c['name'], c['centroid'][:3], c['net_importance'])
```

---

## 🧠 Use Cases
- Social agents forming identity via accumulated belief clusters
- Reflection-based belief consolidation
- Semantic memory grouping for simulations or cognitive models

---

## 🔄 Embedding Compatibility
BLOC assumes your memory entries are embedded using a tool like STEME.\
If no vector field is present in a memory object, BLOC will auto-embed using content.

---

## 📜 License
MIT (open use encouraged)

---

## 🙌 Credits
Created by Tim Chen\
Built to power the Civilizism agent belief model\
Designed for use in semantic cognition pipelines.

---
> “Memory fades. Identity clusters.”
