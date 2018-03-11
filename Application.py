import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkmsgbox

class Application(ttk.Frame):
	_widgets = [
		["(", ")", "^", "÷"],
		["8", "9", "CLR", "×"],
		["5", "6", "7", "－"],
		["2", "3", "4", "＋"],
		["0", "1", ".", "＝"],
	]

	def __init__(self, master = None):
		super().__init__(master)
		master.title("計算ソフトウェア")
		master.geometry("300x300")
		self._create_style()
		self._create_widgets()

	def _create_style(self):
		style = ttk.Style()
	
		style.configure(
			"TLabel",
			font = ("メイリオ", 20),
			background = "black",
			foreground="white"
		)

		style.configure(
			"TButton",
			font = ("メイリオ", 20)
		)

	def _create_widgets(self):
		# 引延設定 -------------------------------------------
		self.master.columnconfigure(0, weight = 1)
		self.master.rowconfigure(0, weight = 1)

		for i in range(6):
			self.rowconfigure(i, weight = 1 if i != 0 else 0)
			for j in range(4):
				self.columnconfigure(j, weight = 1)
		# -----------------------------------------------------
		
		# UI配置品設定 ---------------------------------------
		self.grid(column = 0, row = 0, sticky = (tk.N, tk.S, tk.E, tk.W))

		self.disp = tk.StringVar()
		self.disp.set("0")

		lbl = ttk.Label(self,
			textvariable = self.disp
		).grid(
			column = 0,
			row = 0,
			columnspan = 4,
			sticky = (tk.N, tk.S, tk.E, tk.W)
		)

		for y, row in enumerate(self._widgets, 1):
			for x, txt in enumerate(row):
				btn = ttk.Button(self,
					text = txt
				)
				btn.grid(
					column = x,
					row = y,
					sticky = (tk.N, tk.S, tk.E, tk.W)
				)
				btn.bind("<ButtonRelease-1>", self._operate)
		# -----------------------------------------------------

	def _operate(self, event):
		inp = event.widget["text"]
		if inp == "CLR":
			self.disp.set("0")
		elif inp == "^":
			self.disp.set((self.disp.get() if self.disp.get() != "0" else "") + "**")
		elif inp == "÷":
			self.disp.set((self.disp.get() if self.disp.get() != "0" else "") + "/")
		elif inp == "×":
			self.disp.set((self.disp.get() if self.disp.get() != "0" else "") + "*")
		elif inp == "－":
			self.disp.set((self.disp.get() if self.disp.get() != "0" else "") + "-")
		elif inp == "＋":
			self.disp.set((self.disp.get() if self.disp.get() != "0" else "") + "+")
		elif inp == "＝":
			try:
				self.disp.set(eval(self.disp.get()))
			except SyntaxError:
				tkmsgbox.showerror("通知", "數式の構文に錯誤有り")
		# 函數等への對應
		else:
			self.disp.set((self.disp.get() if self.disp.get() != "0" else "") + event.widget["text"])
