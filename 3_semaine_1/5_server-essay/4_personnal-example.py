import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import json
import numpy as np

# importation dash, cc, core components et dependances

app = dash.Dash(external_stylesheets=['https://www.w3schools.com/w3css/4/w3.css'])
N = 100
app.layout = html.Div([
	html.Div([
			dcc.Graph(
				style={
					'height': '50vh'
				},
				figure={
					'data': [
						{
							'x': np.linspace(0, 1, N),
							'y': np.random.randn(N),
							# 'text': ['a', 'b', 'c', 'd'],
							# 'customdata': ['c.a', 'c.b', 'c.c', 'c.d'],
							# 'name': 'Trace 1',
							'mode': 'markers',
							'marker': {'size': 4}
						},
						{
							'x': np.linspace(0, 1, N),
							'y': np.random.randn(N),
							# 'text': ['w', 'x', 'y', 'z'],
							# 'customdata': ['c.w', 'c.x', 'c.y', 'c.z'],
							# 'name': 'Trace 2',
							# 'mode': 'markers',
							# 'marker': {'size': 12}
						}
					],
					'layout': {
						'clickmode': 'event+select',
						'showlegend': False,
						'margin': {'l': 15, 'r': 0, 'b': 15, 't': 5}
					}
				}
			)
	], style={'width': '60vw', 'float':'left'}),
	html.Div([
			dcc.Graph(
				id='Graphe',
				style={
					'height': '50vh'
				},
				figure={
					'data': [
						{
							'x': np.linspace(0, 1, N),
							'y': np.random.randn(N),
							# 'text': ['a', 'b', 'c', 'd'],
							# 'customdata': ['c.a', 'c.b', 'c.c', 'c.d'],
							# 'name': 'Trace 1',
							'mode': 'markers',
							'marker': {'size': 4}
						},
						{
							'x': np.linspace(0, 1, N),
							'y': np.random.randn(N),
							# 'text': ['w', 'x', 'y', 'z'],
							# 'customdata': ['c.w', 'c.x', 'c.y', 'c.z'],
							# 'name': 'Trace 2',
							# 'mode': 'markers',
							# 'marker': {'size': 12}
						}
					],
					'layout': {
						'clickmode': 'event+select',
						'showlegend': False
					}
				}
			)
	], style={'width': '40vw', 'float':'left'}),
	html.Div([
			dcc.Graph(
				id="Graphe2",
				style={
					'height': '50vh'
				},
				figure={
					'data': [
						{
							'x': np.linspace(0, 1, N),
							'y': np.random.randn(N),
							# 'text': ['a', 'b', 'c', 'd'],
							# 'customdata': ['c.a', 'c.b', 'c.c', 'c.d'],
							# 'name': 'Trace 1',
							'mode': 'markers',
							'marker': {'size': 4}
						},
						{
							'x': np.linspace(0, 1, N),
							'y': np.random.randn(N)
						}
					],
					'layout': {
						'clickmode': 'event+select',
						'showlegend': False
					}
				}
			)
	], style={'width': '100vw', 'float':'left'}),
	html.H1('Titre', style={'position': 'fixed', 'top': '50%', 'left':'150', 'padding-top':'-50%'}, id='Titre')
])

@app.callback(
    Output(component_id='Graphe2', component_property='figure'),
    [Input(component_id='Graphe', component_property='hoverData')]
)
def update_output_div(input_value):
    return {
				'data': [
					{
						'x': np.linspace(0, 1, N),
						'y': np.random.randn(N),
						# 'text': ['a', 'b', 'c', 'd'],
						# 'customdata': ['c.a', 'c.b', 'c.c', 'c.d'],
						# 'name': 'Trace 1',
						'mode': 'markers',
						'marker': {'size': 4}
					},
					{
						'x': np.linspace(0, 1, N),
						'y': np.random.randn(N)
					}
				],
				'layout': {
					'clickmode': 'event+select',
					'showlegend': False
				}
			}
@app.callback(
    Output(component_id='Titre', component_property='children'),
    [Input(component_id='Graphe', component_property='hoverData')]
)
def update_output_div(input_value):
    return json.dumps(input_value)

if __name__ == '__main__':
    app.run_server(debug=True)