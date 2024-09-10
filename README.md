# CAS-Grab Python Scripts

A simple tool to fill in entries in the "Resources" tab of elabftw. 

## Usage
- Create a new Resources entry with the label "Chemical Compound" or "Polymer"
- Enter the *CAS Registry Number* in the *Title* field. Don't worry, this will be changed.
- Run main.py or set up an application to periodically run main.py

After main.py has been run, the CAS registry number in the title should have been moved to the appropriate field, being replaced by the name of the compound listed on Pubchem.
Other fields, including the SMILES and the chemical's full name will also automatically be entered.