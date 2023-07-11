# Messkataloge app

import pandas as pd
import numpy as np
import pylab, matplotlib
from scipy.signal import savgol_filter
from bokeh.layouts import column, row
from bokeh.models.widgets import TextInput
from bokeh.models import Button, HoverTool, Div
from bokeh.plotting import figure, curdoc

###

# set up global variables
messkataloge_all = []
td_text = ""

# create the callback to do the search
def callback():
    # Clear the plot
    fig.renderers = []
    # Clear legend
    fig.legend.items = []
    #print(str(len(fig.legend)) + " = len of fig.legend:")
    #if len(fig.legend) > 0:
    #    print(str(len(fig.legend.items)))
    #    for li in range(len(fig.legend.items)):
    #        fig.legend.items[li].label.visible = False
    # Check to see if data file is loaded & if not load it
    if len(messkataloge_all) == 0:
        #curdoc().add_next_tick_callback(set_text_value) #(set_text_value) load_data()
        load_data()
    # Clear then parse search_words from text_input
    search_words = []
    search_words = text_input.value.split(",")
    ###
    # Set the colors dynamically using Matplotlib's color sets
    cmap = pylab.get_cmap('gist_rainbow', len(search_words))
    cmaph = []
    for i in range(cmap.N):
        cmaph.append(matplotlib.colors.rgb2hex(cmap(i)))
    search_tokens = []
    count = 0
    for stz in search_words:
        stz_stripped = stz.strip().lower()
        t256color = matplotlib.colors.rgb2hex(cmaph[count])
        search_tokens.append([stz_stripped, t256color])
        count += 1
    ###
    line_data = []
    def moving_average(x, w):
        return np.convolve(x, np.ones(w), 'valid') / w
    for st, colz in search_tokens:
        sr = messkataloge_all[messkataloge_all['token'] == st]
        search_totals = sr['yyyymm']
        svcounts = search_totals.value_counts().sort_index()
        # calculate frequencies for search_token counts (svcounts) for each yyyymm
        svcounts_df = pd.DataFrame({'yyyymm':svcounts.index, 'token_counts':svcounts.values})
        freq_df = pd.DataFrame({'yyyymm':dcounts.index, 'total_tokens':dcounts.values})
        freq_df = freq_df.merge(svcounts_df, how="left")
        # set all missing token_counts values to 0 (instead of NaN)
        freq_df['token_counts'] = freq_df['token_counts'].fillna(0)
        # set frequencies into 'freq' column
        freq_df['freq'] = freq_df['token_counts'] / freq_df['total_tokens']
        # 
        x = freq_df['yyyymm']
        y = freq_df['freq']
        y_ave = moving_average(y, 5)             #10 # 5 = number of rows to average for smoothing    
        y_savgol = savgol_filter(y_ave, 99, 3)   #29 vs 99 #y_ave, 99, 3  #deriv=0, delta=x[1] - x[0]  # Savitzky-Golay filtering for smoothing 
        #if y_savgol < 0: y_savgol = 0  # make sure not to go below 0 (the smoothing does this sometimes)
        #
        line_data.append([st, colz, x, y_savgol])
    # draw the lines
    for st, colz, x, y in line_data:
        fig.line(x, y, color=colz, legend_label=st.capitalize(), line_width=3) 
    ###
    # set up the tooltips
    hover = HoverTool(mode='vline')
    hover.tooltips = [("Frequency","@y{(.000000)}"), ("Year", "@x{(0.00)}")]
    fig.tools.append(hover)

###

# load the data file & generate token counts
def load_data():
    print("Loading data file...")
    global td_text
    global messkataloge_all, dcounts, tcounts 
    td_text = "Loading data file..."
    #curdoc().add_next_tick_callback(set_text_value)
    set_text_value()
    # Load the data file
    source_file = "all_tokens.csv"
    messkataloge_all = pd.read_csv(source_file)
    print("Data file loaded.")
    td_text = td_text + "<br>Data file loaded."
    #curdoc().add_next_tick_callback(set_text_value)
    set_text_value()
    #set_text_value("","",td_text)
    # remove neujahr data
    messkataloge_all = messkataloge_all.loc[messkataloge_all['yyyymm'] != 1703.01]
    messkataloge_all = messkataloge_all.loc[messkataloge_all['yyyymm'] != 1706.01]
    messkataloge_all = messkataloge_all.loc[messkataloge_all['yyyymm'] != 1708.01]
    messkataloge_all = messkataloge_all.loc[messkataloge_all['yyyymm'] != 1709.01]
    # lowercase all tokens
    messkataloge_all['token'] = [str(tokn).lower() for tokn in messkataloge_all['token']]
    print(str(len(messkataloge_all)) + " tokens read")
    td_text = td_text + "<br>" + str(len(messkataloge_all)) + " tokens read"
    #set_text_value("","",td_text)
    #curdoc().add_next_tick_callback(set_text_value)    
    set_text_value()
    # get total token counts for each yyyymm in the Kataloge
    all_dates = messkataloge_all['yyyymm']
    dcounts = all_dates.value_counts().sort_index()
    #get all counts
    all_tok = messkataloge_all['token']
    tcounts = all_tok.value_counts() #.sort_index()
    tc_df = pd.DataFrame(tcounts)

###

def set_text_value():
    text_div.text = td_text  #attr, old, 

###

# Add the base figure
fig = figure(title = "Messkataloge Frequencies (smoothed)", plot_width=900, plot_height=600)

# Add the text input box for our search terms
text_input = TextInput(value="", title="Enter search terms (lowercase, \",\" as separator):")

# add a button widget and set to run callback()
button = Button(label="Go")
button.on_event('button_click', callback)

text_div = Div(text="<i>Data file will be loaded on first search.</i>")
#text_div.on_change("text", set_text_value)

# put the text_input + button and the plot in a layout and add to the document for display
curdoc().title = "Messkataloge Frequencies"
curdoc().add_root(row(column(text_input, button, text_div), fig))
#    curdoc().add_next_tick_callback(set_text_value("","",td_text))
#curdoc().add_next_tick_callback(set_text_value)
