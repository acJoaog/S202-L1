from database import Database
from writeAJson import writeAJson
from DiagramaUML import *
from MotoristaDAO import MotoristaDAO
from MotoristaCLI import motoristaCLI

db = Database(database="Atlas-Cluster", collection="Motoristas")
motorista = MotoristaDAO(database=db)

cli = motoristaCLI(motorista)
cli.run()