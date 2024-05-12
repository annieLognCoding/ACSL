class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1 and not nums2:
            return None  # Handle cases where both arrays are empty
        if not nums1:
            return self.findMedianOfSingleArray(nums2)
        if not nums2:
            return self.findMedianOfSingleArray(nums1)

        shorterArray = nums1 if len(nums1) <= len(nums2) else nums2
        biggerArray = nums2 if len(nums1) <= len(nums2) else nums1
        indSmaller, indBigger = len(shorterArray) // 2, len(biggerArray) // 2

        return self.findMedianHelper(indSmaller, indBigger, shorterArray, biggerArray)
    
    def findMedianHelper(self, i, j, nums1, nums2):
        step = i // 2
        if(step == 0):
            step = 1 
        
        # Edge case handling
        if(i == 0 or i == len(nums1) - 1 or j == 0 or j == len(nums2) - 1):
            if(i == 0 and j == len(nums2) - 1 or i == len(nums1) - 1 and j == 0):
                return (nums2[j] + nums1[i]) / 2 if (len(nums1) + len(nums2)) % 2 == 0 else min(nums2[j], nums1[i])
            elif(i == 0):
                if(nums1[i] > nums2[j + 1]):
                    return (nums2[j] + nums2[j - 1]) / 2 if (len(nums1) + len(nums2)) % 2 == 0 else nums2[j - 1]
            elif(j == 0 or j == len(nums2) - 1):
                return (nums1[i] + nums1[i - 1]) / 2 if (len(nums1) + len(nums2)) % 2 == 0 else nums1[i - 1]

        target1 = nums1[i]
        target2 = nums2[j]
        ans = min(target1, target2)
        if((len(nums2) + len(nums1)) % 2 == 0):
            ans = (target1 + target2) / 2

        
        if(target1 == target2):
            return ans
        elif (target1 < target2):
            if(target1 < nums2[j - 1]):
                return self.findMedianHelper(i + step, j - step, nums1, nums2)
            else:
                return ans
        else:
            if(target1 > nums2[j + 1]):
                return self.findMedianHelper(i - step, j + step, nums1, nums2)
            else:
                return ans
    
    def findMedianOfSingleArray(self, arr):
        n = len(arr)
        return (arr[n // 2 - 1] + arr[n // 2]) / 2.0 if n % 2 == 0 else arr[n // 2]

# Specific arrays to test
arr1 = [10, 20, 30]
arr2 = [15, 25, 35, 45, 55]

# Create a solution instance and test
solution = Solution()
combined = sorted(arr1 + arr2)
expected_median = combined[len(combined) // 2] if len(combined) % 2 != 0 else (combined[len(combined) // 2 - 1] + combined[len(combined) // 2]) / 2.0
actual_median = solution.findMedianSortedArrays(arr1, arr2)

print("Combined sorted array:", combined)
print("Expected median:", expected_median)
print("Actual median calculated:", actual_median)
