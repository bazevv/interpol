import nox

@nox.session(python=["3.9"])
def tests(session):
    session.install("pytest", "pytest-cov", "numpy", "scipy")
    session.install(".")  # устанавливает твой пакет (interpol)
    session.run("pytest", "--cov=interpol", "--cov-report=term-missing", "tests")

@nox.session
def lint(session):
    session.install("flake8")
    session.run("flake8", "interpol", "tests")

@nox.session
def coverage(session):
    session.install("coverage", "pytest")
    session.install(".")
    session.run("coverage", "run", "-m", "pytest", "tests")
    session.run("coverage", "report")
    session.run("coverage", "html")