from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.output_parsers import PydanticToolsParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.runnables.utils import Output
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain_core.tools import tool



def chain_template_llm_example():
    # ChatPrompt
    print("###########")
    template1=ChatPromptTemplate.from_template("Erstelle ein Rezept mit diesen Zutaten: {ai_argument}")
    print(template1.invoke(input={"ai_argument":"Erdbeeren"}))
    print("###########")
    template2=PromptTemplate.from_template("Erstelle ein Rezept mit diesen Zutaten: {ai_argument}")
    print(template2.invoke(input={"ai_argument":"Pflaumen"}))
    print("###########")
    llm=ChatOllama(model="llama3")
    ergebnis=llm.invoke("Himbeeren")
    print(ergebnis)
    print("###########")
    chain1= template1 | llm
    print(chain1.invoke(input={"ai_argument":"Erdnüsse"}))
    print("###########")
    chain2= template2 | llm
    print(chain2.invoke(input={"ai_argument": "Apfel"}))


def chain_template_llm_parser_example(argument="Nüsse"):
    # ChatPrompt
    print(__name__,__file__)
    template1=ChatPromptTemplate.from_template("Erstelle ein Rezept mit diesen Zutaten: {ai_argument} auf Deutsch")
    llm=ChatOllama(model="llama3")

    parser=StrOutputParser()
    chain=template1|llm|parser

    return chain.invoke(input={"ai_argument":argument})

# print(chain_template_llm_parser_example())


def chain_chain(argument="Nüsse"):
    # ChatPrompt
    print(__name__,__file__)
    template1=ChatPromptTemplate.from_template("Gib mir ein Rezept mit: {ai_argument} auf Deutsch")
    llm=ChatOllama(model="llama3")
    template2=ChatPromptTemplate.from_template(" {recipe} zu welcher Kategorie gehört das Rezept? auf Deutsch")

    parser=StrOutputParser()
    chain1=template1|llm
    chain2=template2|llm|parser
    chain3=chain1|chain2
    return chain3.invoke(input={"ai_argument":argument})
# print(chain_chain())


@tool(description="""Benutze das tool um die Rezepte mit Kategorie schön darzustellen""")
def layout_tool(rezept: str, kategorie: str) -> str:
    layout_strich = 40 * "_"
    result = f"{rezept=}\n\n{layout_strich}\n\n{kategorie=}"
    return layout_strich + result + layout_strich


@tool
def multiply(first_int: int, second_int: int) -> int:
    """Multiply two integers together."""
    return first_int * second_int

print(multiply)
ergebnis=multiply.invoke({"first_int": 4, "second_int": 5})
print(ergebnis)
print(multiply.name)
print(multiply.description)
print(multiply.args)

def chain_chain_tool(argument="Nüsse")->Output:
    # ChatPrompt
    print(__name__,__file__)
    template1=ChatPromptTemplate.from_template("Gib mir ein Rezept mit: {ai_argument} auf Deutsch")
    template2=ChatPromptTemplate.from_template("{recipe} zu welcher Kategorie gehört das Rezept?Benutze das layout_tool ")
    llm=ChatOllama(model="llama3")
    llm_with_tools=ChatOllama(model="llama3-groq-tool-use").bind_tools(tools=[layout_tool])
    parser=StrOutputParser()
    # chain1=template1|llm
    chain2=template2|llm_with_tools
    # chain3=chain1|chain2
    return chain2.invoke(input={"recipe":argument})

for i in range(10):
    ergebnis=chain_chain_tool("Erdbeertorte, 500 g erdbeeren zermatschen und milch dazu gießen")
    print(ergebnis.tool_calls)
    print(ergebnis.content)
    print(ergebnis)

# print(chain_chain_tool())


