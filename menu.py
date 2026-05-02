from dashboard import dashboard
from filabacklog import filabacklog
from pilharecentes import PilhasRecentes
from recomendações import recomendar_jogos
from ranking import gerar_ranking
from registros import registrar_sessao
from carregar_dados import carregar_jogos

def menu():
    print("\nCarregando jogos...")
    lista_jogos = carregar_jogos()
    print(f"✓ {len(lista_jogos)} jogos carregados!")
    
    backlog = filabacklog()
    recentes = PilhasRecentes()
    
   
    print("\nPopulando backlog...")
    for jogo in lista_jogos:
        backlog.enqueue(jogo)
    print(f"✓ Backlog pronto com {backlog.tamanho()} jogos!\n")
    
    historico = []
    tempo_total = {}

    while True:
        try:
            print("\n" + "="*40)
            print("1. Ver backlog")
            print("2. Jogar próximo")
            print("3. Ver recentes")
            print("4. Registrar sessão")
            print("5. Recomendações")
            print("6. Ranking")
            print("7. Dashboard")
            print("0. Sair")
            print("="*40)

            op = input("\nEscolha: ").strip()

            if op == "1":
                print("\n--- VER BACKLOG ---")
                backlog.mostrar()

            elif op == "2":
                jogo = backlog.dequeue()
                if jogo:
                    recentes.push(jogo)
                    print("\n==== JOGANDO ====")
                    jogo.exibir()
                    print("================\n")
                else:
                    print("❌ Backlog vazio! Não há jogos para jogar.")

            elif op == "3":
                recentes.mostrar()

            elif op == "4":
                if not recentes.is_empty():
                    jogo = recentes.topo()
                    tempo = float(input("Tempo jogado: "))
                    registrar_sessao(jogo, tempo, historico, tempo_total)

            elif op == "5":
                recomendar_jogos(lista_jogos, historico, tempo_total)

            elif op == "6":
                gerar_ranking(tempo_total)

            elif op == "7":
                dashboard(lista_jogos, backlog, recentes, historico, tempo_total)

            elif op == "0":
                print("Saindo...")
                break
            
            else:
                print("❌ Opção inválida!")
        
        except Exception as e:
            print(f"❌ Erro: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    menu()
