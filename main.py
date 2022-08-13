from forms import MonthFilterForm
from flask import Flask, render_template
from plotly.subplots import make_subplots
import pandas as pd
import json
import plotly
import plotly.express as px
import plotly.graph_objects as go

# Create Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'

# Read data from csv
df = pd.read_csv('test_dataset.csv').dropna().sort_values(by=['Date'])
country_values = df["Country"].unique()


@app.route('/', methods=["GET", "POST"])
def home():
    form = MonthFilterForm()
    if form.validate_on_submit():
        current_month = form.month.data
        # Create bar graphs
        fig_bar = make_subplots(rows=len(country_values), cols=1, subplot_titles=country_values)
        plot_pos = 1
        for country in country_values:
            country_df = df[(df['Date'].str.contains(fr"-{current_month}-")) & (df['Country'] == country)]
            fig_bar.add_trace(go.Bar(
                x=country_df['Date'],
                y=country_df['Target'],
                showlegend=False
            ), row=plot_pos, col=1)
            plot_pos += 1
        fig_bar.update_layout(height=1200, title_text="Monthly Income")
        bar_json = json.dumps(fig_bar, cls=plotly.utils.PlotlyJSONEncoder)

        # Create pie graph
        fig_pie = px.pie(df, values='Target', names='Country')
        fig_pie.update_layout(title_text="Income By Country")
        pie_json = json.dumps(fig_pie, cls=plotly.utils.PlotlyJSONEncoder)

        return render_template("index.html", form=form, pie_json=pie_json, bar_json=bar_json)
    return render_template("index.html", form=form)


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
