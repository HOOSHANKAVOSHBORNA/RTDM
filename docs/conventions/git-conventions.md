# Git Conventions

## Commit Template

commit template: `<type>(<scope>): <description>`.

|       type        |           function                    |                   example                 |
| :---------------- | -----------------------------         | :---------------------------------------- |
| `feat` | adding new feature. | `feat(components): add color box component.` |
| `fix` | fixing bug. | `fix: prevent from multiple assignment.` |
| `refactor` | now cleaner and more readable code. | `refactor(global): change userManager to singleton pattern.` |
| `test` | adding tests for features. | `test: add node field data change test.` |
| `config` | changing project configs like dependencies and build. | `config: increase cpu core used for running.` |
| `docs` | modifying documents. | `docs: add git conventions document.` |
| `improve` | improving codes. | `improve: change ux clicks.` |
| `perf` | improving performance. | `perf: remove additional variables.` |
| `style` | do conventions. | `style: rename variables.` |
| `chore` | miscellaneous commits. | `chore: modify .gitignore file.` |


# References

https://tenstars.co/blog/best-practices-on-writing-clean-commit-messages#:~:text=Our%20commit%20messages%20must%20have,more%20context%20to%20our%20changes.

https://www.conventionalcommits.org/en/v1.0.0/

https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13

https://hashnode.com/post/which-commit-message-convention-do-you-use-at-work-ck3e4jbdd00zyo4s1h7mc7e0g