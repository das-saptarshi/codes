# Link to Problem: https://leetcode.com/problems/text-justification/
# Time Complexity: O(n) where n is the number of words
# Space Complexity: O(n + (n / maxWidth))


from typing import List
from math import ceil

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        sentences = self.makeSentences(words, maxWidth)
        return self.justifySentences(sentences, maxWidth)

    
    def makeSentences(self, words, maxWidth):
        sentences = []
        index = 0
        n = len(words)        


        while index < n:
            sentence = []
            charsCount = 0

            while index < n and (charsCount + len(sentence) + len(words[index])) <= maxWidth:
                sentence.append(words[index])
                charsCount += len(words[index])
                index += 1
            
            sentences.append({
                'charsCount': charsCount,
                'spaceCount': len(sentence)  - 1,
                'sentence': sentence
            })
        
        return sentences

    def justifySentences(self, sentences, maxWidth):
        justifiedSentences = []
        
        for sentence in sentences[:-1]:
            spaces = maxWidth - sentence['charsCount']
            spaceCount = sentence['spaceCount']

            print(sentence)
            ans = ''

            for word in sentence['sentence']:
                
                if spaceCount > 0:
                    x = int(ceil(spaces / spaceCount))
                    spaces -= x
                    spaceCount -= 1
                else:
                    x = spaces

                ans += word + ' ' * x
            
            justifiedSentences.append(ans)
        
        sentence = sentences[-1]
        spaces = maxWidth - sentence['charsCount']
        
        justifiedSentences.append(' '.join(sentence['sentence']) + ' ' * (spaces - sentence['spaceCount']))

        return justifiedSentences
