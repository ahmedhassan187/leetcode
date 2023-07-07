class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ts=0
        fs=0
        i=0
        maxi = 0
        last_max = 0
        j=0
        if len(answerKey) ==1:
            return 1
        if len(answerKey) ==2:
            return 2
        for i in range(len(answerKey)):
            if answerKey[i] == 'T':
                ts += 1
            elif answerKey[i] == 'F':
                fs += 1
            if min(fs,ts) >= k:
                maxi = max(fs,ts)+k
                while min(fs,ts)>k:
                    if answerKey[j] == 'F':
                        fs -= 1
                    elif answerKey[j]=='T':
                        ts -= 1
                    j=j+1
            if maxi > last_max:
                last_max = maxi
        if maxi == 0:
            return len(answerKey)
        return last_max
