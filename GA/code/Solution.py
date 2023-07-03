import random

class Solution():
    def __init__(self, input) -> None:
        pathout, N, M, K, t, s, g, a, b, c, d, e, f = input

        self.N = N
        self.M = M
        self.K = K
        self.t = t
        self.s = s
        self.g = g
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        
        self.x = None
        self.y = None

        self.k_x = dict()
        self.k_y = dict()
        
        self.dotuongdong = 0
        self._do_tuong_dong_giua_cac_do_an = 0
        self._do_tuong_dong_giua_do_an_va_giao_vien = 0

        self.path_output = pathout

    def init_Sol(self):
        def tim_x(self):
            x = []
            k_x = {}
            for i in range(self.K):
                k_x[i] = []
            
            for i in range(self.N):
                random_number = random.randint(0, self.K - 1)
                x.append(random_number)
                k_x[random_number] = k_x[random_number] + [i]
            
            return x, k_x

        def tim_y(self, x):
            y = []
            k_y = {}
            for i in range(self.K):
                k_y[i] = []

            for gv in range(self.M):#gv i hoi dong nao
                while(1):
                    HD_gv = random.randint(0, self.K - 1)
                    for DA_i in range(self.N):
                        if self.t[DA_i] - 1 == gv:
                            if HD_gv == x[DA_i]:
                                continue
                            else:
                                break
                        else:
                            break
                    return False, None, None
                
                y.append(HD_gv)
                k_y[HD_gv] = k_y[HD_gv] + [gv]

            return True, y, k_y

        while(1):

            x, k_x = tim_x(self)
            suc, y, k_y = tim_y(self, x) 
            if suc:
                print("ok")
                self.x = x
                self.k_x = k_x
                self.k_y = k_y
                self.y = y
                break

    def rang_buoc(self)->bool:
        # RB1
        for so_DA in self.k_x.values():       
            if (len(so_DA) > self.b) or (len(so_DA) < self.a):
                return False
        # RB2
        for so_GV in self.k_y.values():       
            if (len(so_GV) > self.d) or (len(so_GV) < self.c):
                return False
        # RB3
        for i in range(self.N):

            if self.x[i] == self.y[self.t[i] - 1]:
                return False
            
        # RB4 do tuong dong DA&DA
        if not self._DA_and_DA():
            return False
        # RB5 do tuong dong GV&DA
        if not self._GV_and_DA():
            return False
        
        self.dotuongdong = self._do_tuong_dong_giua_cac_do_an/2 + self._do_tuong_dong_giua_do_an_va_giao_vien
        return True
    
    def tinhk_xy(self):
        k_x = {}
        for i in range(self.K):
            k_x[i] = []
        
        for i in range(self.N):
            k_x[self.x[i]] = k_x[self.x[i]] + [i]

        k_y = {}
        for i in range(self.K):
            k_y[i] = []
        
        for i in range(self.M):
            k_y[self.y[i]] = k_y[self.y[i]] + [i]

        self.k_x = k_x
        self.k_y = k_y


    def _DA_and_DA(self):
        self._do_tuong_dong_giua_cac_do_an = 0
        for xs in self.k_x.values():
            for DA1 in xs:
                for DA2 in xs:
                    if DA1 == DA2: continue
                    if self.s[DA1][DA2] < self.e:
                        return False
                    else:
                        self._do_tuong_dong_giua_cac_do_an += self.s[DA1][DA2]
        return True
    
    def _GV_and_DA(self):
        self._do_tuong_dong_giua_do_an_va_giao_vien = 0
        for k in range(self.K):
            for GV in self.k_y[k]:
                for DA in self.k_x[k]:
                    if self.g[DA][GV] < self.f:
                        return False
                    else:
                        self._do_tuong_dong_giua_do_an_va_giao_vien += self.g[DA][GV]
        return True
