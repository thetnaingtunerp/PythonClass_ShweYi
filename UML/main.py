# pip install plantuml six

from plantuml import PlantUML

# Public PlantUML server
server = PlantUML(url="http://www.plantuml.com/plantuml/img/")

# Generate UML diagram from file
server.processes_file("stock.puml")
