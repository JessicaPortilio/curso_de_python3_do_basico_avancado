"""
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte

Tipagem fraca e forte são termos usados para descrever como os tipos de dados são verificados e gerenciados em diferentes linguagens de programação.

Uma tipagem fraca, também conhecida como tipagem dinâmica, é caracterizada por não verificar o tipo de dado de uma variável em tempo de compilação. Isso significa que o tipo de uma variável pode ser alterado em tempo de execução e que as operações podem ser realizadas entre variáveis de tipos diferentes sem gerar um erro. Isso pode ser vantajoso, já que permite maior flexibilidade e facilidade na escrita do código, mas pode também ser um problema, já que pode levar a erros de tempo de execução difíceis de detectar.

Uma tipagem forte, por outro lado, é caracterizada por verificar o tipo de dado de uma variável em tempo de compilação. Isso significa que o tipo de uma variável é fixo e não pode ser alterado em tempo de execução e que as operações só podem ser realizadas entre variáveis do mesmo tipo. Isso pode ser vantajoso, já que ajuda a evitar erros de tempo de execução, mas pode também ser um problema, já que pode levar a uma maior verbosidade no código e dificultar a escrita do mesmo.

Algumas linguagens, como Python, Ruby, JavaScript, entre outras, são consideradas de tipagem dinâmica, enquanto outras, como C, C++, Java, C# são consideradas de tipagem estática.

É importante lembrar que existem diferentes gradações entre a tipagem fraca e forte, o que pode ser considerado tipagem fraca para alguns, pode ser forte para outros e algumas linguagens podem oferecer mecanismos para combinar ambos.

str -> string -> texto
Strings são textos que estão dentro de aspas

"""

# Aspas simples
print('Jessica')
print(1, 'Jessica "Aspas duplas"')

# Aspas duplas
print("Jessica")
print(2, "Jessica 'Aspas simples'")

# Escape
print("Jessica \"Colocar aspas\"")

# r
print(r"Jessica \"Tudo que está na string\"")
