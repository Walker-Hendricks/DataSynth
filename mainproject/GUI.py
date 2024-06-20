#import data_analysis as da                         #My data analysis module
import panel as pn                                  #Main GUI application
import sympy as sp                                  #Analyzing text input
from sympy.parsing.latex import parse_latex         #Converting Latex input to Sympy
import re                                           #For isolating variables


pn.extension('mathjax')

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
dep_drop = pn.widgets.Select(name='Dependent Variable', options=['No item selected'])
indep_drop = pn.widgets.Select(name='Independent Variable', options=['No item selected'], visible=False)
indep_drop1 = pn.widgets.Select(name='Independent Variable 1', options=['No item selected'], visible=False)
indep_drop2 = pn.widgets.Select(name='Independent Variable 2', options=['No item selected'], visible=False)


# Dynamic Updates
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


#   Update Dropdown Visibility
def drop_vis(event):
    '''
    This function changes the visibility of the dropdown widgets based on radiobox input
    '''

    if event.new == 'Static':
        dep_drop.visible = True
        indep_drop.visible = False
        indep_drop1.visible = False
        indep_drop2.visible = False
    elif event.new == 'Monovariate':
        dep_drop.visible = True
        indep_drop.visible = True
        indep_drop1.visible = False
        indep_drop2.visible = False
    elif event.new == 'Bivariate':
        dep_drop.visible = True
        indep_drop.visible = False
        indep_drop1.visible = True
        indep_drop2.visible = True

    # Clear previous selections
    dep_drop.value = 'No item selected'
    indep_drop.value = 'No item selected'
    indep_drop1.value = 'No item selected'
    indep_drop2.value = 'No item selected'

radio_group.param.watch(drop_vis, 'value')


#   Update Dropdown Selections
def update_drop(event):
    equation = event.new
    # Find all variable names in the equation (letters followed by optional digits or underscores)
    variables = re.findall(r'\\?[a-zA-Z_\\\u03b1-\u03c9]\w*', equation)
    variables = [f"${var}$" for var in variables]
    # Setting new options
    dep_drop.options = ['No item selected'] + variables
    indep_drop.options = ['No item selected'] + variables
    indep_drop1.options = ['No item selected'] + variables
    indep_drop2.options = ['No item selected'] + variables

    # Clear previous selections
    dep_drop.value = 'No item selected'
    indep_drop.value = 'No item selected'
    indep_drop1.value = 'No item selected'
    indep_drop2.value = 'No item selected'

    update_vars(None)

text_input.param.watch(update_drop, 'value')


#   Update Constant Input
def update_vars(event):
    equation = text_input.value
    mode = radio_group.value
    dep_var = dep_drop.value
    indep_var = indep_drop.value
    indep_var1 = indep_drop1.value
    indep_var2 = indep_drop2.value

    # Find all variable names in the equation (letters followed by optional digits or underscores)
    variables = re.findall(r'\\?[a-zA-Z_\\\u03b1-\u03c9]\w*', equation)
    
    variables_inputs = {}
                
    # Remove values from those chosen as independent and dependent
    filtered_vars = [f"${var}$" for var in variables if f"${var}$" not in (dep_var, indep_var, indep_var1, indep_var2)]
    
    # Create new widgets for new variables
    for var in filtered_vars:
        if var not in variables_inputs:
            variables_inputs[var] = pn.widgets.TextInput(name=var, visible=True, min_width=80, width_policy='max', width = 80, max_width = 80)

    # Update the layout with the new set of widgets
    layout[:] = [radio_group, text_input, latex, dep_drop, indep_drop, indep_drop1, indep_drop2] + list(variables_inputs.values())

#Binding variable lists to other widgets
dep_drop.param.watch(update_vars, 'value')
indep_drop.param.watch(update_vars, 'value')
indep_drop1.param.watch(update_vars, 'value')
indep_drop2.param.watch(update_vars, 'value')


# Layout the widgets in a column
layout = pn.Column(radio_group, text_input, latex, dep_drop, indep_drop, indep_drop1, indep_drop2)



pn.serve(layout, port=5006, show=False)
