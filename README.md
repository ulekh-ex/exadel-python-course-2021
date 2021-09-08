# exadel-python-course-2021
Exadel Python Course 2021 for employees.

[TASKS](https://docs.google.com/document/d/1EgIJw4_dZehaOURjYDdtZI09jMlQe2AGmfneZUgxfDM/edit?usp=sharing).

## How to get started
1. Install Python
    1. Download & install the latest [Python](https://www.python.org/downloads/) version.
    2. Make sure that Python is available through the command line, check its location (`where python`  - Windows, `which python` - Linux). You may need to update your `PATH` variable.
    3. Try to run Python REPL via command line:
        ```bash
        python
        ```
        You should see output like:
        ```bash
        Python 3.8.5 (default, May 27 2021, 13:30:53) 
        [GCC 9.3.0] on linux
        Type "help", "copyright", "credits" or "license" for more information.
        >>> 
        ```
2. Install IDE of your choice:
    * [PyCharm Community](http://www.jetbrains.com/pycharm/download) - the Python IDE from JetBrains
    * [VSCode Python extension](https://code.visualstudio.com/docs/languages/python)
    * [Python plugin for IDEA](https://www.jetbrains.com/help/idea/plugin-overview.html)
3. Install [git](https://git-scm.com/downloads) (if not installed yet)
4. Sign up to [GitHub](https://github.com/) (if you do not have account yet)
5. Fork([?](https://docs.github.com/en/get-started/quickstart/fork-a-repo)) this repository. If you wish, create your own private repo instead, but follow the structure defined here.
6. Add your mentor as a [contributor](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-user-account/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository) to your repository so that he/she can review your PRs.
7. Clone your forked repository & run `hello_world.py` 
    ```bash
    git clone https://github.com/{your-github-nick}/exadel-python-course-2021.git
    cd exadel-python-course-2021
    python tasks/task00/hello_world.py
    ```
8. In the end you should see `Hello, World!` line in console. 
## Repository structure
Place your solutions inside `tasks` folder, create a separate folder for every task. Treat every task folder as a separate project.

Example:
```
tasks/
    task00/
        hello_world.py
    task99/
        super_app.py
        requirements.txt
```

## Solution & review workflow
* Create a separate branch for each task like:
    ```bash
    git checkout -b taskXX
    ```
* Create a separate folder for your task:
    ```
    tasks/taskXX
    ```
* Solve it :)
* Commit & push your solution
* Once ready with your solution:
    * Open a Pull Request (PR) to `main` from task branch
    * Add your mentors as PR reviewers
    * Resolve PR comments
    * Once PR is approved, merge it to `main` branch
