excludes = \*~ \*.pyc .cache/\* test_\* __pycache__/\*

e?=dev
SERVICE=python_globalsign

export ${SERVICE}
export ${e}

.PHONY: clean
clean:
	find . -type f -name '*.pyc' -delete

.PHONY: bandit
bandit:
# Bandit checks for known security flaws, vulnerabilies, general bad
# habits and returns non-zero if threshold is met.  -ll means were looking
# for a severity of medium and confidence of low.
# ['undefined', 'low', 'medium', 'high']
	poetry run bandit -ll -i -x ${SERVICE}/tests/ -r ${SERVICE}/ --format custom \
	--msg-template \
	"{abspath}:{line}: {test_id}[bandit]: {severity}: {msg}"

.PHONY: flake
flake:
	poetry run flake8 service

.PHONY: test
test:
	poetry run pytest
