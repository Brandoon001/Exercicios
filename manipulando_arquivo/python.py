from pathlib import Path
import os
 
for nome in ['arquivo1.txt', 'arquivo2.txt', 'arquivo3.txt']:
    print(Path('primeira_pasta/segunda_pasta', nome))
 
for nome in ['arquivo1.txt', 'arquivo2.txt', 'arquivo3.txt']:
    print(Path('primeira_pasta/segunda_pasta') / nome)

homePath = Path('C:/Users/Aluno')
pasta = Path('spam')
subPasta = Path('pasta')
print(homePath / pasta / subPasta)

print(Path.home())

os.chdir(Path.home())
print(Path.cwd().is_absolute())
print(Path('primeira_pasta').is_absolute())
print(Path.cwd() / Path('primeira_pasta'))

p = Path('C:/Users/Aluno/Documents/Projetos/Exercicios/jocile/Exercicios/testando_caminho/python.py')

print(f"Drive: {p.anchor}")
print(f"Parent: {p.parent}")
print(f"Name: {p.name}")
print(f"Stem: {p.stem}")
print(f"Suffix: {p.suffix}")
print(f"Drive: {p.drive}")

print(f"pasta superior: {p.parents[0]}")
print(f"pasta anterior: {p.parents[1]}")

print(list(Path.cwd().glob('*')))
print(list(Path.cwd().glob('*.py')))

caminho = Path('C:/exemplo/arquivo.txt')
 
print(caminho.exists())
print(caminho.is_dir())
print(caminho.is_file())