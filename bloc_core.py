import numpy as np
from steme_core import embed, STEME, cosine_similarity

def add_to_cluster(memory, tag_pool, meta_tag_pool, thres):
    """
    Adds memory to an existing or new cluster based on semantic similarity.
    
    Mutates tag_pool in place.
    
    Args:
        memory (dict): Must have 'content' and 'importance'
        tag_pool (list): Each element is a cluster dict: {'name', 'centroid', 'net_importance'}
        meta_tag_pool (list): Predefined names to assign to new clusters
        thres (float): Similarity threshold for cluster membership

    Returns:
        str: The name of the cluster the memory was added to
    """
    # Embed the new memory content
    new_vec = embed(memory['content'])
    memory_importance = memory.get('importance', 0.0)

    # Drop any clusters with invalid (NaN) centroids
    valid_clusters = [c for c in tag_pool if not np.isnan(c['centroid']).any()]
    tag_pool[:] = valid_clusters

    # Find best matching existing cluster
    best_match = None
    best_score = -np.inf
    for cluster in tag_pool:
        score = cosine_similarity(new_vec.reshape(1, -1), cluster['centroid'].reshape(1, -1))[0][0]
        if score > best_score:
            best_score = score
            best_match = cluster

    # If similarity high enough, update that cluster's centroid
    if best_match is not None and best_score >= thres:
        old_weight = best_match.get('net_importance', 0.0)
        new_weight = old_weight + memory_importance
        if new_weight > 0:
            numerator = best_match['centroid'] * old_weight + new_vec * memory_importance
            updated_centroid = numerator / new_weight
            # Sanitize any NaNs that might sneak in
            best_match['centroid'] = np.nan_to_num(updated_centroid)
            best_match['net_importance'] = new_weight
            return best_match['name']
        # If new_weight <= 0, fall through to creating a new cluster

    # Otherwise, form a fresh cluster
    new_name = STEME(memory['content'], meta_tag_pool, top_k=1)[0][1]['content']
    tag_pool.append({
        'name': new_name,
        'centroid': new_vec,
        'net_importance': memory_importance
    })
    return new_name
