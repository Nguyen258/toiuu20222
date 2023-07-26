from tqdm import tqdm
import copy
import time
import random

import Solution

class Ga():
    def __init__(self, N, Gen, sol:Solution) -> None:
        self.sol_sample = sol
        self.Gen = Gen
        self.n_pop = N
        self.remove = int(N/3)
        self.mutation_rate = 0.1
        self.hybridization_rate = 0.5

        self.pop = []
        self.fitness = []

        self.top_fitness = None
        self.expulsion_set = []

        self.path_output = sol.path_output

    def run(self):
        with open(self.path_output, 'w') as file:
            file.truncate(0)
        # khoi toa quan the
        self.initialize_population()
        # tinh ham muc tieu
        self.evaluate_population()
        # sap xep chon loc
        self.sort_selective()
        for gen in tqdm(range(self.Gen)):
            # in ra ca the tot nhat
            self.print_gen(gen)
            # sinh san
            self.reproductionss()
            # tinh ham muc tieu
            self.evaluate_population()
            # sap xep, chon loc
            self.sort_selective()

    def reproductionss(self):
        child = []
        # lai 
        for i in range(self.n_pop):
            if i in self.expulsion_set:continue
            for j in range(i, self.n_pop):
                if j in self.expulsion_set:continue
                random_number = random.random()
                if random_number < self.hybridization_rate:
                    child_tmp, suc = self._laighep(i,j)
                    if suc:
                        child = child + child_tmp

        # dot bien
        for i in range(self.n_pop):
            if i in self.expulsion_set:continue
            random_number = random.random()
            if random_number < self.mutation_rate:
                child_tmp2, suc = self._dotbien(i)
                if suc:
                    child = child + [child_tmp2]
        # trung
        childs_return = []
        for chi in child:
            if self._sol_not_in_pop(chi) == True:
                if self._not_in(chi, childs_return) == True:
                    childs_return.append(chi)

        # init
        start_time = time.time()
        while(len(childs_return) < len(self.expulsion_set)):
            current_time = time.time()  # Lấy thời gian hiện tại
            elapsed_time = current_time - start_time  # Tính thời gian đã trôi qua
            if elapsed_time >= 20:  # Kiểm tra nếu đã đạt đến thời gian kết thúc (ví dụ: 60 giây - 1 phút)
                for hi in self.expulsion_set:
                    sol_new = copy.deepcopy(self.pop[hi])
                    childs_return.append(sol_new)
                    if len(childs_return) == len(self.expulsion_set):
                        break  # Thoát khỏi vòng lặp

            sol_init = copy.deepcopy(self.sol_sample)
            sol_init.init_Sol()
            if (sol_init.rang_buoc()) and (self._sol_not_in_pop(sol_init)):
                childs_return.append(sol_init)
            else:
                del sol_init

        for i_sol in self.expulsion_set:
            element_to_remove = random.choice(childs_return)
            self.pop[i_sol] = element_to_remove
            childs_return.remove(element_to_remove)
        
    def print_gen(self, gen):
        with open(self.path_output, 'a') as file:
            # Ghi các lời gọi print vào file
            print("Gen: {}".format(gen + 1), file=file)
            print("    fitniss:{}".format(self.top_fitness[1]), file=file)
            print("    x:{} |y:{}".format(self.pop[self.top_fitness[0]].x, self.pop[self.top_fitness[0]].y), file=file)
            print("", file=file)

    def sort_selective(self):
        fitness = self.fitness
        sorted_lose = sorted(fitness, key=lambda x: x[1], reverse=True)
        self.top_fitness = sorted_lose[0]
        self.expulsion_set = [sol_lose[0] for sol_lose in sorted_lose[self.n_pop - self.remove:]]
    
    def evaluate_population(self):
        for i in range(self.n_pop):
            fit = [i, self.pop[i].dotuongdong]
            self.fitness.append(fit)

    def initialize_population(self):
        start_time = time.time() 
        while(len(self.pop) <= self.n_pop):
            current_time = time.time()  # Lấy thời gian hiện tại
            elapsed_time = current_time - start_time  # Tính thời gian đã trôi qua
            if elapsed_time >= 10:  # Kiểm tra nếu đã đạt đến thời gian kết thúc (ví dụ: 60 giây - 1 phút)
                self.n_pop = len(self.pop)
                self.remove = int(self.n_pop/3)
                break  # Thoát khỏi vòng lặp

            sol_init = copy.deepcopy(self.sol_sample)
            sol_init.init_Sol()
            
            if (sol_init.rang_buoc()) and (self._sol_not_in_pop(sol_init)):
                self.pop.append(sol_init)
            else:
                del sol_init


    def _laighep(self,sol1_id, sol2_id):
        child = []

        parent1_x = copy.deepcopy(self.pop[sol1_id].x)
        parent1_y = copy.deepcopy(self.pop[sol1_id].y)

        parent2_x = copy.deepcopy(self.pop[sol2_id].x)
        parent2_y = copy.deepcopy(self.pop[sol2_id].y)
        
        # Lai ghép chuỗi gen từ cha mẹ
        child1_x = []
        child1_y = []
        child2_x = []
        child2_y = []
        for i in range(len(parent1_x)):
            random_number = random.random()
            if random_number > 0.5:    
                child1_x.append(parent1_x[i])
                child2_x.append(parent2_x[i])
            else:
                child1_x.append(parent2_x[i])
                child2_x.append(parent1_x[i])

        for i in range(len(parent1_y)):
            random_number = random.random()
            if random_number > 0.5:  
                child1_y.append(parent1_y[i])
                child2_y.append(parent2_y[i])
            else:
                child1_y.append(parent2_y[i])
                child2_y.append(parent1_y[i])

        # create
        sol_child1 = copy.deepcopy(self.sol_sample)
        sol_child2 = copy.deepcopy(self.sol_sample)

        sol_child1.x = child1_x
        sol_child1.y = child1_y
        sol_child1.tinhk_xy()

        if sol_child1.rang_buoc():
            child.append(sol_child1)

        sol_child2.x = child2_x
        sol_child2.y = child2_y
        sol_child2.tinhk_xy()

        if sol_child2.rang_buoc():
            child.append(sol_child2)
        
        return child, (child != []) 
    
    def _dotbien(self, sol_id):

        mutated_x = copy.deepcopy(self.pop[sol_id].x)
        mutated_y = copy.deepcopy(self.pop[sol_id].y)
        
        for i in range(len(mutated_x)):
            random_number = random.randint(0, self.sol_sample.K -1)
            mutated_x[i] = random_number  # Đột biến bit i của gen x

            if i < len(mutated_y):
                random_number = random.randint(0, self.sol_sample.K -1)
                mutated_y[i] = random_number  # Đột biến bit i của gen y
                
        sol_child = copy.deepcopy(self.sol_sample)
        sol_child.x = mutated_x
        sol_child.y = mutated_y
        sol_child.tinhk_xy()
        if sol_child.rang_buoc():
            return sol_child, True
        else:
            return None, False


    def _sol_not_in_pop(self, sol_test:Solution):
        for sol_i in self.pop:
            if (sol_i.x == sol_test.x):
                if (sol_i.y == sol_test.y):
                    return False
        return True
    def _not_in(self, chi, chi_return):
        for c in chi_return:
            if (chi.x == c.x) and (chi.y == c.y):
                return False
        return True
        

