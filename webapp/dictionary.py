import justpy as jp
from definition import Definition
from webapp import layout
from webapp import page

class Dictionary(page.Page):
    path = "/dictionary"

    @classmethod
    def serve(cls):
        wp = jp.QuasarPage(tailwind=True)

        page_layout = layout.DefaultLayout(a=wp, view="hHh lpR fFf")
        container = jp.QPageContainer(a=page_layout)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Instant English dictionary", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the definition of any English word instantly as you type",
               classes="text-lg")

        input_div = jp.Div(a=div, classes="grid grid-cols-2")
        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40 bg-blue-400")

        input_box = jp.Input(a=input_div, placeholder="Type in a word...", outputdiv = output_div,
                 classes="m-2 bg-grey-100 border-2 border-gray-200 rounded "
                         "w-64 focus:outline-none focus:bg-white focus:border-purple-500 "
                         "py-2 px-4 ")
        input_box.on('input', cls.get_definition)
        # jp.Button(a=input_div, text="Get Definition", classes="border-2 text-gray-500", click=cls.get_definition, outputdiv=output_div, inputword=input_word)

        return wp


    @staticmethod
    def get_definition(widget, msg):
        print(f"Getting definition for {widget.value}")
        definition_instance = Definition(term=widget.value)
        definition = definition_instance.get()
        if (len(definition) < 1 and len(widget.value) < 4) :
            definition = "Not enough information.."
        elif(len(definition) < 1 and len(widget.value) > 4):
            definition = "Try a less specific search..."

        widget.outputdiv.text = definition