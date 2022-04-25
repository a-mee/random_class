class MyRandom():
    __a = 7
    __c = 5
    __m = 997
    def __init__(self, **kwargs):
        if 'seed' in kwargs:
            self.__seed = kwargs['seed']
        else:
            import time 
            self.__seed = int(time.time())
    
    def _randint(self):
        self.__seed = (MyRandom.__a * self.__seed + MyRandom.__c) % MyRandom.__m
        return self.__seed
    
    def rand(self):
        return self._randint() / 997
    
    def randint(self, bot, top):
        if isinstance(bot, int) and isinstance(top, int) and top > bot:
            while True:
                ans = self._randint() % top + 1
                if bot <= ans:
                    return ans
        else:
            print('error: incorrect arguments')
    
    def shuffle(self, lst):
        if isinstance(lst, list) and lst != []:
            count = len(lst) 
            newList = lst.copy()
            while count > 1:
                ans = self.randint(0, count)
                newList[count-1], newList[ans-1] = newList[ans-1], newList[count-1]
                count -= 1
            return newList
        else:
            print('error: incorrect argument')
    
    def choice(self, lst):
        if isinstance(lst, list) and len(lst) > 1:
            count = 0
            lst_dict = {}
            for num in lst:
                count +=1
                lst_dict[count] = num
            ans = self.randint(1, count)
            return lst_dict[ans]
        else:
            print('error: incorrect argument')
    
    def seed(self, new_seed):
        if isinstance(new_seed, int):
            self.__seed = new_seed
        else:
            print('error: incorrect argument')

class MyDie(MyRandom):
    def throw(self):
        return self.randint(1,6)

class MyCoin(MyRandom):
    coin = {1: 'heads', 2:'tails'}
    
    def toss(self):
        ans = self.randint(1,2)
        return MyCoin.coin[ans]