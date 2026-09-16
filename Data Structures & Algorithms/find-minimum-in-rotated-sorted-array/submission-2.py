class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        In other words, find the pivot point

        if l -> mid sorted (nums[l] <= nums[mid]): l = mid
        else l -> mid not sorted: r = mid - 1
        RESULT: FINDS GREATEST NUM, OR INF LOOPS
 
        pivot in right: [ 3, 4, 5, 1, 2 ]
                                l                  
                                r
                                m            
        pivot in right: [ 2, 3, 4, 1 ]  * INF LOOP
                                l
                                   r   
                                m
        pivot in left: [ 4, 1, 2, 3 ]
                         l
                         r         
                         m
        pivot in right: [2, 3, 1]       * INF LOOP
                            l
                               r    
                            m
        pivot in left:  [3, 1, 2]
                         l
                         r
                         m

        if l -> mid sorted (nums[l] < nums[mid]): l = mid
        else l -> not sorted (or l == mid): r = mid - 1
        RESULT: FINDS GREATEST NUM, NOT LEAST
 
        pivot in right: [ 3, 4, 5, 1, 2 ]
                                l            
                                r
                                m            
        pivot in right: [ 2, 3, 4, 1 ]
                                l
                             r   
                                m
        pivot in left: [ 4, 1, 2, 3 ]
                         l
                         r         
                         m
        pivot in right: [ 2, 3, 1 ]
                             l
                          r    
                             m
        pivot in left:  [ 3, 1, 2 ]
                          l
                          r
                          m

        if l -> mid sorted (nums[l] <= nums[mid]): l = mid + 1
        else l -> not sorted: r = mid
        RESULT: MISSES MIN BY 1 IN [1, 2] CASE
 
        pivot in right: [ 3, 4, 5, 1, 2 ]
                                      l
                                      r
                                      m      
        pivot in right: [ 2, 3, 4, 1 ]
                                   l      
                                   r
                                   m   
        pivot in left: [ 4, 1, 2, 3 ]
                            l
                            r         
                            m
        pivot in right: [ 2, 3, 1 ]
                                l
                                r    
                                m
        pivot in left:  [ 3, 1, 2 ]
                             l
                             r 
                             m
        """

        l = 0 
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2

            if nums[l] < nums[r]:
                return nums[l]

            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
 