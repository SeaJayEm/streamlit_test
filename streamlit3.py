import streamlit as st
from streamlit_authenticator import Authenticate
import streamlit as st
# Importation du module
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()

def afficher_contenu(selection):
    if selection == "Accueil":
        st.write("Bienvenue sur la page d'accueil !")
    elif selection == "Photos":
        st.write("Bienvenue sur mon album photo")

if st.session_state["authentication_status"]:
    st.title("Bienvenue sur le contenu réservé aux utilisateurs connectés")

    # Création du menu
    with st.sidebar:
        selection = option_menu(
            menu_title="Menu",
            options=["Accueil", "Photos"],
            icons=["house", "camera"],
            menu_icon="cast",
            default_index=0
    )

    # Affichage du contenu en fonction de la sélection
    afficher_contenu(selection)

    # Le bouton de déconnexion
    authenticator.logout("Déconnexion")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplis')