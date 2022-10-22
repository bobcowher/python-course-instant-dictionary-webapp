import justpy as jp

@jp.SetRoute("/home")
def home():
    wp = jp.QuasarPage(tailwind=True)
    #Styling is in tailwindcss
    div = jp.Div(a=wp, classes="bg-grey-200 h-screen")

    #Start of div1 -----------------------------
    div1 = jp.Div(a=div, classes="grid grid-cols-3 gap-4 p-4 border border-black")
    in_1 = jp.Input(a=div1, placeholder="Enter first value",
             classes="form-input")
    in_2 = jp.Input(a=div1, placeholder="Enter second value",
             classes="form-input")
    d_output = jp.Div(a=div1, text="Result goes here...", classes="text-gray-600")


    #Start of div2 -----------------------------
    div2 = jp.Div(a=div, classes="grid grid-cols-2 gap-4")
    jp.QBtn(a=div2, text="Calculate", click=sum_up, in1=in_1, in2=in_2,
              d = d_output,
              classes="border border-blue-500 m-2 p-2 rounded"
              " text-blue-600 hover:bg-red-500 hover:text-white")
    jp.Div(a=div2, text="I am a cool interactive div!", classes = "hover:bg-red-500",
           mouseenter=mouse_enter, mouseleave=mouse_leave)

    return wp

@jp.SetRoute("/about")
def about():
    pass

def sum_up(widget, msg):
    sum = float(widget.in1.value) + float(widget.in2.value)
    widget.d.text = sum

def mouse_enter(widget, msg):
    widget.text = "A mouse entered the house"

def mouse_leave(widget, msg):
    widget.text = "A mouse left the house!"

@jp.SetRoute("/about")
def home():
    wp = jp.WebPage()
    jp.Div(a=wp, text="Welcome to the about page!")

jp.Route("/", home)
jp.justpy()