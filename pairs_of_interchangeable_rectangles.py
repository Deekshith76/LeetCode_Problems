from collections import defaultdict

def interchangeableRectangles(rectangles): # List[[width, height],..] expects int
    
    count = defaultdict(lambda:0) # w/h : no.of rectangles with same w, h
    
    # for w, h in rectangles:
    #     count[w/h] = 1 + count.get(w/h, 0)
    
    for w, h in rectangles:
        ratio = w/h
        count[ratio] += 1
    res = 0
    for c in count.values():
        if c > 1:
            res += (c * (c-1)) // 2
    return res
    
rectangles = [[4,8],[3,6],[10,20],[15,30]]
rectangles2 = [[4,5],[7,8]]
print(interchangeableRectangles(rectangles)) #6
print(interchangeableRectangles(rectangles2)) #0

'''
Cpp solution
'''

# class Solution {
# public:
#     long long interchangeableRectangles(vector<vector<int>>& rectangles) {
        
#         int len = rectangles.size();
#         double ratio[len];
        
#         for(int i=0; i<len; ++i)
#         {
#             ratio[i] = (1.0 * rectangles[i][0]/rectangles[i][1]);
#         }
        
#         sort(ratio, ratio+len);
#         long res = 0;
#         long count = 0;
#         int i = 0;
#         while (i < len)
#         {
#             count = 0;
#             while(i+1 < len && ratio[i+1] == ratio[i])
#             {
#                 count += 1;
#                 ++i;
#                 res += count;
#             }
#             ++i;
#         }
#         return res;
#     }
# };