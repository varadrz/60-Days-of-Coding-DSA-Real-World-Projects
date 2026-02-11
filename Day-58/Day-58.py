# Day 58 - Recommendation Engine
# Focus: Hashing + Trie + Scoring Optimization
# Language: Python 3


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        return self._collect_words(node, prefix)

    def _collect_words(self, node, prefix):
        results = []
        if node.is_end:
            results.append(prefix)

        for ch, next_node in node.children.items():
            results.extend(self._collect_words(next_node, prefix + ch))

        return results


class RecommendationEngine:
    def __init__(self):
        self.trie = Trie()
        self.item_scores = {}  # HashMap for item popularity

    def add_item(self, item, score):
        self.trie.insert(item)
        self.item_scores[item] = score

    def recommend(self, prefix):
        matches = self.trie.starts_with(prefix)

        # DP-style ranking: sort by score
        matches.sort(key=lambda x: self.item_scores.get(x, 0), reverse=True)
        return matches


def main():
    engine = RecommendationEngine()

    # Add items with popularity score
    engine.add_item("laptop", 90)
    engine.add_item("lamp", 75)
    engine.add_item("laser", 60)
    engine.add_item("mobile", 95)
    engine.add_item("mouse", 80)

    query = input("Enter search prefix: ").strip()
    recommendations = engine.recommend(query)

    print("\nRecommended Items:")
    for item in recommendations:
        print(f"{item} (Score: {engine.item_scores[item]})")


if __name__ == "__main__":
    main()
