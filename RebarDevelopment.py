import math
from functools import reduce

jd1=100
jd2=90
V=10

u="average_bond_stress"
u=V/sum([jd1, jd2])
# print(u)

fy=400
fck=24

class Rebar_type():
    def __init__(self, rebar_type):
        self.type_factor={"tensile_deformed_rebar":0.9,
                          "compressive_deformed_rebar":0.25,
                          "Hooked_bar":0.24}
        self.tensile_deformed_rebar_coefficient_parameter={"lightCon":1.0,
                                     "rebarLocation":1.3,
                                     "paintfilm":1.0,
                                     "rebar_size":1.0,
                                     "rebar_interval":min(62.7,174.6/2),
                                     "horizontalRebar":0,
                                     "diameter":25.4
                                     }
        self.factor=self.type_factor[rebar_type] # 이게 갈고리에서도 여전히 주철근 인장 철근 정착의 하중 계수를 이용한다.
        self.EDL=self.factor*fy/math.sqrt(fck) # Essential Development Length
        self.tensile_deformed_rebar = self.EDL*self.tensile_deformed_rebar_coefficient_parameter["rebarLocation"]*self.tensile_deformed_rebar_coefficient_parameter["paintfilm"]*self.tensile_deformed_rebar_coefficient_parameter["rebar_size"]/self.tensile_deformed_rebar_coefficient_parameter["lightCon"]*self.tensile_deformed_rebar_coefficient_parameter["diameter"]**2/(self.tensile_deformed_rebar_coefficient_parameter["rebar_interval"]+self.tensile_deformed_rebar_coefficient_parameter["horizontalRebar"])
        self.tensile_deformed_rebar = self.tensile_deformed_rebar * 930/1013.4
        self.tensile_deformed_rebar_result_length = max(self.tensile_deformed_rebar,300)




        self.compressive_deformed_rebar_coefficient_parameter = {"diameter":22,
                                                                 "lightCon":1.0,
                                                                 "correction_factor":1.0}
        self.compressive_deformed_rebar = max(self.EDL*self.factor*self.compressive_deformed_rebar_coefficient_parameter["diameter"]/self.compressive_deformed_rebar_coefficient_parameter["lightCon"],0.043*self.compressive_deformed_rebar_coefficient_parameter["diameter"]*fy)
        self.compressive_deformed_rebar_result_length = max(self.compressive_deformed_rebar,200)


        self.hooked_tensile_deformed_rebar_coefficient_parameter={"paint_film":1.0,
                                                                  "diameter":25.4,
                                                                  "lightCon":1.0,
                                                                  "Depth":62.7}
        self.hooked_tensile_deformed_rebar_correction_factor= 0.7
        self.hooked_tensile_deformed_rebar = self.EDL*self.hooked_tensile_deformed_rebar_coefficient_parameter["paint_film"]*self.hooked_tensile_deformed_rebar_coefficient_parameter["diameter"]/self.hooked_tensile_deformed_rebar_coefficient_parameter["lightCon"]
        self.hooked_tensile_deformed_rebar_result_length = max(self.hooked_tensile_deformed_rebar*self.hooked_tensile_deformed_rebar_correction_factor*930/1013.4,max(8*self.hooked_tensile_deformed_rebar_coefficient_parameter["diameter"],150))


TensileRebar=Rebar_type("tensile_deformed_rebar")
print(TensileRebar.tensile_deformed_rebar, type(TensileRebar.tensile_deformed_rebar))
print(TensileRebar.tensile_deformed_rebar_result_length)

CompressiveRebar=Rebar_type("compressive_deformed_rebar")
print(CompressiveRebar.compressive_deformed_rebar, type(CompressiveRebar.compressive_deformed_rebar))
print(CompressiveRebar.compressive_deformed_rebar_result_length)
# https://shoark7.github.io/programming/algorithm/3ways-to-get-multiplication-in-a-list-in-python 출처: 리스트 내 요소 곱 구하기
# arr = [1, 2, 3, 4, 5]

HookedRebar=Rebar_type("Hooked_bar")
print(HookedRebar.type_factor)
print(HookedRebar.factor)
print(HookedRebar.EDL)
print(HookedRebar.EDL*1.0*25.4/1.0)
print(HookedRebar.hooked_tensile_deformed_rebar, type(HookedRebar.hooked_tensile_deformed_rebar))
print(HookedRebar.hooked_tensile_deformed_rebar_result_length)


"""
def multiply(arr):
    ans = 1
    for n in arr:
	if n == 0:
            return 0
        ans *= n
   return ans

def multiply(arr):
    return reduce(lambda x, y: x * y, arr)

multiply(arr)
"""
