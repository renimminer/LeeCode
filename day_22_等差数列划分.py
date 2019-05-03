"""
A = [1, 2, 3, 4]
返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。
成功 O(n)
显示详情
执行用时 : 56 ms, 在Arithmetic Slices的Python3提交中击败了51.81% 的用户
内存消耗 : 13.4 MB, 在Arithmetic Slices的Python3提交中击败了15.91% 的用户
"""
class Solution:
    def numberOfArithmeticSlices(self, A):
        n = len(A)  # 前三行判断特殊情况，A长度小于3直接返回0
        if len(A) < 3:
            return 0
        dp = [0, 0]  # 动态规划的转移矩阵
        i = 2
        j = 1       # j 是矩阵dp子序列连续非零时的起点指针
        sum = 0     # 合计每个非零子序列段的等差数列个数，初始设为0
        while i < n:  # 对于矩阵dp
            if A[i - 1] - A[i - 2] == A[i] - A[i - 1]:  # 如果该位置形成的前三项构成等差数列，
                dp.append((j + 1) * j / 2)              # dp中，该位置数值为 以j指针为起点的高斯数列和
                j += 1
            else:
                j = 1                   # 当等差子序列断裂（dp矩阵中出现0时）重置j指针
                dp.append(0)
                sum += dp[i-1]          # 等差子序列断裂（dp矩阵中出现0时）统计一次当前最大子序列个数
            i += 1
        return dp[-1]+sum
        # 输出结果时dp矩阵最后一项（无论是否为0）加上之前的累计sum


if __name__ == "__main__":
    solution = Solution()
#    A = [1,2,3,4]
#    A = []
#    A = [1]
#    A = [1,1]
    # A = [1,1,2,3,4] # 3
    # A = [1,1,2,3,3,5] #
    # A = [1,1,2,3,4,5,6,7] # 1,3,6,10,15
    A = [1,2,3,4,3,7,8,9,10]

    print(solution.numberOfArithmeticSlices(A))