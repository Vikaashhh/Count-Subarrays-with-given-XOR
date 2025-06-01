class Solution:
    def subarrayXor(self, arr, k):
        xor_map = {0: 1}  # pehle se 0 rakha kyunki kabhi kabhi direct prefixXOR hi k hota hai
        count = 0         # final answer
        curr_xor = 0      # ab tak ka prefix xor

        for num in arr:
            curr_xor ^= num  # har element ka xor lete jao

            # check karo ki curr_xor ^ k pehle aaya tha kya
            required = curr_xor ^ k
            if required in xor_map:
                count += xor_map[required]

            # ab is curr_xor ko map me update karo
            if curr_xor in xor_map:
                xor_map[curr_xor] += 1
            else:
                xor_map[curr_xor] = 1

        return count
