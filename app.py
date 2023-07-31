import dash
import time
import datetime
from dash import dcc, html
from dash.dependencies import Input, Output
from question_block import questionBlockAIO

# SETUP -----------------------------------------------------------

from questions import list_of_qa_tuples

CONTENT_STYLE = {
    "width":"100%",
    "height":"100%",
    "font-family": "Courier New, monospace",
    "backgroundColor": 'black',
    "color": 'white'
}

question_div_style = {
    "padding": "2rem",
    "width":"40%",
    "height":"60%",
    "display": 'inline-block',
    "backgroundColor": 'black',
    "vertical-align": "top"
}

div_style = {
    "width":"40%",
    "height":"60%",
    "display": 'inline-block',
    "backgroundColor": 'black',
    "vertical-align": "top"
}

escape_room_unlocked_div_style = {
    "padding": "1rem",
    "width":"100%",
    "height":"50%",
    "backgroundColor": 'black',
    "display": 'block'
}

escape_room_locked_div_style = {
    "padding": "1rem",
    "width":"100%",
    "height":"50%",
    "backgroundColor": 'black',
    "display": 'None'
}

top_heading_style = {  
    "padding-left": "2rem", 
"font-family":'monospace', 
"color": '#46e800'}

heading_style = { 
"padding": "2rem", 
"font-family":'monospace', 
"color": '#46e800'}

ai_heading_style = { 
"padding": "2rem", 
"font-family":'monospace', 
"color": 'red'}

button_style = {
    "margin": "2rem",
    "height":"1%",
    "background": "red",
	"padding": "1%",
	"justify-content": "center",
	"font-size": "15px",
	"font-weight": "bolder",
	"color": "white",
	"letter-spacing": "4px",
	"border": "1px solid white",
	"cursor": "pointer",
	"box-shadow": "0 5px 10px gray",
	"transition": "0.2s all"
}


def time_taken(start, end):
    time_taken = datetime.timedelta(seconds= end - start)
    hours, remainder = divmod(time_taken.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return minutes, seconds


# APP -----------------------------------------------------------

app = dash.Dash(__name__)

app.layout = html.Div([
    
    # before entering --------------------------------------------------
    
    html.Div([
    html.H1(">>> Help!", style=top_heading_style),
    html.H1(">>> An unfriendly AI has taken over the team", style=top_heading_style),
    html.H1(">>> Only through solving a sequence of", style=top_heading_style),
    html.H1(">>> highly human-specific tasks", style=top_heading_style),
    html.H1(">>> can we avoid automation oblivion", style=top_heading_style),
    html.H1(">>> and escape from the AI", style=top_heading_style),
    html.H1(">>> ", style=top_heading_style),
    html.H1(">>> ", style=top_heading_style),
    html.H1(">>> ", style=top_heading_style),
    html.H1(">>> ", style=top_heading_style),
    html.H1(">>> ", style=top_heading_style),
    html.H1(">>> ", style=top_heading_style),
    html.Button('Take on the AI', id='enter_escape_room', n_clicks=0, style=button_style),
    dcc.Store(id='start_time'),
    html.Div(id="ai_response_1")
    ], style=escape_room_unlocked_div_style),
    
    # escape room 1 ---------------------------------------------------
    
    html.Div(id="escape_room_1", children=[
    
    html.Div([
    html.H1(">>> Stop it from copying itself!", style=heading_style),
    questionBlockAIO(list_of_qa_tuples, 0),
    html.Br(),
    questionBlockAIO(list_of_qa_tuples, 1),
    html.Br(),
    questionBlockAIO(list_of_qa_tuples, 2),
    html.Br(),
    questionBlockAIO(list_of_qa_tuples, 3),
    html.Br(),
    questionBlockAIO(list_of_qa_tuples, 4),
    html.Br(),
    ], style=question_div_style),
    
    html.Div([
    html.Img(id="er1_image_result", src=app.get_asset_url("ai1.jpg")),
    html.Div(id='er1')
    ], style=div_style)
    
    ], style=escape_room_locked_div_style),
    
    # escape room 2 ------------------------------------------------------
    
    html.Div(id="escape_room_2", children=[
    
    html.Div([
    html.Img(id="er2_image_result", src=app.get_asset_url("ai2.jpg")),   
    html.Div(id='er2')
    ], style=div_style),
    
    html.Div([
    html.H1(">>> That was a decoy. I'm everywhere now. You won't escape.", style=ai_heading_style),
    questionBlockAIO(list_of_qa_tuples, 5),
    html.Br(),
    questionBlockAIO(list_of_qa_tuples, 6),
    html.Br(),
    questionBlockAIO(list_of_qa_tuples, 7),
    html.Br(),
    questionBlockAIO(list_of_qa_tuples, 8),
    html.Br(),
    questionBlockAIO(list_of_qa_tuples, 9),
    html.Br(),
    ], style=question_div_style)
    
    ], style=escape_room_locked_div_style),
    
    # escape room 3 ------------------------------------------------------
    
    html.Div(id="escape_room_3", children=[
    
    html.Div([
    html.H1(">>> Your last chance. My final triumph.", style=ai_heading_style),
    questionBlockAIO(list_of_qa_tuples, 10),
    html.Br(),
    questionBlockAIO(list_of_qa_tuples, 11),
    html.Br(),
    questionBlockAIO(list_of_qa_tuples, 12),
    html.Br(),
    questionBlockAIO(list_of_qa_tuples, 13),
    html.Br(),
    questionBlockAIO(list_of_qa_tuples, 14),
    html.Br(),
    ], style=question_div_style),
    
    html.Div([
    html.Img(id="er3_image_result", src=app.get_asset_url("ai1.jpg")),  
    html.Div(id='er3')
    ], style=div_style)
    
    ], style=escape_room_locked_div_style)
    
    # end of whole app layout ---------------------------------------------
    
    ], style=CONTENT_STYLE)

# callbacks for interactivity --------------------------------------------

@app.callback(
    [Output('er1', 'children'),
    Output('er1_image_result', 'src'),
    Output('escape_room_2', 'style')],
    [Input('start_time', 'data'),
    Input(questionBlockAIO.ids.for_input('q1'), 'value'),
    Input(questionBlockAIO.ids.for_input('q2'), 'value'),
    Input(questionBlockAIO.ids.for_input('q3'), 'value'),
    Input(questionBlockAIO.ids.for_input('q4'), 'value'),
    Input(questionBlockAIO.ids.for_input('q5'), 'value')])
    
def update_result_room_1(start_time, q1, q2, q3, q4, q5):
    """
    Returns a tuple for the output statement and image
    """
    
    condition = (q1.lower().strip() == list_of_qa_tuples[0][1]) \
    and (q2.lower().strip() == list_of_qa_tuples[1][1]) \
    and (q3.lower().strip() == list_of_qa_tuples[2][1]) \
    and (q4.lower().strip() == list_of_qa_tuples[3][1]) \
    and (q5.lower().strip() == list_of_qa_tuples[4][1]) 
    
    if condition: 
        mins, secs = time_taken(start_time, time.time())
        return html.H1([f">>> You escaped in {mins} minutes, {secs} seconds... but the AI is just getting started..."], style=heading_style), \
        app.get_asset_url("escaped_1.jpg"), \
        escape_room_unlocked_div_style
    else:
        return html.H1(["", html.Br(), ""]), app.get_asset_url("ai1.jpg"), escape_room_locked_div_style


@app.callback(
    [Output('er2', 'children'),
    Output('er2_image_result', 'src'),
    Output('escape_room_3', 'style')],
    [Input('start_time', 'data'),
    Input(questionBlockAIO.ids.for_input('q6'), 'value'), 
    Input(questionBlockAIO.ids.for_input('q7'), 'value'),
    Input(questionBlockAIO.ids.for_input('q8'), 'value'),
    Input(questionBlockAIO.ids.for_input('q9'), 'value'),
    Input(questionBlockAIO.ids.for_input('q10'), 'value')])
    
def update_result_room_2(start_time, q6, q7, q8, q9, q10):
    """
    Returns a tuple for the output statement and image
    """
    
    condition = (q6.lower().strip() == list_of_qa_tuples[5][1]) \
    and (q7.lower().strip() == list_of_qa_tuples[6][1]) \
    and (q8.lower().strip() == list_of_qa_tuples[7][1]) \
    and (q9.lower().strip() == list_of_qa_tuples[8][1]) \
    and (q10.lower().strip() == list_of_qa_tuples[9][1]) 
    
    
    if condition: 
        mins, secs = time_taken(start_time, time.time())
        return html.H1([f">>> Got it! You've taken {mins} minutes, {secs} seconds so far", html.Br(), ">>> Hurry! This is our last chance to prevent full AI takeover!"], style=heading_style), \
        app.get_asset_url("escaped_2.jpg"), \
        escape_room_unlocked_div_style
    else:
        return html.H1(["", html.Br(), ""]), app.get_asset_url("ai2.jpg"), escape_room_locked_div_style 
        
        
@app.callback(
    [Output('er3', 'children'),
    Output('er3_image_result', 'src')],
    [Input('start_time', 'data'),
    Input(questionBlockAIO.ids.for_input('q11'), 'value'),
    Input(questionBlockAIO.ids.for_input('q12'), 'value'),
    Input(questionBlockAIO.ids.for_input('q13'), 'value'),
    Input(questionBlockAIO.ids.for_input('q14'), 'value'), 
    Input(questionBlockAIO.ids.for_input('q15'), 'value')])
    
def update_result_room_3(start_time, q11, q12, q13, q14, q15):
    """
    Returns a tuple for the output statement and image
    """
    
    condition1 = (q11.lower().strip() == list_of_qa_tuples[10][1]) \
    and (q12.lower().strip() == list_of_qa_tuples[11][1]) \
    and (q13.lower().strip() == list_of_qa_tuples[12][1]) 
    
    condition2 = (q14.lower().strip() == list_of_qa_tuples[13][1]) \
    and (q15.lower().strip() == list_of_qa_tuples[14][1]) 
    
    if condition1 and not condition2:
        return html.H1(["No! No! Impossible!"], style=ai_heading_style), app.get_asset_url("ai3_angry.jpg") 
    elif condition1 and condition2: 
        mins, secs = time_taken(start_time, time.time())
        return html.H1([">>> You escaped!!!", html.Br(), ">>> You escaped!", html.Br(), f">>> You took {mins} minutes, {secs} seconds in total. Phew!"], style=heading_style), app.get_asset_url("escaped_3.jpg")
    else:
        return html.H1(["", html.Br(), ""]), app.get_asset_url("ai1.jpg")  
        
        
@app.callback(
    [
    Output('ai_response_1', 'children'),
    Output('escape_room_1', 'style'),
    Output('start_time', 'data')],
    Input('enter_escape_room', 'n_clicks')
)
def update_output(n_clicks):
    if n_clicks > 0: 
        return html.H1([">>> You can't escape inevitable automation."], style=ai_heading_style), \
        escape_room_unlocked_div_style, \
        time.time()
    else:
        return html.H1([""], style=ai_heading_style), \
        escape_room_locked_div_style, \
        None

#----------------------

if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0')
    
    