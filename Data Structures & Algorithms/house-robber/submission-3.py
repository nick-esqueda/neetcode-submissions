class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        intution:
        - trying to find the optimal value
        - sequence of choices
        - must enumerate all combinations to find the best
        - take/leave patterns
        - subproblem? 
        - optimal substructure?


        [ 2, 9, 8, 3, 6 ]
          x             
                i
                      ?   <- what's the max I could get from robbing this house vs. not robbing it?
        
        do you need to ask if you *should* rob the current house?

        "i can rob this one, but i'd have to skip the next one"
        "i can NOT rob this one, and can use the next one"
        you can skip multiple houses if you really need
        - any benefit to this?

        choosing between this house and the next?


        [ 2, 9, 8, 3, 6 ]
          i
          x
        [ 2, 9, 8, 3, 6 ]
                i
          x     x
        [ 2, 9, 8, 3, 6 ]
                      i
          x     x     x
        total = 16
        ( if you skip, you HAVE to go to the n+2 house)

        [ 2, 9, 8, 3, 6 ]
          i      
          _
        [ 2, 9, 8, 3, 6 ]
             i      
          _  x
        [ 2, 9, 8, 3, 6 ]
                   i      
          _  x     x
        [ 2, 9, 8, 3, 6 ]
                        i      
          _  x     x
        total = 12

        [ 2, 9, 8, 3, 6 ]
          i      
          _
        [ 2, 9, 8, 3, 6 ]
             i      
          _  _
        [ 2, 9, 8, 3, 6 ]
                i      
          _  _  x
        [ 2, 9, 8, 3, 6 ]
                      i      
          _  _  x     x
        total = 14

        if you skip it, you CAN? go to the n+1 house. but couldn't you also go to the n+2?
        NO, stick with only going to N+1. If you go to N+2 then you clearly should have taken N.


        dp = [1, 2, 4, 0]
 
        [ 1, 2, 3, 1 ]
                   i
        """

        if len(nums) <= 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(dp)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        
        return dp[-1]












        