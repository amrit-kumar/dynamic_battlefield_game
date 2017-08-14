from random import randint
# import numpy

class Battleship(object):

    def __init__(self):
        self.ocean_matrix_g = []
        self.ship_list_g=[]

    def define_ocean(self):
        # global ocean_matrix
        ocean_matrix=[]

        #ocean_size = input("give your ocean size!!").split(',')
        global m,n
        m,n=0,0
        try:
            n=int(input("enter number of row for ocean_matrix:"))
            m=int(input("enter number of column for ocean_matrix:"))
            for i in range(1, m * n, m):
                row_matrix = []
                for k in range(i, i + m, 1):
                    row_matrix.append(k)
                ocean_matrix.append(row_matrix)
            print("ocean_matrix", ocean_matrix)

        except Exception as e:
            print(str(e))
        self.ocean_matrix_g=ocean_matrix
        return ocean_matrix

    def define_ship(self):

        ship_list = []
        while True:
            inp=input("enter (y or yes) to enter a new ship or enter anything else to terminate ship input:")

            if inp=='yes' or inp=='y':

                ship_start_point=input("enter starting point coordinates of ship seperated by comma:").split(',')
                ship_end_point=input("enter end point coordinates of ship seperated by comma:").split(',')

                l=int(ship_start_point[0])
                m=int(ship_start_point[1])
                n=int(ship_end_point[0])
                o=int(ship_end_point[1])
                if m>o or l>n:
                    print("End point coordinates must be gretaer than starting point coordinates")
                    continue
                for i in range(l,n+1,1):
                    for j in range(m,o+1,1):
                        # print("iiii",i,"jjjjj",j,"elementssssssssssssss",self.ocean_matrix_g[i][j])
                        if self.ocean_matrix_g[i][j] in ship_list:
                            print('Ship cannot overlap enter other cordinates')
                            continue

                        ship_list.append(self.ocean_matrix_g[i][j])
                        # print("ship_list@@@@@@@@@@@@@@@@@@@@@@@@", self.ocean_matrix_g[i][j])

            else:
                break
            self.ship_list_g=ship_list
        return ship_list


def war(self):
    a_is_attacker=True

    while len(a_obj.ship_list_g)!=0 and len(b_obj.ship_list_g)!=0:
        if a_is_attacker:
            try:
                ship_attack_point = input(
                    " Hi 'A' enter attack point coordinates of ship seperated by comma:").split(',')
                x = int(ship_attack_point[0])
                y = int(ship_attack_point[1])
                if 0<=x<m or 0<=y<n:
                    print("Enter First value between 0 to {} and second value between {}".format(m, n))

                value = b_obj.ocean_matrix_g[x][y]
                print("value", value)
            except Exception as e:
                print(str(e))

            if value in b_obj.ship_list_g:
                print("attack successful")
                b_obj.ship_list_g.remove(value)
                if not b_obj.ship_list_g:
                    print("A IS THE WINNER!!!!!!!!!!!!!")
                    break
            else:
                a_is_attacker=False

        else:
            try:
                ship_attack_point = input(
                    " Hi 'B' enter attack point coordinates of ship seperated by comma:").split(',')

                x = int(ship_attack_point[0])
                y = int(ship_attack_point[1])
                if 0<=x<m or 0<=y<n:
                    print("Enter First value between 0 to {} and second value between 0 to {}".format(n-1,m-1))

                value = a_obj.ocean_matrix_g[x][y]
                print("value", value)

            except Exception as e:
                print(str(e))

            if value in a_obj.ship_list_g:
                print("attack successful")
                a_obj.ship_list_g.remove(value)
                if not a_obj.ship_list_g:
                    print("B IS THE WINNER!!!!!!!!!!!!!")
                    break
            else:
                a_is_attacker=True


a_obj=Battleship()
b_obj=Battleship()

a_obj.ocean_matrix1=a_obj.define_ocean()
b_obj.ocean_matrix1=b_obj.define_ocean()

a_obj.ship_list_g=a_obj.define_ship()
b_obj.ship_list_g=b_obj.define_ship()

war(self=object)

