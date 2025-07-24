**📝 QuizDesk**

_**A standalone Python/Tkinter‑powered desktop quiz application, packaged into a Windows .exe for zero‑install ease.**_

---

**🚀 Overview**  
QuizDesk brings your quiz questions to life in a simple, intuitive GUI. Educators and learners alike can load question sets, take timed quizzes, and see instant scoring—all without touching a web browser.

---

**✨ Key Features**

- **Zero‑install .exe**  
  Download and run the Windows executable—no Python required.  
- **Dynamic Question Loading**  
  Point QuizDesk at any JSON or CSV file containing your quiz data and start immediately.  
- **Timed Quiz Sessions**  
  A global countdown timer keeps each quiz challenging and engaging.  
- **Real‑Time Scoring & Feedback**  
  Scores update live; see per‑question correctness and overall performance.  
- **Customizable Themes & Icons**  
  Built on ttkbootstrap—you can swap themes or replace the `olaneye.ico` file in the project root.

---

**🛠️ Technologies**

| **Layer**            | **Technologies**              |
|----------------------|-------------------------------|
| **UI & Logic**       | Python, Tkinter, ttkbootstrap |
| **Packaging**        | PyInstaller                   |
| **Version Control**  | Git                           |
| **Data Files**       | JSON, CSV                     |

---

**🔧 Installation & Setup**

**✅ Prerequisites**  
- **Windows 10+ (64‑bit)** for the `.exe`  
- **Python 3.8+ & pip** (only if running from source)

**📌 Setup Instructions (from source)**  
```bash
git clone https://github.com/Boboahmedino/QuizDesk.git
cd QuizDesk
pip install -r requirements.txt
python app.py
````

---

**📥 Downloads**
▶️ [Download the latest Windows .exe](https://github.com/Boboahmedino/QuizDesk/releases/latest)
*No Python install required—just double‑click and go!*

---

**📂 Project Structure**

```plaintext
QuizDesk/
├── app.py             ← main entry point
├── data.py            ← quiz‑loading logic (imports quiz_data)
├── olaneye.ico        ← application icon for packaging
└── README.md          ← this documentation
```

---

**🎮 Usage**

1. **Launch**

   * Double‑click `QuizDesk.exe` (Windows)
   * or run `python app.py` (from source)

2. **Load a Quiz**
   Click **Load Quiz**, then select a `.json` or `.csv` file.

3. **Set Time Limit**
   Enter the desired total quiz time in seconds (default: 90 sec).

4. **Answer & Navigate**

   * Read each question, select an option, then **Next**.
   * Click **Submit** to finish early.

5. **View Your Score**
   A popup displays your final score and feedback.

---

**🔮 Future Enhancements**

* **Leaderboard & Export**
  Save and export score histories to CSV.
* **Built‑in Quiz Editor**
  Create and modify quizzes without external files.
* **Theme Picker**
  Let users switch between ttkbootstrap themes at runtime.

---

**👤 Author**
**Olaneye Ahmed Oladapo**
🔗 [GitHub](https://github.com/Boboahmedino) | 🔗 [LinkedIn](https://www.linkedin.com/in/olaneye/)

```
