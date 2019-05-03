class Solution:
    """
    给定一个方形整数数组 A，我们想要得到通过 A 的下降路径的最小和。

下降路径可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列。
O(n2)
显示详情
执行用时 : 88 ms, 在Minimum Falling Path Sum的Python3提交中击败了63.89% 的用户
内存消耗 : 13.5 MB, 在Minimum Falling Path Sum的Python3提交中击败了95.83% 的用户
    """
    def minFallingPathSum(self, A):
        n = len(A)
        if n == 1:  # 特殊处理
            return A[0][0]
        dp = [A[-1]] # 其实这项可以加进循环
        for i in range(n-2, -1, -1):
            dp.append(A[i]) # i从A的最后一行向第一行逐行加
            for j in range(0, n):
                if j == 0:  # 如果j标识为矩阵的第0列，找它与上一步本列或下一列的累计最小和
                    dp[n - i - 1][j] += min(dp[n - i-2][j], dp[n - i-2][j + 1])
                elif j == n-1: # 如果j标识为矩阵的最后一列，找它与上一步本列或上一列的累计最小和
                    dp[n - i - 1][j] += min(dp[n - i-2][j], dp[n - i-2][j - 1])
                else:
                    dp[n-i-1][j] += min(dp[n-i-2][j], dp[n-i-2][j-1], dp[n-i-2][j+1])
        return min(dp[-1])


if __name__ == "__main__":
    solution = Solution()
    # print(solution.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
    # print(solution.minFallingPathSum([[1]]))
    print(solution.minFallingPathSum([[1, 1], [1, 1]]))