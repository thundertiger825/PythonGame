import cx_Freeze
import os
os.environ['TCL_LIBRARY'] = "C:\\Program Files (x86)\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Program Files (x86)\\Python36-32\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("snake5.py")]

cx_Freeze.setup(name="Slither",
                options={"build_exe":{"packages":["pygame"],"include_files":["Untitled8.png","3e3cb45360c1e445c8ab6fff83939daa.jpg","Untitled9.png","Untitled19.png","Untitled99.png","Untitled56.png","Untitled57.png","Untitled98.png","Untitled1.2.png","Spiral.png","d20bb6f128c818ce4e6a2508137ed7b9.jpg","cute-snake-cartoon-illustration-55471879.jpg","cartoon-snake-frame-illustration-54299249.jpg","animals-snakes-medical_research-making_money-snake_bite-bitten_by_a_snake-cgan1811_low.jpg","snakemusik1.mid","mariobrosd_9r81556y.mp3"]}},
                description ="game by harman",
                executables = executables,
version='1.0.0'


                )

