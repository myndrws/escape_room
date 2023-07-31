# for info see https://dash.plotly.com/all-in-one-components

from dash import Dash, Output, Input, State, html, dcc, callback, MATCH
import uuid

# All-in-One Components should be suffixed with 'AIO'
class questionBlockAIO(html.Div):  # html.Div will be the "parent" component

    class ids:
        for_input = lambda aio_id: {
            'component': 'questionBlockAIO',
            'subcomponent': 'for_input',
            'aio_id': aio_id
        }

    # Make the ids class a public class
    ids = ids

    # Define the arguments of the All-in-One component
    def __init__(
        self,
        list_of_qa_tuples: list,
        question_index: int,
        aio_id = None,
    ):
        """For question block component
        """ 

        question_number = question_index + 1
        question_string = f"> " + list_of_qa_tuples[question_index][0]
                
        if aio_id == None:
            aio_id = f"q{question_number}"

        # Define the component's layout
        super().__init__([ # Equivalent to `html.Div([...])`
            html.H4(question_string), 
            dcc.Input(id=self.ids.for_input(aio_id), 
            placeholder="Answer",
            type="text", 
            value='')
            ])
