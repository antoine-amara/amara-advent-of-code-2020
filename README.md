# Advent of Code 2020

a python dev environment to do advent of code.
it contains the solution for days of the advent of code too.
this repo works with a dev container for vscode with python 3.9, poetry, and some dev tools.

Each solution has a python script with the name pattern: `day-{N}.py`.

Resolve solutions:
`None`

## How to use

First, you need vscode and remote container extension installed:
- vscode: https://code.visualstudio.com/Download
- tuto on how to install and use remote container extension: https://code.visualstudio.com/docs/remote/containers

If you have vscode and remote container, open this workspace into the container, run a vscode terminal, and launch this command to install dependencies:
```shell
make dependencies
```

It will install all dependencies inside the remote container with poetry.

You are done, the environment is ready.

To see other available commands:

```shell
make help
```