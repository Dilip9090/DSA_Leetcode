class Solution(object):
    def sortPeople(self, names, heights):
        combined = zip(heights, names)
        
        
        sorted_data = sorted(combined, reverse=True)
       
       
        result = [name for height, name in sorted_data]
        
        return result