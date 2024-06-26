# EcoChallenge - EcoCode Rule Validator

The objective of this project is to provide a generic tool to facilitate the validation of new rules.

## Principles

For each potential rule, the rule validator will take as inputs :
  - a file containing the "good code smell"
  - a file containing the "bad code smell"
  - a file containing the test scenarios to be executed.

  For each scenario, the rule validator will instrumente it with monitoring tools (actually only one - vjoule) and will generate some results file.

  You can find some generated sample files in the folder **/samples**. 

  Based on those results file, a graphic summary is generated for each rule.

## How to

Pre-requisites : you must have a machine with python3 + vjoule installed

How to generate result files : ```python rule_validator.py```

How to render a result files : ```python graph_generator.py <function_name>.csv```
