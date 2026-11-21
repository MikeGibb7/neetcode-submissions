class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        for st in strs:
            msg +=  st + "\n"
        print(msg)
        return msg

    def decode(self, s: str) -> List[str]:
        li = []
        word = ""
        for i in s:
            if i == "\n":
                li.append(word)
                word = ""
                continue
            word += i
        return li
