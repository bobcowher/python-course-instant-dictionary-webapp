import justpy as jp
from webapp import layout
from webapp import page


class About(page.Page):

    path = "/about"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        page_layout = layout.DefaultLayout(a=wp, view="hHh lpR fFf")
        container = jp.QPageContainer(a=page_layout)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the About page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit,
         sed do eiusmod tempor incididunt ut labore et dolore 
         magna aliqua. Ut enim ad minim veniam, quis nostrud 
         exercitation ullamco laboris nisi ut aliquip ex ea 
         commodo consequat. Duis aute irure dolor in reprehenderit 
         in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui 
        officia deserunt mollit anim id est laborum.

        
        """, classes="text-lg")
        return wp
