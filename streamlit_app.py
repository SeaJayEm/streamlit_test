# pipreqs C:\Users\clair\OneDrive\Documents\Wild\Quetes\

import streamlit as st
from streamlit_authenticator import Authenticate
import streamlit as st
# Importation du module
from streamlit_option_menu import option_menu
import pandas as pd

# Appliquer le style avec CSS
st.markdown("""
    <style>
    /* Fond général de la page */
    .stApp {
        background-color: #ffffff;
    }
    /* Titre Login */
    h3 {
        font-size: 24px;
        margin-bottom: 20px;
        color: #333333;
    } 
    h1 {
        font-size: 34px;
        margin-bottom: 20px;
        color: #333333;
    }    
    h2 {
        font-size: 24px;
        margin-bottom: 10px;
        color: #333333;
    } 
    p {
        color: #333333;
    }
    .st-emotion-cache-1n47svx {
        background-color: #f8f9fa; 
        border: 1px solid #333333 !important;
    }            
    /* Champs de saisie */
    .stTextInput input {
        background-color: #f8f9fa !important;
        color: #000000 !important;
        border: 1px solid #dee2e6 !important;
        border-radius: 4px !important;
        padding: 8px 12px !important;
        font-size: 14px !important;
        width: 100% !important;
        box-shadow: none !important;
    }
    /* Labels des champs */
    .stTextInput label {
        color: #495057 !important;
        font-size: 14px !important;
        font-weight: normal !important;
        margin-bottom: 5px !important;
    }
    /* Bouton de connexion */
    .stButton button {
        background-color: #ffffff !important;
        color: #495057 !important;
        border: 1px solid #ced4da !important;
        border-radius: 4px !important;
        padding: 6px 12px !important;
        font-size: 14px !important;
        font-weight: normal !important;
        width: auto !important;
        margin-top: 10px !important;
    }
    /* Reset complet du style des alertes */
    .stAlert > div {
        padding: 0 !important;
        border: none !important;
        background-color: transparent !important;
    }    
    /* Style unique pour le message */
    .stAlert {
        background-color: #fff3cd !important;
        color: #856404 !important;
        border: 1px solid #ffeeba !important;
        border-radius: 4px !important;
        padding: 12px !important;
        margin: 10px 0 !important;
    }
    /* Suppression des styles du conteneur parent */
    div[data-stale="false"] > div:has(.stAlert) {
        background: none !important;
        border: none !important;
    }
    /* Suppression de la marge intérieure */
    .stAlert > * {
        margin: 0 !important;
    } 
    /* Style de la sidebar */
    [data-testid="stSidebar"] {
        background-color: #D2D3D4 !important;
        padding: 1rem;
    }               
    /* Style du bouton déconnexion */
    .stButton button {
        background-color: white !important;
        color: #212529 !important;
        border: none !important;
        border-radius: 4px !important;
        padding: 8px 16px !important;
        width: 100% !important;
        margin-bottom: 1rem !important;
    }
    .header-center {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Charger les données depuis le fichier CSV
def charger_comptes_depuis_csv(fichier_csv):
    df = pd.read_csv(fichier_csv)
    comptes = {"usernames": {}}
    for _, row in df.iterrows():
        comptes["usernames"][row["username"]] = {
            "name": row["username"],
            "password": row["password"],
            "email": row["email"],
            "failed_login_attemps": row["failed_login_attempts"],
            "logged_in": row["logged_in"],
            "role": row["role"]
        }
    return comptes

# Appeler la fonction pour charger les comptes
lesDonneesDesComptes = charger_comptes_depuis_csv("comptes.csv")

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)
authenticator.login()

utilisateur = st.session_state.get("name", "utilisateur inconnu")

def afficher_contenu(selection):
    if selection == "👋 Accueil":
        st.write("Bienvenue sur la page d'accueil !")
    elif selection == "🐱 Photos de Gaïa":
        st.markdown('<h3 class="header-center">Voici mon album de photos de Gaïa, le plus beau chat du monde !</h1>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('<h2 class="header-center">Beautiful Gaïa</h1>', unsafe_allow_html=True)
            st.image("https://raw.githubusercontent.com/SeaJayEm/streamlit_test/refs/heads/main/gaia1.jpg")

        with col2:
            st.markdown('<h2 class="header-center">Sleepy Gaïa</h1>', unsafe_allow_html=True)
            st.image("https://raw.githubusercontent.com/SeaJayEm/streamlit_test/refs/heads/main/gaia2.jpg")

        with col3:
            st.markdown('<h2 class="header-center">Wild Gaïa</h1>', unsafe_allow_html=True)
            st.image("https://raw.githubusercontent.com/SeaJayEm/streamlit_test/refs/heads/main/gaia3.jpg")
                  
if st.session_state["authentication_status"]:
    # Création du menu
    with st.sidebar:
        st.write(f"Bienvenue {utilisateur}")
            # Le bouton de déconnexion
        authenticator.logout("Déconnexion")
        selection = option_menu(
            menu_title="Menu",
            options=["👋 Accueil", "🐱 Photos de Gaïa"],            
            default_index=0,
            styles={
        "container": {
            "padding": "0!important", 
            "background-color": "#D2D3D4!important",
            "margin": "0!important"
        },
        "icon": {"color": "black", "font-size": "16px"},
        "nav-link": {
            "color": "#333333",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "#4a4a4a"
        },
        "nav-link-selected": {"background-color": "#dc3545"},
        "menu-title": {
            "color": "#333333",
            "background-color": "#D2D3D4!important",
            "font-weight": "bold",
            "font-size": "20px",
            "padding": "10px",
            "margin": "0!important"
        },
        ".menu-title.align-items-center": {
            "background-color": "#D2D3D4!important",
            "margin": "0!important"
        },
        "menu": {
            "background-color": "#D2D3D4!important",
            "padding": "0px"
        },
        # Ciblage plus large
        "[data-v-5af006b8]": {
            "background-color": "#D2D3D4!important"
        },
        # Ciblage des éléments nav et leurs conteneurs
        "nav": {
            "background-color": "#D2D3D4!important",
            "margin": "0!important",
            "padding": "0!important"
        },
        ".nav-container": {
            "background-color": "#D2D3D4!important",
            "margin": "0!important",
            "padding": "0!important"
        },
        "nav-link": {
            "color": "#333333",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "#4a4a4a",
            "border": "none!important",  # Ajout de cette ligne
            "border-bottom": "none!important"  # Et celle-ci
        },
    }
    )
    # Affichage du contenu en fonction de la sélection
    afficher_contenu(selection)

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplis')
