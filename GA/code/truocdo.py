    def init_Sol(self):
        print(self.gv_hd)
        def tim_xx(self):
            while(1):
                stores = []
                for i in range(self.N):
                    stores.append(i)
                x = [-1]*self.N
                k_x = {}
                for i in range(self.K):
                    k_x[i] = []

                # chien luoc chon DA cung duoc GV cung hoi dong
                for gv in range(self.M):
                    gv_hd = copy.deepcopy(self.gv_hd[gv])
                    if len(gv_hd) >= self.d:
                        tmp = []
                        while(len(gv_hd) > 0):
                            rand_sl = random.randint(0, self.d - 1)
                            if len(gv_hd) <= rand_sl:
                                random_selection = gv_hd
                            else:
                                random_selection = random.sample(gv_hd, rand_sl)
                            
                            rand_hd = 0
                            while(1):
                                rand_hd = random.randint(0, self.K - 1)
                                if rand_hd in tmp: continue
                                if len(k_x[rand_hd]) + len(random_selection) > self.b: continue
                                break

                            tmp.append(rand_hd)
                            k_x[rand_hd] = k_x[rand_hd] + random_selection

                            for item in random_selection:
                                stores.remove(item)
                                gv_hd.remove(item)
                        
                print("33333",stores)
                check_1 = 0
                for i in range(self.K):
                    l = len(k_x[i])
                    if self.b - l >= 0:
                        random_selection = random.sample(stores, self.b - l)
                    if self.b - l <0:
                        check_1 = 1
                        break
                    if self.b - l ==0:
                        print("ok 1")

                    for item in random_selection:
                        stores.remove(item)
                    
                    k_x[i] = k_x[i] + random_selection

                for k, v in k_x.items():
                    print(len(v))

                if check_1 == 1:
                    print("do check_1")
                    continue
                for key, value in k_x.items():
                    for i in value:
                        x[i] = key

                check, gvhd = gv_tranh_hd(self, x)
                if check:
                    return x, k_x, gvhd
                else:
                    print("k_x:", k_x)
                    print("x", x)
                    print("do check 2")
                    print(stores)
                    continue
                
        def gv_tranh_hd(self, x):
            t = self.t
            gv_hd = {}
            for i in range(self.M):
                gv_hd[i] = []

            for i in range(self.N):
                gv = t[i] - 1
                hd = x[i]
                gv_hd[gv] = gv_hd[gv] +[hd]
            
            for i in range(self.M):
                tmp = set(gv_hd[i])
                gv_hd[i] = tmp 

                if len(tmp) >= self.d:
                    print(self.d)
                    print(tmp)
                    return False, None
            print(" 0 ")
            return True, gv_hd
                

        def tim_x(self):
            while(1):
                x = []
                k_x = {}
                for i in range(self.K):
                    k_x[i] = []
                
                for i in range(self.N):
                    random_number = random.randint(0, self.K - 1)
                    x.append(random_number)
                    k_x[random_number] = k_x[random_number] + [i]
                    
                max = 0
                for _, value in k_x.items():
                    if len(value) < self.a: continue
                    if len(value) > max: max = len(value)

                if max > self.b:
                    # print("nono")
                    continue

                check, gvhd = gv_tranh_hd(self, x)
                if check:
                    return x, k_x, gvhd
                else:
                    continue

        def tim_y(self, gvhd):
            y = []
            k_y = {}
            for i in range(self.K):
                k_y[i] = []

            for gv in range(self.M):#gv i hoi dong nao
                chon_gv_in = []
                for i in range(self.K):
                    if i in gvhd[gv]:continue
                    chon_gv_in.append(i)

                HD_gv = random.choice(chon_gv_in)
                
                y.append(HD_gv)
                k_y[HD_gv] = k_y[HD_gv] + [gv]

            for value in k_y.values():
                if len(value) < self.c: 
                    return False, None, None
                if len(value) > self.d:
                    return False, None, None

            return True, y, k_y

        while(1):
            if self.b*self.K == self.N:
                x, k_x, gvhd = tim_xx(self)
                # print("done1")
            else:
                x, k_x, gvhd = tim_x(self)

            suc, y, k_y = tim_y(self, gvhd) 
            # print("done2")
            if suc:
                # print("pass")
                self.x = x
                self.k_x = k_x
                self.k_y = k_y
                self.y = y
                break