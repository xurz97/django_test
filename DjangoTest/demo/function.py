def differential(CipherName, Round1, Round2):
    """
    Do something
    """
    sss = CipherName + "差分分析" + " " + str(Round1) + " " + str(Round2) + "\n "
    return sss+"""2 : Ch(w=0, id=0040 0000 0000, od=0000 0000 8000)\n 3 : Ch(w=0, id=0040 0000 0000 0000, od=0000 0000 0000 8000)\n 4 : Ch(w=0, id=0040 0000 0000 0000, od=0000 0000 0000 8000 8002)"""

def linear(CipherName, Round1, Round2):
    """
    Do something
    """
    sss = CipherName + "线性分析" + " " + str(Round1) + " " + str(Round2) + "\n "
    return sss+"""2 : Ch(w=0, id=0040 0000 0000, od=0000 0000 8000)\n 3 : Ch(w=0, id=0040 0000 0000 0000, od=0000 0000 0000 8000)\n 4 : Ch(w=0, id=0040 0000 0000 0000, od=0000 0000 0000 8000 8002)"""

def difflinear(CipherName, Round1, Round2):
    """
    Do something
    """
    sss = CipherName + "差分线性分析" + " " + str(Round1) + " " + str(Round2) + "\n "
    return sss+"""2 : Ch(w=0, id=0040 0000 0000, od=0000 0000 8000)\n 3 : Ch(w=0, id=0040 0000 0000 0000, od=0000 0000 0000 8000)\n 4 : Ch(w=0, id=0040 0000 0000 0000, od=0000 0000 0000 8000 8002)"""