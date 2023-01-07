import flet as ft

def main(page:ft.Page):
    page.title = 'PassKeepr'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.bgcolor = 'white'

    page.add(
        ft.TextField(bgcolor= 'grey', color= 'black', width= 500, text_align= 'center')
    )

    page.update()

if __name__ == '__main__':
    ft.app(target = main)