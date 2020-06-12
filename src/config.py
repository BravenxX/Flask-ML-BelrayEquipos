# Sistem INFO
VERSION = "1.0.0"
NAME = "Analisis predictivo - Equipos Belray"

# Statement for enabling the development environment
DEBUG = True 

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  


# Model directory 
MODELS_DIR = os.path.abspath('../assets/models')  
MODELS_MACHINARY_ELEMENTS_DIR = os.path.abspath(f'{MODELS_DIR}/machinery_elements') 
