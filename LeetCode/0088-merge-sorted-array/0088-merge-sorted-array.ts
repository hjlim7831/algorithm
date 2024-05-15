/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    let p1: number = m - 1
    let p2: number = n - 1
    let k: number = nums1.length - 1

    while(p2 >= 0){
        if(nums1[p1] > nums2[p2]){
            nums1[k] = nums1[p1]
            p1--
        } else {
            nums1[k] = nums2[p2]
            p2--
        }
      k--
    }
    
};