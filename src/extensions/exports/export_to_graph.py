import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from enum import Enum
from adjustText import adjust_text

class ExportToGraph:
    class Position(Enum):
        CENTER = 'center'
        LEFT = 'left'
        RIGHT = 'right'
        
    def __init__(self, data, dpi=100, figsize=(10, 6)):
        self.data = data
        self.dpi = dpi
        self.figsize = figsize
        self.fig, self.ax = plt.subplots(figsize=self.figsize)        
        
    def plot(self, kind='bar', x=None, y=None, hue=None, show_legend=True, legend_loc= 'best', legend_font_size:float=8, **kwargs):
        '''Build Seaborn charts with kind name
        '''
        plot_funcs = {
            "bar": sns.barplot,
            "line": sns.lineplot,
            "scatter": sns.scatterplot,
            "hist": sns.histplot,
            "box": sns.boxplot,
            "violin": sns.violinplot,
            "heat": sns.heatmap
        }
        if kind not in plot_funcs:
            raise ValueError(f"Graph type {kind} is't supported.")
        
        plot_funcs[kind](data=self.data, x=x, y=y, hue=hue, ax=self.ax, **kwargs)
        
        if show_legend and hue:
            self.ax.legend(loc=legend_loc, fontsize=legend_font_size)
        
        return self
    
    def show(self):
        plt.show()
        
    def serial(self, x, y, **kwargs):
        """Serial chart
        
        Args:
            - x: X axis (timeline)
            - y: Y axis (value)
            - **kwagrs: others parameters use for serial chart"""
        sns.lineplot(data=self.data, x=x, y=y, ax = self.ax, **kwargs)
    
    def pie(self, labels, sizes, colors=None, autopct='%1.1f%%', startangle:int=90, clockwise:bool=True, 
            move_small_labels:bool=True, hide_label:bool=False, show_legend:bool = True, legend_font_size:float=8,
            min_percent:float=4.0, explode_small=False
            ):
        """Pie chart
        
        Args:
            - labels: list of items
            - sizes: list of ratio of each part
            - colors: list corlor of each part
            - autopct: format for percentage
            - startangel: begin at angle
            - clockwise: chart clockwise if True else counterclock
            - move_small_labels: move small labels to outside when percentage is too small
            - hide_label: hidden label if False
            - show_legend: legend is shown if True
            - min_percent: keep parts is bigger than input percent else group them to Other"""
            
        labels = np.array(labels)
        sizes = np.array(sizes)
        total = sum(sizes)
        
        displayed_labels = None if hide_label else labels
        
        if min_percent > 0:
            mask = (sizes/total*100) >= min_percent
            other_size = sum(sizes[~mask])
            sizes = np.append(sizes[mask], other_size)
            labels = np.append(labels[mask], 'Other')
            if colors is not None:
                colors = np.array(colors)
                colors = np.append(colors[mask], '#cccccc')
                
        wedges, texts, autotexts = self.ax.pie(
            sizes, labels=displayed_labels, colors= colors, autopct=autopct,
            startangle=startangle, counterclock=not clockwise,
            pctdistance=0.75,
            explode=[0.1 if (size/total*100) < min_percent else 0 for size in sizes] if explode_small else None
        )
        # move label to outside if percentage is too small
        if move_small_labels:            
            for wedge, autotext in zip(wedges, autotexts):
                percent = float(autotext.get_text().strip('%'))
                if percent < min_percent:                      
                    theta = np.deg2rad((wedge.theta2 + wedge.theta1) / 2) 
                    x, y = autotext.get_position()
                    new_x, new_y = 1.3 * np.cos(theta), 1.3 * np.sin(theta)
                    #Move text to outside
                    autotext.set_position((new_x, new_y))                    
                    autotext.set_ha('center' if -0.5 < new_x < 0.5 else 'left' if new_x > 0 else 'right')
                    autotext.set_va('center')
                    # draw line to part of pie
                    self.ax.annotate(
                        autotext.get_text(),
                        xy=(x,y),                        
                        xytext=(new_x, new_y),  
                        arrowprops=dict(
                            arrowstyle='-', 
                            color='black', 
                            lw=0.5, 
                            connectionstyle="arc3,rad=0.1"
                        )
                    )
                    # bbox background is transparent
                    # autotext.set_bbox(dict(facecolor='none', edgecolor='none', alpha=0))
                    autotext.set_text("")
        if show_legend:
            self.ax.legend(wedges, labels, 
                           loc='center left', bbox_to_anchor=(1,0.5),
                           fontsize=legend_font_size)
        
        self.ax.axis('equal')                
        
    def toImage(self, output_file:str='graph.png'):
        """Export graph to image
        
        Args:
            output_file: image's filename"""
        self.fig.tight_layout()        
        self.fig.savefig(output_file, dpi=self.dpi, bbox_inches='tight')
        plt.close(self.fig)
        
    def setTitle(self, title:str, location:Position=Position.CENTER, y:float=-0.05):
        """Set title for the graph
        
        Args:
            title: title name"""
        self.ax.set_title(title, loc=location.value, y=y)
        
    def setLabels(self, xlabel:str = None, ylabel:str = None):
        """Set lable for X axis and Y axis
        
        Args:
            - xlabel: X axis name
            - ylabel: Y axis name"""
        if xlabel:
            self.ax.set_xlabel(xlabel)
        if ylabel:
            self.ax.set_ylabel(ylabel)
            
    def setAxisLimits(self, xlim=None, ylim=None):
        """Set limits for X axis and Y axis
        
        Args:
            - xlim: limit for X axis (tuple: (min, max))
            - ylim: limit for Y axis (tuple: (min, max))"""
        if xlim:
            self.ax.set_xlim(xlim)
        if ylim:
            self.ax.set_ylim(ylim)

# Ví dụ sử dụng lớp Plotter
if __name__ == "__main__":
    # Tạo dữ liệu mẫu
    tips = sns.load_dataset("tips")

    # Ví dụ vẽ biểu đồ tròn
    # plotter = ExportToGraph(data, dpi=300)
    # plotter.pie(labels=data['x'], sizes=data['y'],
    #             # colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen'], 
    #             startangle=90,hide_label=True, show_legend=True)
    # plotter.setTitle("Biểu đồ tròn", location=plotter.Position.CENTER, y=-0.06)
    # plotter.toImage('pie_chart_clockwise.png')
    

    plotter = ExportToGraph(tips, dpi=300)
    plotter.setTitle("Bar chart", location=plotter.Position.LEFT, y=1)
    plotter.plot(kind='bar', x='day', y='total_bill', hue='sex', show_legend=True, legend_loc='upper left').show()
    plotter.toImage("bar_chart2.png")