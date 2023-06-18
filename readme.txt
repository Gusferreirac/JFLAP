Intruções para uso correto do programa

1- Programas necessários:
	
	. É necessário instalar o Graphviz, caso ainda não esteja instalado na máquina. Este é responsável por gerar as imagens dos autômatos

2- Formato dos autômatos (JSON):

	.AFD (os nomes das variáveis devem ser os mesmos que os abaixo e na sequinte ordem):
	
		.states: consiste em uma lista informando os estados do autômato
		.input_symbols: consiste em uma lista informando os caracteres do autômato
		.trasitions: consiste em um dicionario informando as transições do autômato. O dicionario deve estar no formato "q0":{"0":"q0"} (nesse caso q0 quando recebe 0 ativa q0)
		.initial_state: consiste no estado inicial do autômato.
		.final_states: consiste em uma lista de estados finais
		
		Exemplo de um arquivo de AFD
		
		{
		  "states": [ 
			"q0",
			"q1",
			"q2"
		  ],
		  "input_symbols": [ 
			"0",
			"1"
		  ],
		  "trasitions": { 
			"q0": {"0":"q0","1":"q1"}, 
			"q1": {"0":"q0", "1":"q2"},
			"q2": {"0":"q2","1":"q1"}
		  },
		  "initial_state": "q0",
		  "final_states":["q1"]
		}
		
	.AFN (os nomes das variáveis devem ser os mesmos que os abaixo e na sequinte ordem):	
		.states: consiste em uma lista informando os estados do autômato
		.input_symbols: consiste em uma lista informando os caracteres do autômato
		.trasitions: consiste em um dicionario informando as transições do autômato. O dicionario deve estar no formato "q0":{"a":["q0"]} (diferente do afd no afn os caracteres podem ativar multiplos estados então o valor atrelado ao caractere deve ser uma lista de estados). Além disso "" indica uma trasição vazia ("q0":{"":["q1"]} indica transição vazia de q0 pra q1).
		.initial_state: consiste no estado inicial do autômato.
		.final_states: consiste em uma lista de estados finais
		
		Exemplo de um arquivo de AFN
		
		{
		  "states": [
			"q0",
			"q1",
			"q2"
		  ],
		  "input_symbols": [
			"a",
			"b"
		  ],
		  "trasitions": {
			"q0": {"a":["q1"]},
			"q1": {"a":["q1"], "":["q2"]},
			"q2": {"b":["q0"]}
		  },
		  "initial_state": "q0",
		  "final_states":["q1"]
		}