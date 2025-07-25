# 🎥 Video Recorder using Python

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)](https://www.python.org/)
[![moviepy](https://img.shields.io/badge/moviepy-1.0.3-blue)](https://zulko.github.io/moviepy/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Judethedude007/video-recorder-using-python/pulls)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

---

Welcome to **Video Recorder using Python**!  
This project leverages Python libraries such as `moviepy` and others to create a screen recorder with audio support.  
> **Note:** The latest version of `moviepy` lacks the `editor` module, so an older version is used for full functionality.

---

## 🚀 Features

- Record your screen with audio
- Save recordings in popular video formats
- Lightweight & easy to use
- Extensible for custom use-cases

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Judethedude007/video-recorder-using-python.git
   cd video-recorder-using-python
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   # OR install manually
   pip install moviepy==1.0.3 sounddevice numpy
   ```

   > ⚠️ **Important:** Make sure you install a compatible version of `moviepy` (e.g., 1.0.3) that includes the `editor` module.

---

## 🛠️ Usage

```bash
python recorder.py
```

- When prompted, select the area to record or use full screen.
- The script records both video and system audio.
- Press the designated key (e.g., `q`) to stop recording.

---

## 🧠 How It Works

1. **Screen Capture:**  
   Uses `moviepy` to capture the screen frames.

2. **Audio Recording:**  
   Captures audio input/output using `sounddevice`.

3. **Synchronization:**  
   Merges the video and audio streams into a single output file.

4. **Saving:**  
   Exports the final video in your chosen format.

---

## 📁 Project Structure

```
video-recorder-using-python/
│
├── recorder.py
├── requirements.txt
├── README.md
└── ...
```

---

## 🙋‍♂️ Contributing

1. Fork this repo
2. Create your branch: `git checkout -b my-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin my-feature`
5. Create a new Pull Request

---

## 📢 License

This project is licensed under the MIT License.

---

## 💡 About

Created and maintained by [Judethedude007](https://github.com/Judethedude007).  
Feel free to star ⭐ the repo if you find it useful!
