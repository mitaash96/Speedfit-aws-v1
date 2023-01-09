import flet as ft
import config as conf

class split_control(ft.UserControl):
    def __init__(self, val, page):
        super().__init__()
        self.val = val
        self.page = page
    
    def render_split(self, e):
        self.page.clean()
        self.page.add(ft.Container(content= ft.Text(value= self.val),
            alignment= ft.alignment.center, bgcolor= 'blue'))

    def build(self):
        return ft.Container(content = ft.Text(value = f'{self.val}'), on_click= self.render_split, bgcolor= 'red', expand= True,
            width = 500, height= 500)

def main(page: ft.Page):
   
    page.title = 'Select Split'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(ft.GridView(controls= [split_control(_, page) for _ in conf.split.keys()],
        expand= True, horizontal= True, col= 3, runs_count=2, child_aspect_ratio=1.0, run_spacing= 0, padding= 0))
    
    page.padding = 10
    
    page.update()

ft.app(target=main)