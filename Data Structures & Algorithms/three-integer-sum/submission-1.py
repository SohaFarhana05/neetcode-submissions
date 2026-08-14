class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        from collections import Counter

        def check(arr, t, ind):
            d = Counter(arr)

            # Don't allow nums[ind] to be reused
            x = arr[ind]
            d[x] -= 1

            pairs = []

            for a in d:
                if d[a] == 0:
                    continue

                b = t - a

                if b not in d or d[b] == 0:
                    continue

                # Same value requires 2 occurrences
                if a == b:
                    if d[a] >= 2:
                        pairs.append([a, b])
                else:
                    pairs.append([a, b])

            return pairs

        result = []

        for i in range(len(nums)):
            pairs = check(nums, -nums[i], i)

            for pair in pairs:
                triplet = [nums[i], pair[0], pair[1]]
                triplet.sort()

                if triplet not in result:
                    result.append(triplet)

        return result
        # from collections import defaultdict
        # self.ans = []
        # def check(arr,t,ind):
        #     d = Counter(arr)
        #     x = arr[ind]
        #     d[x] -= 1
        #     for a in d:
        #         if d[a] == 0:
        #             continue
        #         b = t - a
        #         if b not in d or d[b] == 0:
        #             continue
        #         if a == b:
        #             if d[a] >= 2:
        #                 return [a, b]

        #         else:
        #             return [a, b]

        #     return None
        #     # a = []
        #     # s = set(arr)
        #     # d = defaultdict(int)
        #     # for i in arr:
        #     #     d[i]+=1
        #     # d[ind]-=1
        #     # for i in range(len(arr)):
        #     #     here = t - arr[i]
                
        #     #     if here in s:
        #     #         if here==t:
        #     #             if d[here]>1:
        #     #                 a = [here,arr[i]]
        #     #                 self.ans = a
        #     # if len(self.ans)!=0:
        #     #     return True 
        #     # return False
        # result = []
        # for i in range(len(nums)):
        #     pair = check(nums,-nums[i],i)
        #     if pair:
        #         triplet = [nums[i], pair[0], pair[1]]
        #         triplet.sort()

        #         if triplet not in result:
        #             result.append(triplet)
        # return result
        # #     if check(nums,-nums[i],i):
        # #         w , r = self.ans[0], self.ans[1]
        # #         if ([w,r,nums[i]] or [r,w,nums[i]] or [nums[i],w,r] or [nums[i],r,w]) not in result:
        # #             result.append([w,r,nums[i]])
        # # return result
