class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1 and not nums2:
            return None
        if not nums1:
            return self.findMedianOfSingleArray(nums2)
        if not nums2:
            return self.findMedianOfSingleArray(nums1)

        return self.findMedianHelper(nums1, nums2)

    def findMedianHelper(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        
        low, high = 0, m
        while low <= high:
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i

            maxLeftX = float('-inf') if i == 0 else nums1[i - 1]
            minRightX = float('inf') if i == m else nums1[i]

            maxLeftY = float('-inf') if j == 0 else nums2[j - 1]
            minRightY = float('inf') if j == n else nums2[j]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (m + n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                high = i - 1
            else:
                low = i + 1

    def findMedianOfSingleArray(self, arr):
        n = len(arr)
        if n == 0:
            return None
        return (arr[n // 2 - 1] + arr[n // 2]) / 2.0 if n % 2 == 0 else arr[n // 2]


# Testing the updated solution
solution = Solution()
test_cases = [
    ([1, 3, 5], [2, 4, 6]),  # Perfectly interleaved
    ([], [1, 2, 3, 4, 5]),  # Edge case with one empty array
    ([1, 2, 3, 4, 5, 6], [7, 8, 9, 10]),  # Non-overlapping larger sizes
    ([1], [2, 3, 4, 5, 6, 7, 8, 9, 10])  # One very small array vs a large array
]

results = []
for nums1, nums2 in test_cases:
    median = solution.findMedianSortedArrays(nums1, nums2)
    results.append(f"Median of {nums1} and {nums2} is {median}")
print(results)
