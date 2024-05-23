from statistics import median

def findMedianSortedArrays(nums1, nums2):
    return median(sorted(nums1 + nums2))




nums1 = [1,2,3]
nums2 = [4,5,6]
print(findMedianSortedArrays(nums1, nums2)) 

def different_approach(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    if len(nums1) % 2 == 1:
        n = int(len(nums1) / 2)
        return(nums1[n])
    else:
            m = int(len(nums1) / 2)
            k = m - 1
            f = (nums1[m] + nums1[k]) / 2
            return(f)
        
print(different_approach(nums1, nums2)) 