import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

ext_css = ['https://www.w3schools.com/w3css/4/w3.css']

df = pd.read_csv('../audience.csv')
df['Date'] = pd.to_datetime(df['Date'])

app = dash.Dash(external_stylesheets=ext_css)
app.layout = html.Div(id='graph',children=[
		dcc.Graph(
			figure={
				'data' : [
					go.Scatter(
						x=df['Date'],
						y=df['Utilisateurs'],
						mode='markers'
					)
				]
			}, style={'width': '80vw', 'float': 'left'}
		),
		html.Div(id='my-div', style={'width': '20vw', 'float': 'left'}),
		dcc.Input(id='my-id', value='Dash App', type='text')
	])
	
@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

if __name__ == '__main__':
    app.run_server(debug=True)