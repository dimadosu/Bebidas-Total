import streamlit as st
import requests

# URL base de la API de TheCocktailDB
API_URL = "https://www.thecocktaildb.com/api/json/v1/1"

# Función para obtener la lista de bebidas populares
def get_popular_drinks():
    response = requests.get(f"{API_URL}/filter.php?a=Alcoholic")
    data = response.json()
    return data.get('drinks', [])

# Función para buscar una bebida por nombre
def search_drink_by_name(name):
    response = requests.get(f"{API_URL}/search.php?s={name}")
    data = response.json()
    return data.get('drinks', [])



# Título de la aplicación
st.title("Explorador de Bebidas")

# Intro de la pagina web 

with st.container():
    st.write(""" 
        En esta página podrás buscar una bebida de tu preferencia, se mostrará información, 
        los ingredientos y los pasos para que puedas prepararlo.
        ¡Qué lo disfrutes! """)

# Sidebar para búsqueda
st.sidebar.header("Buscar una bebida")
search_term = st.sidebar.text_input("Nombre de la bebida")

# Si hay un término de búsqueda, mostrar resultados de búsqueda
if search_term:
    st.header(f"Resultados de búsqueda para '{search_term}'")
    search_results = search_drink_by_name(search_term)
    
    if search_results:
        for drink in search_results:
            st.subheader(drink["strDrink"])
            st.image(drink["strDrinkThumb"], width=200)
            st.write(f"**Categoría**: {drink['strCategory']}")
            st.write(f"**Alcoholic**: {drink['strAlcoholic']}")
            st.write(f"**Instrucciones**: {drink['strInstructions']}")
            
            ingredients = []
            for i in range(1, 16):
                ingredient = drink.get(f"strIngredient{i}")
                measure = drink.get(f"strMeasure{i}")
                if ingredient:
                    ingredients.append(f"{ingredient} - {measure}")
            st.write("**Ingredientes**:")
            st.write("\n".join(ingredients))
            
    else:
        st.write("No se encontraron resultados.")

# Mostrar bebidas populares
st.header("Bebidas Populares")
popular_drinks = get_popular_drinks()

for drink in popular_drinks:
    st.subheader(drink["strDrink"])
    st.image(drink["strDrinkThumb"], width=200)



