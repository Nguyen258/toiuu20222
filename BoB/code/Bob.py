import time

class Bob():
    def __init__(self, input) -> None:
        pathout, N, M, K, t, s, g, a, b, c, d, e, f = input
        # input
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
        # use
        self.x = [0]*N
        self.y = [0]*M
        self._do_tuong_dong_giua_cac_do_an = 0
        self._do_tuong_dong_giua_do_an_va_giao_vien = 0
        self.fit = 0
        self.k_x = dict()
        self.k_y = dict()
        self.time_start = time.time() 
        # output
        self.x_good = None
        self.y_good = None
        self.fit_good = 0
        self.path_output = pathout
        
    def run(self):
        with open(self.path_output, 'w') as file:
            file.truncate(0)

        start = [-1]*(self.N+self.M)
        self.try_bob(start, 0)

        with open(self.path_output, 'a') as file:
            print("    fitniss:{}".format(self.fit_good), file=file)
            print("    x:{} |y:{}".format(self.x_good, self.y_good), file=file)
            print("", file=file)

    def try_bob(self, a, t):
        if t == self.N+self.M:
            self.x = a[:self.N]
            self.y = a[self.N: t]
            self.tinhk_xy()
            if self.rang_buoc():
                if self.fit > self.fit_good:
                    self.fit_good = self.fit
                    self.x_good = self.x
                    self.y_good = self.y
        else:
            current_time = time.time() 
            if current_time - self.time_start > 600:
                return
            else:
                for i in range(self.K):
                    a[t] = i
                    self.try_bob(a, t+1)

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
        
        self.fit = self._do_tuong_dong_giua_cac_do_an + self._do_tuong_dong_giua_do_an_va_giao_vien
        return True
    
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
