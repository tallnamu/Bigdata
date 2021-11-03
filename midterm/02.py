class stat:
    def _init_(self):
        self.x=0
        self.mean=0
        self.var=0
    def mean(self_):
        sum_=0
        for i in range(len(self.x)):
            sum_+=self.x[i]
        return sum_/len(self.x)
    def var(self):
        m=mean(self.x)
        sum_=0
        for i in self:
            sum_+=(i-m)**2
        return sum_/(len(list_)-1)
    def load(self.list_):
        self.x=list_
