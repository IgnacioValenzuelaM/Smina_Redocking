from collections import namedtuple
import pandas as pd
import streamlit as st

"""
# Basic Smina Protein-ligand Docking (Re-Docking)


    RamirezLab
    Mr. Ignacio Valenzuela Martínez
    v.3
    October 2022
"""

with st.echo(code_location='below'):
    from stmol import showmol
    import py3Dmol
    # 1A2C
    # Structure of thrombin inhibited by AERUGINOSIN298-A from a BLUE-GREEN ALGA
    xyzview = py3Dmol.view(query='pdb:1A2C') 
    xyzview.setStyle({'cartoon':{'color':'spectrum'}})
    showmol(xyzview, height = 500,width=800)
    from stmol import *
    showmol(render_pdb(id = '1A2C'))
