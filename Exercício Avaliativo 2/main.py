from database import Database
from TeacherCRUD import TeacherCRUD
from TeacherCLI import teacherCLI

db = Database("bolt://52.3.235.203:7687","neo4j","terminations-runaway-dollar")

teacher = TeacherCRUD(database=db)

teacher.create_teacher('Chris Lima',1956,'189.052.396-66')
teacher.read_teacher('Chris Lima')
teacher.update_teacher('Chris Lima',"162.052.777-77")

cli = teacherCLI(teacher)
cli.run()