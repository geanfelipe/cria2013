#include <stdio.h>
#include <ctype.h> /*converte de minúscula para maiúscula e vice-versa*/

/*
São três salas idênticas com 360 lugares
*/

int posicoes_puladas=0;
int numero_da_poltrona;
char poltrona[3][21][20];
char matrizFileira[]="ABCDEFGHIJKLMNOPQRSTU";
char matrizFileiraInvalida[]="VXYZ";


/*declarando as funcoes*/
int letra_das_fileiras(char);
void iniciar();
char preencher(int, int, int);
char situacao_das_salas(void);

/*********************************OBSERVAÇAO***************************************/
/*se trocar a ordem de leitura de entrada do usuário dá bug na leitura da variável*/
/* 												     de nome caracter																		*/
/**********************************************************************************/
int main()
{
	char caracter,ok, status_das_salas;
	int filaLetra, sala,numero_da_poltrona,opcao, posicao_anterior='x';
	

	printf("\n                                   Seja Bem Vindo\n");
	printf("#");
	printf("\n|Salas existentes -> 1 a 3|\n|Letras das fileiras existentes -> A a U|\n|Número de poltronas existentes -> Fileira A até E: 1 a 8 de F até U: 1 a 20|\n");
	printf("#\n");
	printf("Opções de Navegação\n");

	while (1)   //loop principal do programa
	{
		printf("\n0) Sair\n");
		printf("1) Efetuar compra\n");
		printf("2) Situação das salas\n");

		while(1)  //loop das opcoes
		{
			printf(": ");
			scanf("%d",&opcao);
			if(opcao<4) break;
			else printf("\n");
		}
}
	return 0;
}
