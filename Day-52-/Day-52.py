# Day 52 - ML Feature Selection Simulator
# Focus: Optimization Techniques (Greedy + Pruning)
# Language: Python 3


class FeatureSelectionSimulator:
    def __init__(self, features, scores, max_features):
        """
        features: list of feature names
        scores: importance score for each feature
        max_features: number of features to select
        """
        self.features = features
        self.scores = scores
        self.max_features = max_features

    def select_features(self):
        """
        Greedy optimization:
        Select top-k features based on score
        """
        feature_data = list(zip(self.features, self.scores))

        # Sort features by descending importance score
        feature_data.sort(key=lambda x: x[1], reverse=True)

        selected = feature_data[:self.max_features]
        return selected


def main():
    features = ["Age", "Salary", "Experience", "Education", "Location"]
    scores = [0.65, 0.82, 0.75, 0.60, 0.55]
    max_features = 3

    simulator = FeatureSelectionSimulator(features, scores, max_features)
    selected_features = simulator.select_features()

    print("\nSelected Features for Model Training:")
    for feature, score in selected_features:
        print(f"{feature} (Score: {score})")


if __name__ == "__main__":
    main()
