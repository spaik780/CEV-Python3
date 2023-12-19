# Biblioteca para checar gramática em Python.
# https://pypi.org/project/language-tool-python/
import language_tool_python

# Função para encontrar a enésima ocorrência em um texto.
# textToSearch : Texto que será efetuada a pesquisa.
# searchText   : Termo a ser procurado em textToSearch.
# nthOcurrence : Qual ocorrência a função retornará o índice.
def findNthOccurrence(textToSearch, searchText, nthOccurence):
	index = -1
	for _ in range(nthOccurence):
		index = textToSearch.find(searchText, index+1)
	return index

# Função para receber o enunciado do exercício.
def getExerciseHeader(exerciseText):
	startIndex = findNthOccurrence(exerciseText, '"""', 1)
	endIndex = findNthOccurrence(exerciseText, '"""', 2)
	header = exerciseText[startIndex+4:endIndex-1]
	return header

print("Analisando gramática dos enunciados...")
for exerciseIndex in range(1, 115):
	fileName = "ex{:0>3}.py".format(exerciseIndex)
	fileText = open(f"Exercícios/{fileName}", encoding="UTF-8").read()

	header = getExerciseHeader(fileText)
	languageTool = language_tool_python.LanguageToolPublicAPI("pt-BR")
	matches = languageTool.check(header)

	if matches:
		for match in matches:
			print("{:-^120}".format(fileName))
			matchContent = match.__dict__
			print(matchContent["message"])
			print("Sugestões:", matchContent["replacements"])
			print(matchContent["context"])
			print(" " * matchContent["offsetInContext"] + "^" * matchContent["errorLength"])
print("-" * 120)
print("Fim da Análise.")
