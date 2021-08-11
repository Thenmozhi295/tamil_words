import hashlib


class BloomFilter:
    
    def __init__(self, k=10000, hashes=None):
        
        self.bitarray = [False]*k
        if hashes:
            self.hashes = hashes
        else:
            self.hashes = BloomFilter.default_hashes

    @staticmethod
    def default_hashes(x):
        
        h = hashlib.sha512(x).hexdigest()
        return [h[:32], h[32:64], h[64:96], h[96:]]

    def add(self, member):
        
        for h in self.hashes(member):
            idx = int(h, 16) % len(self.bitarray)
            self.bitarray[idx] = True

    def check(self, member):
        
        for h in self.hashes(member):
            idx = int(h, 16) % len(self.bitarray)
            if self.bitarray[idx] != True:
                return False
        return True
