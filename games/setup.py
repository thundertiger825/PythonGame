import cx_Freeze

executables = [cx_Freeze.Executable("game1.py")]

cx_Freeze.setup(name="Slither",options={"build_exe":{"packages":["pygame"],"include_files":["apple.png","snakeheader.png"]}},
                description ="snake by watson",
                executables = executables


                )

