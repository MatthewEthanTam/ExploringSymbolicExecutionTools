# ExploringSymbolicExecutionTools
The two tools I will be testing is `Manticore` for Solidity Smart Contracts and `CrossHair` for python code.
### Setup 
`python3 -m venv env` 

`source env/bin/activate`

`pip install -r requirements.txt`
### Running Manticore (Solidity)
` manticore-verifier ManticoreExamples/property.sol --contract TestToken  `
` manticore ManticoreExamples/Test.sol --contract Ownership `

### Running CrossHair (Python)
` crosshair check CrossHairExample/Test.py  ` 
