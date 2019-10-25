# Contribution guidelines

Before sending a Pull Request, please make sure that you're assigned the task on a GitHub issue.

- If a relevant issue already exists, discuss on the issue and get it assigned to yourself on GitHub.
- If no relevant issue exists, open a new issue and get it assigned to yourself on GitHub.

Please proceed with a Pull Request only after you're assigned. It'd be bad time if your Pull Request and your hardwork
isn't accepted just because it isn't ideologically compatible.

## Developing the Project

### Install

```sh
git clone https://github.com/iamjohnnym/python-globalsign
cd python-globalsign
```

### Create a PR with your branch

_**Make your changes in a different git branch (eg, `enhancement/new-feature`).**_

- enhancing the service
- fixing a bug
- adding additional tests

### Test

```sh
make test
```

### Validate syntax and security

```sh
make flake
make bandit
```

### Update Documents

### Update Makefile and CI tools
