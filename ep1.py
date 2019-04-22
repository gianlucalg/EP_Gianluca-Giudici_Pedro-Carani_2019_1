
# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Pedro Braga Carani, pedrobc1@al.insper.edu.br
# - aluno B: Gianluca Lazzaris Giudici, gianlucalg@al.insper.edu.br
nome=input('Qual seu nome?')
def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
        
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca",
                "esperar dupla": "Esperar a dupla do EP para fugir do insper",
                "predio 2": "Ir ate o Predio 2",
                "Tech Lab": "Ir para o -1"
                
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
                "aquario": "Ir para um aquario"
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
            "descricao": "No caminho, voce encontrou sua dupla e resolve conversar com ela",
            "opcoes":{
                 'inicio': 'voltar para o insper com sua dupla'}
            
                    
                    
        },
        'aquario': {
            'titulo':'em busca de algo',
            'descricao': 'voce esta em um aquario',
            'opcoes':{
                    "inicio":"sair"}
            },
        'predio 2': { 
            'titulo': 'Predio 2',
            'descricao': 'voce esta a procura do professor',
            'opcoes':{
                    'sala 114': 'ir ate a sala de aula',
                    'inicio': 'voltar para o predio1',
                    'Fab Lab':'ir para o FabLab'
                    }
            },
         'sala 114': {
            'titulo': 'sala de aula',
            'descricao': "esta tendo aula, o professor nao esta presente, no entanto, voce encontrou um portal que da acesso a sala do professor",
            'opcoes':{
                    'portal': 'acesso a sala do professor, e deu tudo certo o adiamento do EP',
                    'predio 2': 'nao confia no portal'}
            },
        'portal':{
            'titulo':'voce encontrou o professor',
            'descricao':'deu tudo certo com o adiamento, missao cumprida.',
            'opcoes':{}
            },
        'Fab Lab' : {
           'titulo':'Fab Lab',
           'descricao':'voce esta no Fab Lab, o professor nao esta aqui, cuidado com os monstros ao retornar!!!!',
           'opcoes':{
                   'predio 2':'voltar para o predio 2'
                   }
           },
        'Tech Lab' : { 
            'titulo': 'Tech Lab',
            'descricao':'voce esta no subsolo do predio 1 em busca do professor',
            'opcoes':{
                    'entrar':'entrar no Tech Lab',
                    'Baja':'ir para o Baja'}
          },
        'entrar' : {
            'titulo': 'Dentro da oficina',
            'descricao':'voce esta dentro do Tech lab, nao tem ninguem no local, só os monstros',
            'opcoes':{
                    'inicio':'ir embora correndo'}
          },
        'Baja':{
            'titulo': 'Baja',
            'descricao':'voce encontrou um tunel de acesso, parece que ele sai na biblioteca...',
            'opcoes':{
                    'bilioteca':'entrar no tunel'}
        }       
             
    }
          
           
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual
import time
import random


#FEATURE MONSTROS
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
    hit_point=20
    op=['correr', 'lutar', 'item']
    return monstros, vida, hit_point, op

#FEATURE PREMIOS
def rewards():
    premios=['Diploma', 'Carta da aprovacao', 'Passe livre']
    r=random.randint(0, 3)
    return premios[r]

   
chave=0
    


def main():
    
    #INICIO
    time.sleep(0.5)
    print()
    print("Na hora do sufoco!")
    print("------------------")
    time.sleep(0.2)
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    time.sleep(0.2)
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    time.sleep(0.2)
    print()
    print()
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()
    monstros, vida, hit_point, op = monsters()
    game_over = False
    game_win = False
    while not game_over and not game_win:
        
        cenario_atual = cenarios[nome_cenario_atual]
        #Geral
        time.sleep(0.2)
        print ()
        print ()
        print(cenario_atual['titulo'])
        time.sleep(0.2)
        print('-'*len(cenario_atual['titulo']))
        time.sleep(0.2)
        print(cenario_atual['descricao'])
        time.sleep(0.2)
        
        print()
        
        #FEATURE combate
        km=[]
        kv=[]

        for k, v in monstros.items():
            km.append(k) 
            kv.append(v)
    
        
        
        x=random.randint(1, 6)
       

 
      
        
        
        print('Sua Vida:{0}'.format(vida))
        print()
        
    
        i=random.randint(1, 50)
  


        opcoes = cenario_atual['opcoes']
        
        if len(opcoes) == 0:   
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
       
        
        #Rewards
        elif i==3:
              
              print (rewards())    
              print ('Voce foi bem sucedido na sua missao')
              game_over= True
        
        
        #vida
        elif vida ==0:
            game_over = True
        
        
        
        #SPAWN MONSTRO 1
        
        elif x==0: 
            print ('Apareceu um monstro chamado {}, voce pode correr dele ou enfrenta-lo!'.format(km[x]))
            print('opcoes:')
            w=0
            while w<len(op):
                
                print (op[w])
                w+=1
            vida_monstro1=40
            
            
            
            
            while vida_monstro1 != 0 and game_over==False:  
                x1=input('O que voce vai fazer?:')
            
                if x1 in op[1]:
                    y1=vida_monstro1
                    vida-=10
                    vida_monstro1-=20
                    
                    print ("a vida do monstro é {}".format(y1))
                    print ('Sua vida é {}'.format(vida))
                    print ('O seu ataque é {}'.format(hit_point))
                    
                    
                elif x1 in op[2]:
                    r=random.randint(0,4)
                    if r==2:
                        vida+=100 
                        print ('voce usou o item que te deu mais 100 de vida')
                    else:
                        print ('voce nao tem item')
                
                
                else:    
                    print ('Voce nao foi rapido suficiente...')
                    vida_monstro1=0
                    
                    
                    
            print ('Voce derrotou o monstro')    
        
        
        
        
        #Spawm Monstro 2
        
        
        
        elif x==1:
            print ('Apareceu um monstro chamado {}, voce pode correr dele ou enfrenta-lo!'.format(km[x]))
            print('opcoes:')
            w=0
            while w<len(op):
                
                print (op[w])
                w+=1
            vida_monstro2=40
           
            while vida_monstro2 != 0 and game_over==False:
                x1=input('O que voce vai fazer?:')
                if x1 in op[1]:
                    y2=vida_monstro2
                    vida_monstro2-=hit_point
                    vida-=10
                    print ("a vida do monstro é {}".format(y2))
                    print ('Sua vida é {}'.format(vida))
                    print ('O seu ataque é {}'.format(hit_point))
                elif x1 in op[2]:
                    r=random.randint(0,4)
                    if r==2:
                        vida+=100 
                        print ('voce usou o item que te deu mais 100 de vida')
                    else:
                        print ('voce nao tem item')
                
                else:    
                    print ('Voce nao foi rapido suficiente...')
                    game_over= True
                    
            print ('Voce derrotou o monstro, segue o jogo')  
            time.sleep(2)
        
        
        #Spawm monstro 3
        
        elif x==2:
            
            print ('Apareceu um monstro chamado {}, voce pode correr dele ou enfrenta-lo!'.format(km[x]))
            print()
            print('Opcoes:')
            w=0
            while w<len(op):
                
                print (op[w])
                w+=1
            vida_monstro3=60
            while vida_monstro3 != 0 and game_over==False: 
                
                x1=input('O que voce vai fazer?:')
                if x1 in op[1]:
                    y3=vida_monstro3
                    vida_monstro3-=hit_point
                    vida-=5
                    print ("a vida do monstro é {}".format(y3))
                    print ('Sua vida é {}'.format(vida))
                    print ('O seu ataque é {}'.format(hit_point))
                elif x1 in op[2]:
                    r=random.randint(0,4)
                    if r==2:
                        vida+=100 
                        print ('voce usou o item que te deu mais 100 de vida')
                    else:
                        print ('voce nao tem item')
                
                else:    
                    print ('Voce nao foi rapido suficiente...')
                    game_over= True
                    
            if vida_monstro3==0:        
                print ('Voce derrotou o monstro') 
            else: 
                print ('adeus')

        else:
            print ('Opcoes:')
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
            if escolha=='portal':
                game_win=True
            pocao=random.randint(0,5)
            if pocao ==2:
                print ('Voce achou a pocao magica, sua vida foi recuperada')
                vida=100
                
            if escolha in opcoes:
                nome_cenario_atual = escolha
      
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
            
                
    if i==3 or game_win==True:
        print ('PARABENS {}'.format(nome))
    elif vida==0:
        print('Voce morreu!')
  
    
      
    print("FIM!")


# Programa principal.
if __name__ == "__main__":
    main()
