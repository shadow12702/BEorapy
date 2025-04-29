from pathlib import Path
import os
import pandas as pd


class Section():
    def __init__(self, id, header, data):
        self.id = id 
        self.header = header
        self.data = data
        

class ExportToHtml():
    
    def __init__(self, tilte: str):
        self.Title = tilte
        self._sections: list[Section]
         
    @property
    def sections(self):
        return self._sections
    
    @sections.setter
    def sections(self, value: list[Section]):
        self._sections = value
        
        
    @property
    def _set_css_style(self):
        """Generate CSS file"""
        css_content = """
        /* Base styles */
        :root {
            --primary-color: #336699;
            --secondary-color: #663300;
            --bg-color: #fcfcf0;
            --header-bg: #cccc99;
        }

        body {
            font: 10pt Arial, Helvetica, sans-serif;
            color: black;
            background: white;
            line-height: 1.6;
        }

        /* Typography */
        a {
            font-weight: bold;
            color: var(--secondary-color);
            text-decoration: none;
        }

        h1, h2, h3 {
            color: var(--primary-color);
            margin: 1em 0;
        }

        h1 { font-size: 16pt; }
        h2 { font-size: 14pt; }
        h3 { font-size: 12pt; }

        /* Navigation */
        nav ul {
            list-style: none;
            padding: 0;
        }

        nav li {
            font-size: 10pt;
            font-weight: bold;
            color: var(--primary-color);
            padding: 0.1em 0;
        }

        /* Data Grid */
        .data-grid {
            display: grid;
            gap: 1px;
            background: var(--header-bg);
            border: 1px solid var(--header-bg);
            font-size: 10pt;
            margin: 1em 0;
        }

        .grid-header {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
            background: var(--header-bg);
            color: var(--primary-color);
            font-weight: bold;
            padding: 0.5em;
        }

        .grid-row {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
            background: var(--bg-color);
            padding: 0.5em;
        }

        /* Utilities */
        .center { text-align: center; }
        .right { text-align: right; }
        .note { 
            font-size: 10pt;
            font-style: italic;
            color: var(--primary-color);
        }
        .footnote {
            font-size: 10pt;
            color: #999999;
        }
        """
        
        # css_file = os.path.join(self.output, "styles.css")
        # with open(css_file, "w", encoding='utf-8') as f:
        #     f.write(css_content)
        # return "styles.css"
        return css_content

    def _generate_html_header(self):
        '''Generate HTML5 header'''
        return [
             "<!DOCTYPE html>",
            "<html lang='en'>",
            "<head>",
            "<meta charset='UTF-8'>",
            "<meta name='viewport' content='width=device-width, initial-scale=1.0'>",
            "<title>Performance Analysis Report</title>",
            # f"<link rel='stylesheet' href='{css_file}'>",
            f"<style>{self._set_css_style}</style>"
            "</head>",
            "<body>"
        ]
    
    def _format_table_data(self, df:pd.DataFrame, time_col=None):
        """Create HTML5 semantic grid from a DataFrame with formatted data."""
        grid = ['<div class="data-grid">']
        
        # Add headers
        grid.append('<div class="grid-header">')
        for header in df.columns:
            grid.append(f'<div>{header}</div>')
        grid.append('</div>')
        
        # Add data rows
        for _, row in df.iterrows():
            grid.append('<div class="grid-row">')
            for col, cell in row.items():
                if time_col and col == time_col:
                    # Format datetime if specified
                    cell = cell.strftime('%Y-%m-%d %H:%M:%S')
                # elif isinstance(cell, (int, float)):
                #     # Format numbers with thousand separators
                #     cell = f'{cell:,}'
                grid.append(f'<div>{cell}</div>')
            grid.append('</div>')        
        grid.append('</div>')        
        return grid

    def _create_section(self, section:Section ):
        """Generic section creator with flexible data handling"""
        content = []
        content.append(f'<section id="{section.id}" class="report-section">')
        content.append(f'<h2>{section.header}</h2>')
        try:
            content.extend(self._format_table_data(section.data))
        except Exception as ex:
            content.append(f'<div class="error-message">{ex}</div>')
            
        content.append("</section>")
        return content
    
    def _gen_navigation(self):
        nav = ['<nav class="main-nav">', '<ul>']
        nav.extend([f'<li><a href="#{sec.id}">{sec.header}</a></li>' for sec in self.sections])
        nav.extend(["</ul>", "</nav>"])
        return nav
    
    # def _write_html(self, content):
    #     output_file = os.path.join(self.output, "performance_analysis_report.html")
    #     with open(output_file, "w", encoding='utf-8') as f:
    #         f.write('\n'.join(content))

    
    def generateHtml(self):
        try:
            html = []
            html.extend(self._generate_html_header())
            html.extend(self._gen_navigation())
                
            for section in self.sections:
                html.extend(self._create_section(section))
                
            html.extend(["</body>", "</html>"])
            # self._write_html(html)
            return html
        except Exception as ex:
            print(f"generateHtml error\n{ex}")
            
    
if __name__ == "__main__":
    work_dir = "/".join(Path.cwd().parts)
    csv_path = f"{work_dir}/staging/cdb"
    output = f"{work_dir}/staging"
    
    rpt = ExportToHtml("Performance Analysis Report")
    rpt.sections = [
        Section("db_general","General Database Information",pd.read_csv(f"{csv_path}/db_info.csv")),
        Section("glb_perf","Global Database Performance",pd.read_csv(f"{csv_path}/getAwrAasGraphGlobal.csv")),
        Section("instance_perf","Instance Database Performance",pd.read_csv(f"{csv_path}/getDbaHistoryStatisticGlobal.csv"))
    ]
    html=rpt.generateHtml()
    output_file = os.path.join(output, "performance_analysis_report.html")
    with open(output_file, "w", encoding='utf-8') as f:
        f.write('\n'.join(html))

