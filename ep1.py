
# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Pedro Braga Carani, pedrobc1@al.insper.edu.br
# - aluno B: Gianluca Lazzaris Giudici, gianlucalg@al.insper.edu.br

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
        
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca",
                "esperar dupla": "Esperar a dupla do EP para fugir do insper"
                
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
                        
         
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "sala do professor": "Falar com o professor",
            }
        },    
        'sala do professor': {
            'titulo': 'Sala trancada',
            'descricao':'A sala esta trancada',
            'opcoes': {
                'inicio':"Tomar o elevador para o saguao de entrada em busca da chave",  
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
          
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "Aquario": "Ir para um aquario"
            }
        },
        "esperar dupla": {
            "titulo": "Amigo demais",
            "descricao": "Voce esta revoltado demais pela demora da sua dupla, e resolve ir embora do insper e desistir do curso",
            "opcoes": {
                "ir embora": "Ir embora do insper",
                "inicio": "Pensou melhor e resolveu voltar para a entrada do Insper"
                }
        },
        "ir embora": {
            "titulo": "Adeus",
            "descricao": "Voce foi embora",
            "opcoes": {}
        },    
        'Aquario': {
            'titulo':'em busca de algo',
            'descricao': 'voce esta em um aquario',
            'opcoes':{
                    "inicio":"sair"}
            }
    
                
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

import random
def monsters():
    monstros={'Aobsil':{
                'vida':100,
                'hit_point':10},
                    
              'Luar': {
                      'vida':1000,
                      'hit_point':20},
              'Pi': {10000:0}
              }
    vida=100
    hit_point=0
    op=['correr',
        'lutar']
    return monstros, vida, hit_point, op

def rewards():
    premios=['Diploma', 'Carta da aprovacao', 'Passe livre']
    r=random.randint(0, 3)
    return premios[r]

   

    


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()
    monstros, vida, hit_point, op = monsters()
    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        #Geral
        print(cenario_atual['titulo'])
        print('-'*len(cenario_atual['titulo']))
        print(cenario_atual['descricao'])
        
        
        
        km=[]
        kv=[]

        for k, v in monstros.items():
            km.append(k) 
            kv.append(v)
    
        
        
        x=random.randint(0, 4)
       

            

 
      
        
        
        print('Sua Vida:{0}'.format(vida))
        i=random.randint(1, 10)
  


        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:   
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        elif i==3:
              
              print (rewards())    
              print ('Voce foi bem sucedido na sua missao')
              game_over= True

        elif x==0: 
            print ('Apareceu um monstro chamado {}, voce pode correr dele ou enfrenta-lo!'.format(km[x]))
            print('opcoes:')
            w=0
            while w<len(op):
                
                print (op[w])
                w+=1
            x1=input('O que voce vai fazer?:')
            if x1 in op[1]:
                
                vida-=10
                
            else:    
                print ('Voce nao foi rapido suficiente...')
                game_over= True
                
        else:
            print ('opcoes:')
            ks=[]
            vs=[]
            for k,v in opcoes.items():
                ks.append(k)
                vs.append(v)
            c=0
            while c<len(ks):
                print('{0}:{1}'.format(ks[c],vs[c]))
                c+=1
            
            
            escolha=input('qual sua escolha? ')
            

            if escolha in opcoes:
                nome_cenario_atual = escolha
               
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
            
                
    if i==3:
        print ('PARABENS')
    else:    
        print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()