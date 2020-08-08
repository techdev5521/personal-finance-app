# Dev Environment Setup Guice

## Prerequisites
- [VS Code](https://code.visualstudio.com/download)
- [NodeJS](https://nodejs.org/en/) >= v14.2.0
- npm >= v6.14.4
- npx >= v6.14.4
- Python 3

## Setup
**Note:** Personal Finanace App uses npm and  create-react-app to manage itself. You can learn more about npm [here](https://nodesource.com/blog/an-absolute-beginners-guide-to-using-npm/) and create-react-app [here](https://create-react-app.dev/docs/getting-started/).


### Step 1: Create and enter a project directory
```bash
mkdir project-dir && cd project-dir
```

### Step 2: Close the Reposistory
```bash
git clone https://github.com/techdev5521/personal-finance-app.git
```

### Step 3: Install npm Packages
```bash
npm install
```

#### Using npm
There are three built in npm scripts that come from create-react-app:

1. `npm run start`: This will start a local development server on [localhost:3000](http://localhost:3000) and launch your default browser at that address. As you save changes in /public and/or /src you'll see your changes in the browser.

1. `npm run build`: This will build a static version of the site in /build ready to be placed in the document root of any web server.

1. `npm run test`: This will run any tests (using the [Jest](https://jestjs.io/) tester). There are currently no defined tests.

1. `npm run eject`: <span style="background-color: #fff394">**THIS IS NON-REVERSABLE**</span>: This will abstract all of the build environment settings and make them available to you. See the [create-reacte-app docs on ejecting](https://create-react-app.dev/docs/available-scripts#npm-run-eject) for more information.

### Step 4: Setup Python for API
Go to the API directory
```bash
cd api/
```

Activate the Python virtual environment
```bash
source venv/bin/activate
```

Install Python requiements
```bash
pip install -r requirements.txt
```

### Step 5: Configure VS Code

#### Installing Plugins
- [ES Lint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) for JavaScript linting
- [Babel JavaScript](https://marketplace.visualstudio.com/items?itemName=mgmcdermott.vscode-language-babel) for JavaScript and JSX syntac highlighting and error checking
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) for working with Python virtual environments and debugging
- [Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) for generating Google style docstrings according to section 3.8 of [Google's Python style guide](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings)

Optionally:
- [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) for directly editing files on remote machine
- [Markdown Preview GitHub Styling](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-preview-github-styles) for previewing Markdown as it will appear on GitHub

#### Configuring Environemnt
- Python will need some workspace and debugger configuration to work. See [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial) for more info.
- Remote - SSH will requires hosts to be added to your SSH config file. See [this guide](https://linuxize.com/post/using-the-ssh-config-file/) for more info.
- ES Lint, Babel JavaScript and Markdown Preview GitHub Styling will work without further configuration