from rest_framework.test import APISimpleTestCase
from rest_framework import status
from apps.influential_figure.models import InfluentialFigure

class InfluentialFigureTest(APISimpleTestCase):
    def test_get_influential_figure_list(self):
        influential = InfluentialFigure(name='Zumbi', nationality='Brasileiro')
        influential.save()
        influential_figures = [
            {
                'name': 'Zumbi',
                'nationality': 'Brasileiro'
            }
        ]
        response = self.client.get("/influential_figures")
        del response.data[0]['id']
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(influential_figures, response.data)