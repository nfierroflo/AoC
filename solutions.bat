@echo off
echo Running all solutions...

for /d %%d in (day*) do (
    echo.
    echo Running %%d\solution.py...
    py "%%d\solution.py"
)

echo.
echo All solutions completed!
pause 