# ⚠ Deprecated Repository ⚠
As this project expanded, it made sense to move each of the modules contained in this project to their own repositories, as different parts of the code were intended to be run in completely different environments. 
See:
https://github.com/ddomlab/eln_packages_frontend
https://github.com/ddomlab/eln_packages_backend
https://github.com/ddomlab/eln_packages_common

This repository should be archived, but I do not have access to the settings required to archive the repository.

# CAS-Grab Inventory Managing Tools

A set of tools written in Python to manage inventory and experiments at eln.ddomlab.org.
## Structure
- Contains multiple packages: `Ddomlab-ELN-Automation-Common`, `Ddomlab-ELN-Automation-Backend` and `Ddomlab-ELN-Automation-Frontend`
- The frontend is an application that allows the user to interact with the ELN through a GUI. This extends some of the functions of the web GUI to work with a QR code scanner, although many advanced functions must be done through the web application.
- The backend is an set of scripts used to generate labels, RDKit images, and to pull information from PubChem and attach it to items.
- The common package contains functions used by both the frontend and backend.
