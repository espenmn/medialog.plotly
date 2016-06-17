#plone stuff
from plone.app.layout.viewlets.common import ViewletBase
from zope.component import getMultiAdapter
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

#plotly stuff
import plotly 
from plotly.graph_objs import Bar, Scatter, Figure, Layout
import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

#login / api stuff
username = context.portal_registry['medialog.plotly.interfaces.IPlotlySettings.plotly_username']
api_key  = context.portal_registry['medialog.plotly.interfaces.IPlotlySettings.plotly_api_key']
plotly.tools.set_credentials_file(username=username, api_key=api_key)

class PlotView(ViewletBase):
    """ plot something """

    def make_plot(self):
        """https://plot.ly/python/getting-started/"""

        context = self.context
        title = context.Title()
        name = context.Description() or ''
        csv_file = context.csv_url
        
        df = pd.read_csv(csv_url)
        df.head()
        
        trace = go.Scatter(
                  #x-aksis og y-aksis
                  x = df['AAPL_x'], y = df['AAPL_y'],
                  name=name,
                  )
        layout = go.Layout(
                  title=title,
                  plot_bgcolor='rgb(230, 230,230)',
                  showlegend=True
                  )
        fig = go.Figure(data=[trace], layout=layout)
        context.plotlyhtml = plotly.offline.plot(fig, show_link=False, include_plotlyjs = False, output_type='div')
      
        
    def plotly_html(self):
        """return the html generated from plotly"""

        context = self.context
        if not context.plotlyhtml:
        	self.make_plot()
        
        return context.plotlyhtml