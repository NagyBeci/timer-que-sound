# 🕒 Customizable Timer

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15%2B-green.svg)](https://pypi.org/project/PyQt5/)

## 📝 Overview

A customizable timer application built with PyQt5, featuring a timer queue, circular progress bar, and custom notification sounds.

## ✨ Features

* **Multiple Timers:** Add multiple timers to a queue and run them sequentially
* **Circular Progress Bar:** Visual representation of the timer countdown
* **Custom Time Inputs:** Set hours, minutes, and seconds for each timer
* **Notification Sounds:** Upload and play custom audio files when a timer completes
* **Timer Management:** Start, pause, reset, and delete timers from the queue

## 🎥 Demo

*Screenshots or a GIF demonstrating the application can be placed here.*

## 🚀 Installation

### Prerequisites

* Python 3.6 or higher
* PyQt5

### Clone the Repository

```bash
git clone https://github.com/NagyBeci/timer-que-sound.git
cd timer-que-sound
```

### Install Dependencies

```bash
pip install PyQt5
```

### Run the Application

```bash
python custom_timer.py
```

## 📖 Usage

1. **Set Timer:**
   * Input the desired hours, minutes, and seconds
   * Click **"Add to Queue"** to add the timer to the queue list

2. **Manage Timers:**
   * **Start:** Begins the countdown of the current timer
   * **Pause:** Pauses the ongoing timer
   * **Reset:** Resets the current timer to its initial state
   * **Delete Selected Queue:** Removes selected timers from the queue

3. **Notification Sounds:**
   * Click **"Upload Audio Files"** to select custom audio files (`.wav`, `.mp3`, `.ogg`, `.mp4`)
   * The application will play a random sound from the uploaded files when a timer ends
   * **Stop Audio:** Click to stop the currently playing notification sound

## 🔊 Audio Files

The application comes with 5 default sound files:
* `audio1.mp3`
* `audio2.mp3`
* `audio3.mp3`
* `audio4.mp3`
* `audio5.mp3`

> *Feel free to replace these with your own audio files or upload additional ones through the application interface.*

## 📁 Project Structure

```bash
├── custom_timer.py    # Main application script
├── audio1.mp3        # Default audio files
├── audio2.mp3
├── audio3.mp3
├── audio4.mp3
├── audio5.mp3
└── README.md         # Project documentation
```

## 📚 Dependencies

* **Python 3.6+**
* **PyQt5:** GUI framework used for building the application interface

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request

## 📄 License

This project is licensed under the **MIT License**.

## 📫 Contact

For any questions or suggestions, feel free to open an issue or contact the repository owner.

---

*Enjoy using the Customizable Timer application!* ✨
