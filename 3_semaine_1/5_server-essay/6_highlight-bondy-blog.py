import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output

import json

external_stylesheets = ['https://www.w3schools.com/w3css/4/w3.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('../bondyblog.csv')
# df = df[df['Commentaires'] > 0]
df.index = np.arange(len(df))

app.layout = html.Div([
					html.P(str(len(df.index)), style={
						'marginLeft': 20,
						'background': '#20a8d8',
						'color': 'white',
						'padding': 15,
						'fontSize': '27px',
						'borderRadius': 5,
						'border': '2px solid #038bba',
						'display': 'inline-block',
						'minWidth': 300,
						'marginBottom': 0
					}),
					html.P(str(len(df.index)), style={
						'marginLeft': 20,
						'background': '#f8cb00',
						'color': 'white',
						'padding': 15,
						'fontSize': '27px',
						'borderRadius': 5,
						'border': '2px solid rgb(219, 181, 7)',
						'display': 'inline-block',
						'minWidth': 300,
						'marginBottom': 0
					}, id='p2'),
					html.P(str(len(df['Auteur'].value_counts().index)), style={
						'marginLeft': 20,
						'background': '#f86c6b',
						'color': 'white',
						'padding': 15,
						'fontSize': '27px',
						'borderRadius': 5,
						'border': '2px solid rgb(216, 70, 69)',
						'display': 'inline-block',
						'minWidth': 300,
						'marginBottom': 0
					}),
					html.Div([
								dcc.Graph(
										id='g1',
										config={'displayModeBar': False},
										style={
											'width': '100%',
											'height': '60vh'
										}
									),
									html.Div(id="d1", style={'position': 'absolute','top':40,'left':30}),
									html.Div(id="d2", style={'position': 'absolute','top':60,'left':30})
								],  style={
										'margin': '20px',
										'background':'white',
										'border':'1px solid rgb(209, 209, 209)',
										'borderRadius':'5px',
										'paddingTop':'3px',
										'paddingBottom':'3px',
										'position': 'relative'
									}),
					html.Div([
								dcc.Graph(
										id='g2',
										config={'displayModeBar': True},
										style={
											'width': '100%',
											'height': '200vh'
										},
										figure={
											'data': [
												{
													'x': df['Date'],
													'y': df['Auteur'],
													'mode': 'markers'
												}],
											'layout': {
												'margin': {'l': 200, 'r': 0, 'b': 50, 't': 0},
												'hovermode':'closest'
											}
										}
									)
								],  style={
										'margin': '20px',
										'background':'white',
										'border':'1px solid rgb(209, 209, 209)',
										'borderRadius':'5px',
										'paddingTop':'3px',
										'paddingBottom':'3px',
										'position': 'relative'
									})
					], style={'background': '#e4e5e6', 'marginTop': '-20px', 'paddingTop': '20px'})

@app.callback(
    Output(component_id='g1', component_property='figure'),
    [Input(component_id='g1', component_property='hoverData')]
)
def update_output_div(input_value):
    if input_value is not None:
    	selected = [input_value['points'][0]['pointIndex']]
    	auteur = df[df.index == input_value['points'][0]['pointIndex']]['Auteur'].values[0]
    	selected = df[df['Auteur'] == auteur].index
    else:
    	texte = 'x'
    	selected = [0,1]
    return {
			'data': [{
					'x': df['Date'],
					'y': df['Commentaires'],
					'mode': 'markers',
					'selectedpoints': selected,
                    'marker': {'size': 6},
					'text': df['Auteur']
				}],
            'layout': {
                'margin': {'l': 0, 'r': 0, 'b': 0, 't': 0},
                'showlegend': False,
				'hovermode':'closest'
            }
		}
		
@app.callback(
    Output(component_id='p2', component_property='children'),
    [Input(component_id='g1', component_property='hoverData')]
)
def update_output_div(input_value):
    if input_value is not None:
    	selected = [input_value['points'][0]['pointIndex']]
    	auteur = df[df.index == input_value['points'][0]['pointIndex']]['Auteur'].values[0]
    	selected = df[df['Auteur'] == auteur].index
    else:
    	texte = 'x'
    	selected = []
    return len(selected)
		

		
@app.callback(
    Output(component_id='d1', component_property='children'),
    [Input(component_id='g1', component_property='clickData')]
)
def update_output_content(input_value):
	if input_value is not None:
		return json.dumps(input_value)
	else:
		return 'rien'

		
@app.callback(
    Output(component_id='d2', component_property='children'),
    [Input(component_id='g1', component_property='clickData')]
)
def update_output_content(input_value):
	if input_value is not None:
		return html.A(df[df.index == input_value['points'][0]['pointIndex']]['Lien'].values[0], href=df[df.index == input_value['points'][0]['pointIndex']]['Lien'].values[0], target="_blank")
	else:
		return 'rien'
if __name__ == '__main__':
    app.run_server(debug=True)