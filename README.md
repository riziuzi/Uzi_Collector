<div align="center">
  <h1>🚀 Uzi Collector</h1>
  <p>A Python script for collecting and storing data in a specified directory.</p>
</div>

<p align="center">
<a href="/LICENSE.md"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg"></a>
<a href="https://www.python.org/downloads/release/python-3110/"><img src="https://img.shields.io/badge/Python-3.11%2B-green.svg" /></a>
</p>

## 🎬 Getting Started

To get started, you need to configure two files: `Uzi_configuration.py` and `rizi_spawner.py`.

### 🔧 Uzi_configuration.py

This file stores two variables:

- `root`: 🗂️ This stores the location of the directory where we want to store the data. This directory doesn't have to be the same as the directory where you forked this repo. You can also set the location as a local Google Drive to use it as your cloud server.

- `control`: 🕹️ This is the current location of the repo, from where you are launching this program.

To use the script, set the values of these variables in the `Uzi_configuration.py` file.

### 🚀 rizi_spawner.py

This script creates a file structure in your specified `root` location and collects the data. To run the script, simply execute `rizi_spawner.py`.

## 📖 Further Explanation

More information about the script and its functionality will be added soon. Stay tuned! 🤞

## ⏰ Automating the Task

If you want to automate the task, you can use the Windows task scheduler. Here's how to set it up:

1. Open the task scheduler.
2. Create a new task.
3. Under the Actions section, set Program/script to `py`.
4. Under the Add arguments (optional) section, add `-u "<location of your repo, or simply, control>\rizi_spawner.py"`.
5. Set the desired schedule and save the task.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 📜

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for more information. 💪

<div align="center">
  <p>👀 Happy coding! 👨‍💻👩‍💻</p>
</div>
