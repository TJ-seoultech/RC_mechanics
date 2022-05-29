class Rebar():
    def __init__(self):
        self.ratio_min=2 #최소 철근비
        self.ratio_max=7 #최대 철근비
        self.num=0 # 최소 주철근 개수
        self.distance=40 # 최소 순간격
        self.depth=40 # 최소 피복두께
        self.location="normal" # 철근 위치
        self.SectionArea="Normal" # 단면적 성능
        self.D=22 # 철근 직경
        self.fck=28 # 철근 설계 강도

        self.ratio_min_condition()
        self.ratio_max_condition()
        self.min_num()
        self.min_distance()
        self.min_depth()

    def ratio_min_condition(self):
        if self.SectionArea=="Over":
            print("완화된 최소철근비 규정")
            return True
        else:
            try:
                if self.ratio_min>1:
                    print("최소철근비 상세설계 만족")
                    return True
                else:
                    raise ValueError
            finally:
                pass


    def ratio_max_condition(self):
        if self.location=="overlap joint":
            if self.ratio_max>4:
                print("최대철근비 상시설계 만족")
                return True
        else:
            try:
                if self.ratio_max<8:
                    print("최대철근비 상시설계 만족")
                    return True
                else:
                    raise ValueError
            finally:
                pass



    def min_num(self):
        try:
            if self.num>6:
                print("Rebar num is ok")
                return True
            else: raise ValueError
        except ValueError:
            print("Rebar num is not ok")
        finally:
            print("the end")
            pass

    def min_distance(self):
        assert self.distance>=max(40,1.5*self.D)
        print("최소순간격 만족")
        return True

    def min_depth(self):
        if self.fck>=40:
            if self.depth>=30:
                print("최소 피복두께 만족")
                return True
        else:
            try:
                if self.depth>=40:
                    print("최소 피복두께 만족")
                else:
                    print("최소 피복두께 error")
            finally:
                pass

class Stirrup():
    def __init__(self):
        self.diameter=12
        self.distance=10
        self.horizontal_support=True

        print("횡철근 직경은 {}로 상세설계 요구조건의 {} 이상이므로 최소직경 만족".format(self.diameter, self.max_diameter()))
    def max_diameter(self):
        func = lambda diameter : 13 if diameter>35 else (10 if diameter<32 else False)
        return func(self.diameter)

if __name__=="__main__":
    column=Rebar()
    stirrup1=Stirrup()
    # rebar_num = lambda x: print(x) if (x > 6) else print("no")
    # rebar_num(5)
    # test = lambda a: True if (a > 10 and a < 20) else False
    # print(test(1))
