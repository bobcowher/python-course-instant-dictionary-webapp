import justpy as jp
from webapp import layout
from webapp import page

class Home(page.Page):
    path = "/home"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        page_layout = layout.DefaultLayout(a=wp, view="hHh lpR fFf")
        container = jp.QPageContainer(a=page_layout)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")

        jp.Div(a=div, text="This is the home page!", classes="text-4xl m-2")

        jp.Div(a=div, text="page content here", classes="text-lg")

        return wp


