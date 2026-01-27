# Day 44 - Plagiarism Detection Engine
# Focus: Dynamic Programming on Strings (LCS)
# Language: Python 3


class PlagiarismDetector:
    def __init__(self, text1, text2):
        self.text1 = text1
        self.text2 = text2

    def longest_common_subsequence(self):
        """
        dp[i][j] = length of LCS of text1[:i] and text2[:j]
        """
        n = len(self.text1)
        m = len(self.text2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if self.text1[i - 1] == self.text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]

    def similarity_percentage(self):
        lcs_length = self.longest_common_subsequence()
        max_length = max(len(self.text1), len(self.text2))
        return (lcs_length / max_length) * 100 if max_length > 0 else 0


def main():
    text1 = input("Enter first text: ").strip()
    text2 = input("Enter second text: ").strip()

    detector = PlagiarismDetector(text1, text2)
    similarity = detector.similarity_percentage()

    print(f"\nSimilarity Percentage: {similarity:.2f}%")

    if similarity > 70:
        print("High similarity detected (Possible plagiarism).")
    else:
        print("Similarity within acceptable range.")


if __name__ == "__main__":
    main()
