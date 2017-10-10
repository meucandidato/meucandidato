# Meu Candidato

Sistema voltado para centralizar informações do seu candidato, e tornar acessível para qualquer eleitor sobre sua vida, carreira e qualquer notícia relacionado a ele e seu partido.

[![Join the chat at https://gitter.im/meucandidato/projeto](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/dotnet/coreclr?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Documentation Status](https://readthedocs.org/projects/meucandidato/badge/?version=latest)](http://meucandidato.readthedocs.io/en/latest/?badge=latest)
[![Tracis-CI build status](https://travis-ci.org/gilsondev/meucandidato.svg?branch=master)](https://travis-ci.org/gilsondev/meucandidato)

[Screenshot]

## Objetivo

Essa idéia surgiu quando este idealizador (Gilson Filho) procurava informações de candidatos na última eleição. Como as informações estão em vários
lugares, como também dados do TSE não são tão acessíveis como deveria, pensei em uma forma de criar um aplicação web que possa pesquisar
pelo nome do candidato do seu interesse, e capturar tudo o que é possível dele em:

- Portais de notícias
- Dados do TSE como: credenciamento eleitoral, doações de campanha e seus gastos
- Dados processuais de tribunais do estado do candidato
- E outras informações acessíveis pela Internet

Dessa forma, teriamos nas nossas mãos uma linha do tempo de tudo que ele fez ou não fez, propôs, os partidos que passou e sua associação
a outros candidatos e políticos.

## Instalação

Faça o checkout do projeto

```shell
git clone https://github.com/meucandidato/meucandidato
cd meucandidato
```

Prepare o ambiente com virtualenv e instale

```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ make install
```

Inicie o servidor

```shell
$ mcand runserver
```

## Ambiente para Desenvolvimento

Siga os passos acima, mas ao preparar o ambiente para instalação siga o procedimento abaixo:

```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ make develop
```

Para execução de testes faça:

```shell
$ make test
```

Se executar `make help` irá acessar os comandos disponíveis:

```shell
$ make help

clean:  remove Python file artifacts
pep8:  check style with flake8
test: pep8  run tests quickly with the default Python
install: clean test  install the package to the active Python's site-packages
develop:  Install the package with develop mode
help:   Show this help.
```

Além disso o projeto possui o comando `mcand` que faz o papel do `manage.py` em projetos Django. Digite `mcand` no terminal e verá isso:

```shell
$ mcand

Usage: mcand [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  runserver  Inicia o servidor local em modo debug
  shell      Abre um shell com o objeto app no contexto
```

## Como contribuir

Veja mais no arquivo `CONTRIBUTING.md`, as formas de ajudar com o projeto, e o `AUTHORS.md` para saber quem esta a frente e que pode te auxiliar.