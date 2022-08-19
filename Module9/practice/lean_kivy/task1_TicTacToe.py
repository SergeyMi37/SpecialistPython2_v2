from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (400, 500)


class MyApp(App):
    STEPS=["X","O","X","O","X","O","X","O","X"] # очередь ходов
    STOP=False # флаг останова игры
    def build(self):
        grid = GridLayout(padding=15, cols=3)
        # GridLayout: https://kivy.org/doc/stable/api-kivy.uix.gridlayout.html
        # Widgets: https://kivy.org/doc/stable/api-kivy.uix.html
        self.cell1 = Button(on_press=self.on_btn_click, font_size=40)
        self.cell2 = Button(on_press=self.on_btn_click, font_size=40)
        self.cell3 = Button(on_press=self.on_btn_click, font_size=40)
        self.cell4 = Button(on_press=self.on_btn_click, font_size=40)
        self.cell5 = Button(on_press=self.on_btn_click, font_size=40)
        self.cell6 = Button(on_press=self.on_btn_click, font_size=40)
        self.cell7 = Button(on_press=self.on_btn_click, font_size=40)
        self.cell8 = Button(on_press=self.on_btn_click, font_size=40)
        self.cell9 = Button(on_press=self.on_btn_click, font_size=40)
        self.lbl_status = Label(text="Ходит: X")
        grid.add_widget(self.cell1)
        grid.add_widget(self.cell2)
        grid.add_widget(self.cell3)
        grid.add_widget(self.cell4)
        grid.add_widget(self.cell5)
        grid.add_widget(self.cell6)
        grid.add_widget(self.cell7)
        grid.add_widget(self.cell8)
        grid.add_widget(self.cell9)
        grid.add_widget(self.lbl_status)
        return grid

    def on_btn_click(self,instance):
        if MyApp.STOP:
            self.lbl_status.text = 'Игра закончена'
            return
        if instance.text:
            return 
        instance.text = str(self.get_step())
        if instance.text=="X":
            step="O"
        else:
            step="X"
        winer=self.is_winer("O")
        if winer!="":
            self.lbl_status.text = f'Победил: {winer} '
            MyApp.STOP=True
        winer=self.is_winer("X")
        if winer!="":
            self.lbl_status.text = f'Победил: {winer} '
            MyApp.STOP=True
        else:
            self.lbl_status.text = f'Ходит: {step} '

    def get_step(self):
        return MyApp.STEPS.pop(0)

    def is_winer(self,who):
        if (self.cell1.text==who and self.cell2.text==who and self.cell3.text==who) or (self.cell4.text==who and self.cell5.text==who and self.cell6.text==who) or (self.cell7.text==who and self.cell8.text==who and self.cell9.text==who):
           return who
        if (self.cell1.text==who and self.cell4.text==who and self.cell7.text==who) or (self.cell2.text==who and self.cell5.text==who and self.cell8.text==who) or (self.cell3.text==who and self.cell6.text==who and self.cell9.text==who):
           return who
        if (self.cell1.text==who and self.cell5.text==who and self.cell9.text==who) or (self.cell3.text==who and self.cell5.text==who and self.cell6.text==who):
           return who
        return ""

        return MyApp.STEPS.pop(0)

# TODO: дана заготовка игры "Крестики-нолики". Закончите игру.
# TODO: Когда кто-то выстраивает вряд/по диагонали кри крестика или три нолика, в поле self.lbl_status, вывести: "победил Х".
# TODO: Когда выставлены все крестики или нолики(занято все поле), в поле self.lbl_status, вывести: "Конец игры. Ничья!"
if __name__ == "__main__":
    app = MyApp()
    app.run()
