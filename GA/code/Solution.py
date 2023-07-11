import random
import copy

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

        self.gv_hd = None
        self.gv_hd_doan()

        self.dotuongdong = 0
        self._do_tuong_dong_giua_cac_do_an = 0
        self._do_tuong_dong_giua_do_an_va_giao_vien = 0

        self.path_output = pathout

    def gv_hd_doan(self):
        gv_hd = {}
        for i in range(self.M):
            gv_hd[i] = []

        for da in range(self.N):
            gv = self.t[da] - 1
            gv_hd[gv] = gv_hd[gv] + [da]

        self.gv_hd = gv_hd

    def init_Sol(self):
        # khoi tao k_y
        k_y = {}
        for i in range(self.K):
            k_y[i] =[]

        gv_tmp = [gv for gv in range(self.M)] 
        for k in range(self.K):
            ran = random.choice(gv_tmp)
            k_y[k] = k_y[k] + [ran]
            gv_tmp.remove(ran)

        for k in range(self.K):
            tmp_k = []
            rand_sl = random.randint(0, min(self.d - 1, len(gv_tmp)))
            
            for i in range(rand_sl):
                rand_ = random.choice(gv_tmp)
                tmp_k.append(rand_)
                gv_tmp.remove(rand_)

            k_y[k] = k_y[k] + tmp_k
        
        print(k_y)
        gv_in_hd = [-1]*self.M

        for i in range(self.K):
            for j in k_y[i]:
                gv_in_hd[j] = i

        print(gv_in_hd)


        def timK_X(self, gv_in_hd):
            k_x = {}
            for i in range(self.K):
                k_x[i] = []

            da_can_hd = {}
            for i in range(self.N):
                gvhd = self.t[i] - 1 
                hd_dont_in =  gv_in_hd[gvhd]
                
                hdcan = [hd for hd in range(self.K)]
                hdcan.remove(hd_dont_in)
                da_can_hd[i] = hdcan
            
            print(da_can_hd[0])
            
            hd_con = [self.b]*self.K
            
            for i in range(self.N):

                for j in range(self.K):
                    if (hd_con[j] == 0) and (j in da_can_hd[i]) :  da_can_hd[i].remove(j)    
                print(i, da_can_hd[i])

                if da_can_hd[i] == []: return timK_X(self, gv_in_hd)
                # print(da_can_hd)
                hd = random.choice(da_can_hd[i])
                k_x[hd] = k_x[hd] + [i]
                hd_con[hd] -=  1

            print(k_x)
            return k_x

        k_x = timK_X(self, gv_in_hd)
        self.k_x = k_x
        self.k_y = k_y
        x = [-1]*self.N
        y = [-1]*self.M

        for i in range(self.K):
            for j in k_x[i]:
                x[j] = i
            for m in k_y[i]:
                y[m] = i

        self.x = x
        self.y = y


    def rang_buoc(self)->bool:
        # RB1
        for so_DA in self.k_x.values():       
            if (len(so_DA) > self.b) or (len(so_DA) < self.a):
                print("RB1")
                return False
        # RB2
        for so_GV in self.k_y.values():       
            if (len(so_GV) > self.d) or (len(so_GV) < self.c):
                print("RB2")
                return False
        # RB3
        for i in range(self.N):

            if self.x[i] == self.y[self.t[i] - 1]:
                print("RB3")
                return False
            
        # RB4 do tuong dong DA&DA
        if not self._DA_and_DA():
            print("RB4")
            return False
        # RB5 do tuong dong GV&DA
        if not self._GV_and_DA():
            print("RB5")
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
