from collections import namedtuple
import pandas as pd
import streamlit as st
from stmol import showmol
import py3Dmol

"""
# Basic Smina Protein-ligand Docking (Re-Docking)


    RamirezLab
    Mr. Ignacio Valenzuela Martínez
    v.3
    October 2022
"""

with st.echo(code_location='below'):
    from rdkit import Chem
    from rdkit.Chem import AllChem, Draw
    import py3Dmol

    #Parameters

    view = py3Dmol.view(query='pdb:1A2C')
    view.removeAllModels()
    view.setViewStyle({'style':'outline','color':'black','width':0.1})

    # Receptor 

    view.addModel(open('{0}_clean.pdb'.format(pdb_code),'r').read(),format='pdb')
    Prot=view.getModel()
    Prot.setStyle({'cartoon':{'arrows':True, 'tubes':True, 'style':'oval', 'color':'white'}})
    view.addSurface(py3Dmol.VDW,{'opacity':0.6,'color':'white'})

    # Reference Ligand

    view.addModel(open('{0}_ligand.pdb'.format(pdb_code),'r').read(),format='pdb')
    ref_m = view.getModel()
    ref_m.setStyle({},{'stick':{'colorscheme':'magentaCarbon','radius':0.2}})

    # Docking Result

    results=Chem.SDMolSupplier('{0}_docking.sdf'.format(pdb_code))

    p=Chem.MolToMolBlock(results[1],False)  # [0] give you the first result from docking, to view another change this value
    p2=Chem.MolToMolBlock(results[1],False)
    # Print Score

    print('Reference: Magenta | Smina Pose: Cyan')
    print ('Score: {}'.format(results[0].GetProp('minimizedAffinity')))  # If change docking result above, change this value too

    view.addModel(p,'mol')
    x = view.getModel()
    x.setStyle({},{'stick':{'colorscheme':'cyanCarbon','radius':0.2}})


    #Visualization

    view.zoomTo()
    view.show()
