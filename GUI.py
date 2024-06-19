#import data_analysis as da
import panel as pn
import sympy as sp
from sympy.parsing.latex import parse_latex        #Converting Latex input to Sympy


#Widget Creation
# -----------------------------------------------------------

#  Mode Selector (horizontal buttons)
radio_group = pn.widgets.RadioBoxGroup(name='Mode Selector', options=['Static', 'Monovariate', 'Bivariate'], inline=True)
mode = radio_group.value

#  Equation Entry
text_input = pn.widgets.TextInput(name='Equation Input', placeholder='Enter your LaTeX equation here...')

#  Latex Pane
latex = pn.pane.LaTeX('')

#  Variable Selection Dropdown
indep_drop1 = pn.widgets.Select(name='Independent Variable 1', options=[])
indep_drop2 = pn.widgets.Select(name='Independent Variable 2', options=[])
dep_drop = pn.widgets.Select(name='Dependent Variable', options=[])


#Dynamic Updates
# ---------------------------------------------------------

#  Update Pane
def update_latex_view(event):
    equation = fr'${text_input.value}$'
    try:
        latex.object = equation
    except Exception as e:
        latex.object = "Invalid equation"
        print(f"Error parsing equation for LaTeX: {e}")

text_input.param.watch(update_latex_view, 'value')



string = r'\frac{\pi^2}{6}'
spstring = parse_latex(string)
print(spstring)
