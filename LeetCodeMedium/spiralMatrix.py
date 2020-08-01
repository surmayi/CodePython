class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''1. pop the first row in [] to make it a list
        2.zip to transpose the remaining matrix within[] to make a list
        3. make this list in reverse using [::-1]
        4. Use recusrsion to call the function with this updated list
        5. Keep appending it to the poped items from step 1
        '''
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
        