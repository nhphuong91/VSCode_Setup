# VSCode_Setup
Collection of pre-init directories for various stuffs (programming languages, arduino,...) with VSCode config files

For more information, please refer to [VSCode official site](https://code.visualstudio.com/docs)

# Useful stuff/links
## Predefined variables
Source: [User guide](https://code.visualstudio.com/docs/editor/variables-reference)

The following predefined variables are supported:
* `${workspaceFolder}` - the path of the folder opened in VS Code
* `${workspaceFolderBasename}` - the name of the folder opened in VS Code without any slashes (/)
* `${file}` - the current opened file
* `${relativeFile}` - the current opened file relative to workspaceFolder
* `${relativeFileDirname}` - the current opened file's dirname relative to workspaceFolder
* `${fileBasename}` - the current opened file's basename
* `${fileBasenameNoExtension}` - the current opened file's basename with no file extension
* `${fileDirname}` - the current opened file's dirname
* `${fileExtname}` - the current opened file's extension
* `${cwd}` - the task runner's current working directory on startup
* `${lineNumber}` - the current selected line number in the active file
* `${selectedText}` - the current selected text in the active file
* `${execPath}` - the path to the running VS Code executable
* `${defaultBuildTask}` - the name of the default build task

## Debugging
Source: [User guide](https://code.visualstudio.com/docs/editor/debugging)

### [launch.json attributes](https://code.visualstudio.com/docs/editor/debugging#_launchjson-attributes)
Platform-specific properties: `"windows"`, `"linux"`, `"osx"`

## Tasks (linting, building, packaging, testing, deploying...)
Source: [User guide](https://code.visualstudio.com/docs/editor/tasks)

