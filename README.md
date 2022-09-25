# ExploringSymbolicExecutionTools

The two tools I will be testing is `Manticore` for Solidity Smart Contracts and `CrossHair` for python code.
### Setup 
`python3 -m venv env`

`source env/bin/activate`

`pip install -r requirements.txt`
### Running Manticore (Solidity)

` manticore ManticoreExamples/Reentrancy.sol --contract Reentrance `

` manticore-verifier ManticoreExamples/Reentrancy.sol --contract Reentrance `

` manticore-verifier ManticoreExamples/property.sol --contract TestToken `

### Running CrossHair (Python)

`crosshair check CrossHairExample/Test.py` 

`crosshair check --analysis_kind=asserts CrossHairExample/Test2.py`
