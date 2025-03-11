# Python Tutorial
from langchain_core.tools import tool


# Funktionen I

# Definition der simpelsten art von einer Funktion ohne optionalen Typinformation
def easy_function():
    print("easy_function")
    return

# Definition einer simplen Funktion mit optionalen Typinformation
def easy_function_type_hints()->None:
    print("easy_function_type_hints")
    return None

# Definition einer simplen Funktion mit optionalen Typinformation und mit optionalem Docstring im google style
def easy_function_type_hints_with_docstring()->None:
    """
    Testfunktion mit einer Ausgabe

    Returns:
        nur None wird zurückgegeben
    """
    print("easy_function_type_hints")
    return None

# Aufrufe
easy_function_type_hints_result:None=easy_function_type_hints()
easy_function_result:None=easy_function()
easy_function_type_hints_with_docstring:None=easy_function_type_hints_with_docstring()
print(easy_function_result)

@tool(parse_docstring=True,error_on_invalid_docstring=True)
def multiplizieren(non_default_argument_2:int,default_argument_1:int=2,)->int:
    """
    Funktion multipliziert zwei Zahlen miteinander und liefert das Ergebnis zurück

    Args:
        non_default_argument_2(int): Faktor1 der Multiplikation
        default_argument_1(int): Faktor2 der Multiplikation

    Returns:
        (int): Ergebnis einer Multiplikation
    """
    return non_default_argument_2*default_argument_1

ergebnis:int=multiplizieren(234)
print(ergebnis)

def funktionsname_3(non_default_argument1,non_default_argument2:int,default_argument1:int=1324,default_argument2:any=1234,*tuple_args,**dict_args):
    """
    Funktion multipliziert zwei Zahlen miteinander und liefert das Ergebnis zurück

    Args:
        non_default_argument1: Faktor1 der Multiplikation
        non_default_argument2 (int): Faktor1 der Multiplikation
        default_argument1 (int): Faktor2 der Multiplikation
        default_argument2 (any):test

    Returns:
        (int): Ergebnis einer Multiplikation
    """
    non_default_argument1:any=non_default_argument1
    non_default_argument2:int=non_default_argument2
    default_argument_1:int
    default_argument2:any
    listwargs:tuple=tuple_args
    keyvargs:dict=dict_args
    print(non_default_argument1,non_default_argument2,default_argument1,default_argument2,tuple_args,dict_args,listwargs,keyvargs)
    return
funktionsname_3(non_default_argument1="arg1",non_default_argument2=2,default_argument_1=234,default_argument2="sfeeg",*("tuplearg1","tuplearg2"),**{"test":1234})

# integer/Ganzahlen
def datentypen_funktion():
    # integer
    a=10 # Variablen deklaration ohne typ hint
    b:int=20   # variablen deklaration mit optionalen Typhinweis Vorteil: die IDE weiß besser Bescheid über das was du machen willst und kann helfen
    erster_wert = 10
    zweiter_wert = 20
    ergebnis = erster_wert + zweiter_wert
    print(ergebnis)
    ergebnis = erster_wert - zweiter_wert
    print(ergebnis)
    ergebnis = erster_wert / zweiter_wert
    print(ergebnis)

    print(a+b) # Ausgaben mit print()
    print("Hier eine Variante ohne fstring a+b=", a+b) # Ausgabe von eineme literal und einer Variablen
    print(f"Eine zusätzliche Erklärung der obigen Ausgabe in Form eines Textes {a+b=}") # andere Möglichkeit einer Ausgabe

    # Strings/Texte
    satzanfang:str="Hier grast "
    satzmitte="ein Kamel "
    satzende="in der Wüste."
    zusammengesetzter_satz=satzanfang+satzmitte+satzende   # string concatenation, man kann Texte zusammenfügen
    print(zusammengesetzter_satz)
    neuer_satz=zusammengesetzter_satz.replace("Kamel", "Schildkröte")
    print(neuer_satz)

    satz_als_liste=zusammengesetzter_satz.split()
    print(satz_als_liste)

    # list/Liste
    list_empty:list=[] # leere Liste erstellt
    print("Ich bin eine leere Liste",list_empty)
    list_integer=[0,1,2,3] # gefüllte Liste mit integers
    print("Ich bin eine befüllte Liste",list_integer)


    # if elif else / wenn dann
    if len(list_integer)>=5: # größer gleich 4
      print("schlecht")
    elif list_integer[0]!=0: # ungleich 0
      print("schlecht")
    elif len(list_integer)>=4: # größer gleich 4
      print("gut")
    else:
      print("schlecht")

      # for loop/ for Schleife
      liste2 = []
      for element in list_integer:
          liste2.append(f"Nr. {element}")
      print(liste2)
      list_comrehension_example = [f"Nr. {element}" for element in list_integer]  # kompaktere Variante
      print("kompaktere Version (im code):", list_comrehension_example)