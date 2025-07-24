import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style, ttk
from data import quiz_data

class QuizApp:
    def __init__(self):
        # Window setup
        self.window = tk.Tk()
        self.window.title('Olaneye Quiz App')
        self.window.geometry('540x240')
        self.window.minsize(400, 200)
        self._center_window(800, 500)

        # Style/theme
        style = Style(theme='superhero')
        style.configure('Header.TLabel', font=('Segoe UI', 24, 'bold'))
        style.configure('Question.TLabel', font=('Segoe UI', 18), wraplength=800)
        style.configure('Option.TRadiobutton', font=('Segoe UI', 16), padding=10)
        style.configure('Nav.TButton', font=('Segoe UI', 14), padding=8)
        style.configure('Score.TLabel', font=('Segoe UI', 16, 'bold'), foreground='#FFD700')
        style.configure('Timer.TLabel', font=('Segoe UI', 14, 'bold'), foreground='#FF5566')

        # Menu Bar
        menu = tk.Menu(self.window)
        help_menu = tk.Menu(menu, tearoff=0)
        help_menu.add_command(label='About', command=self._show_about)
        menu.add_cascade(label='Help', menu=help_menu)
        self.window.config(menu=menu)

        # Main Frame
        self.main = ttk.Frame(self.window, padding=20)
        self.main.pack(fill='both', expand=True)
        self.main.columnconfigure(1, weight=1)
        self.main.rowconfigure(1, weight=1)

        # Header: Title, Score, Timer
        header = ttk.Frame(self.main)
        header.grid(row=0, column=0, columnspan=2, sticky='ew')
        header.columnconfigure(0, weight=1)
        ttk.Label(header, text=f"Quiz App", style='Header.TLabel').grid(row=0, column=0, sticky='w')
        self.score_lbl = ttk.Label(header, text='Score: 0/0', style='Score.TLabel')
        self.score_lbl.grid(row=0, column=1, sticky='e', padx=10)
        self.timer_lbl = ttk.Label(header, text='Time: 00:00', style='Timer.TLabel')
        self.timer_lbl.grid(row=0, column=2, sticky='e')

        # Progress Bar
        self.progress = ttk.Progressbar(self.main, orient='horizontal', length=400, mode='determinate')
        self.progress.grid(row=1, column=0, columnspan=2, pady=15)

        # Question and options
        content = ttk.Frame(self.main)
        content.grid(row=2, column=0, columnspan=2)
        content.columnconfigure(0, weight=1)
        self.content = content

        self.question_lbl = ttk.Label(content, text='', style='Question.TLabel')
        self.question_lbl.grid(row=0, column=0, sticky='w')

        self.answer_var = tk.StringVar()
        self.options = []
        for i in range(4):
            rb = ttk.Radiobutton(content, text='', variable=self.answer_var,
                                 style='Option.TRadiobutton', value=str(i), command=self._on_select)
            rb.grid(row=i+1, column=0, sticky='w', pady=5)
            self.options.append(rb)

        # Navigation Buttons
        nav = ttk.Frame(self.main)
        nav.grid(row=3, column=0, columnspan=2, pady=20)
        self.next_btn = ttk.Button(nav, text='Next', style='Nav.TButton', command=self.next_question, state='disabled')
        self.next_btn.grid(row=0, column=1, padx=10)
        ttk.Button(nav, text='Submit', style='Nav.TButton', command=self.submit).grid(row=0, column=2)

        # State variables
        self.current_question = 0
        self.score = 0
        self.total = len(quiz_data)
        self.responses = []  # to store (question, user answer, correct answer)
        self._update_score()
        self._update_progress()

        # Timer for entire quiz
        self.time_left = 90
        self.timer_running = False

        # Start
        self.show_question()
        self._start_timer()
        self.window.mainloop()

    def _center_window(self, w, h):
        sw, sh = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        x, y = (sw-w)//2, (sh-h)//2
        self.window.geometry(f'{w}x{h}+{x}+{y}')

    def _show_about(self):
        messagebox.showinfo('About', 'Quiz App\nDeveloper: OLANEYE AHMED OLADAPO\nv1.0')

    def _update_score(self):
        self.score_lbl.config(text=f'Score: {self.score}/{self.total}')

    def _update_progress(self):
        self.progress['maximum'] = self.total
        self.progress['value'] = self.current_question

    def show_question(self):
        # reset UI
        q = quiz_data[self.current_question]
        self.question_lbl.config(text=q['question'])
        self.answer_var.set(None)
        for rb, opt in zip(self.options, q['options']):
            rb.config(text=opt, state='normal')
        self.next_btn.config(state='disabled')

    def _on_select(self):
        self.next_btn.config(state='normal')

    def check_answer(self):
        q = quiz_data[self.current_question]
        idx = int(self.answer_var.get())
        user_choice = q['options'][idx]
        correct_answer = q['answer']
        # record
        self.responses.append((q['question'], user_choice, correct_answer))
        # score
        if user_choice == correct_answer:
            self.score += 1
        # disable
        for rb in self.options:
            rb.config(state='disabled')
        self._update_score()

    def next_question(self):
        # evaluate
        self.check_answer()
        self.current_question += 1
        self._update_progress()
        if self.current_question < self.total:
            # blink/flicker: clear then show next after 300ms
            self.content.grid_remove()
            self.window.after(300, lambda: self.content.grid())
            self.window.after(600, self.show_question)
        else:
            # finish quiz without review
            self._finish_quiz('Completed!', 'Quiz Completed')
            self.next_btn.config(state='disabled')

            # self._finish_quiz('Quiz Complete', f'You completed the quiz!\nScore: {self.score}/{self.total}')
            # self.window.destroy()

    def _start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self._countdown()

    def _countdown(self):
        mins, secs = divmod(self.time_left, 60)
        self.timer_lbl.config(text=f'Time: {mins:02d}:{secs:02d}')
        if self.time_left > 0:
            self.time_left -= 1
            self.window.after(1000, self._countdown)
        else:
            self._finish_quiz('Time Up!', f'Congratulations!\nFinal Score: {self.score}/{self.total}')
            self.window.destroy()

    def _finish_quiz(self, title, message):
        messagebox.showinfo(title, message)

    def submit(self):
        if messagebox.askyesno('Submit!', 'Submit test?'):
            self._finish_quiz('Quiz Completed!', f'Congratulations!\nFinal Score: {self.score}/{self.total}')
            self.window.destroy()
        else:
            None

if __name__ == '__main__':
    QuizApp()
