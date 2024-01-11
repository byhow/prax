class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        pre = ""
        n = len(products)
        res = []
        for c in searchWord:
            pre += c
            idx = bisect_left(products, pre)
            suggestions = []
            for i in range(idx, min(idx + 3, n)):
                if products[i].startswith(pre):
                    suggestions.append(products[i])
                    
            res.append(suggestions)

        return res
        
