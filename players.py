''' This file handles functionality of all players'''

class Moves:
    def __init__(self):
        pass

    def chess_map(self):
        chess_map_from_alpha_to_index={}
        chess_map_from_index_to_alpha={}
        alpha=['a','b','c','d','e','f','g','h']
        for i in range(0,8):
            chess_map_from_alpha_to_index[i]=alpha[i]

        chess_map_from_index_to_alpha={v:k for k,v in chess_map_from_alpha_to_index.items()}
        return chess_map_from_alpha_to_index,chess_map_from_index_to_alpha

    def Knight(self,x,y):
        potential_moves=[]
        try:
            potential_moves.append((x+2,y-1))
        except:
            pass
        try:
            potential_moves.append(x+2,y+1)
        except:
            pass
        try:
            potential_moves.append((x+1,y+2))

        except:
            pass

        try:
            potential_moves.append((x-1,y+2))
        except:
            pass
        try:
            potential_moves.append((x-2,y+1))

        except:
            pass

        try:
            potential_moves.append((x-2,y-1))
        except:
            pass
        try:
            potential_moves.append((x-1,j-2))
        except:
            pass
        try:
            potential_moves.append((x+1,j-1))

        except:
            pass
        allpossibleMoves=[]
        for x in potential_moves:
            if(x[0]>=0 and x[1]<=7):
                allpossibleMoves.append(x)

        return(allpossibleMoves)
                
           

       

            

'''   
move=Moves()
move.chess_map()
move.Knight(0,7)
'''

    