#Här är alla mina imports som detta programmet krävde
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

#██████╗░███████╗░█████╗░██╗░░░░░#
#██╔══██╗██╔════╝██╔══██╗██║░░░░░#
#██████╔╝█████╗░░███████║██║░░░░░#
#██╔══██╗██╔══╝░░██╔══██║██║░░░░░#
#██║░░██║███████╗██║░░██║███████╗#
#╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝#
#
#██████╗░███████╗░█████╗░░█████╗░░██████╗░███╗░░██╗██╗███████╗███████╗#
#██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝░████╗░██║██║╚════██║██╔════╝#
#██████╔╝█████╗░░██║░░╚═╝██║░░██║██║░░██╗░██╔██╗██║██║░░███╔═╝█████╗░░#
#██╔══██╗██╔══╝░░██║░░██╗██║░░██║██║░░╚██╗██║╚████║██║██╔══╝░░██╔══╝░░#
#██║░░██║███████╗╚█████╔╝╚█████╔╝╚██████╔╝██║░╚███║██║███████╗███████╗#
#╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═╝╚══════╝╚══════╝#
#
#██████╗░███████╗░█████╗░██╗░░░░░#
#██╔══██╗██╔════╝██╔══██╗██║░░░░░#
#██████╔╝█████╗░░███████║██║░░░░░#
#██╔══██╗██╔══╝░░██╔══██║██║░░░░░#
#██║░░██║███████╗██║░░██║███████╗#
#╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝#

#LÄSER IN DATAFRAMES som är .csv filer för två ST csv filer som jag presenterar statistik för (Natinal daily ICU.csv och Regional Totals data.csv)
nationaldailyicuadmissionsdf = pd.read_csv("National_Daily_ICU_Admissions.csv")
regionentotaldf = pd.read_csv("Regional_Totals_Data.csv")
genderdatadf = pd.read_csv("Gender_Data.csv")


#Sätter TEAMAT SLATE för att få en fin Mörkt Tema på hela min sida plus knappar o annat
app = dash.Dash(external_stylesheets=[dbc.themes.SLATE])

# Stylear Sidebar med CSS för att få den perfektstyling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "22rem",
    "padding": "2rem 1rem",
    "background-color": "#1c1e26",
    "color": "#FFFFFF"
}

# Stlear Content med CSS för att få den perfekt padding for the page content
CONTENT_STYLE = {
    "margin-left": "22rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#272b30",
    "color": "#FFFFFF"
}

#Här stylear jag GIFen som är på hemsidan som är där för att folk ska få budskapet att vaccin är viktigt för att stoppa covid-19
GIFHEMSTYLE = {
    "margin-left": "30rem",
    "width": "70rem",
}

#Här skapar jag en till style som är till för graphsen
GRAPHSTYLE = {
    "width": "100vh",
    "height": "100vh",
}

#Här skapar jag en till style som är till för gifsen som inte är på homepagen
GIFSTATSTYLE = {
    "display": "block",
    "margin-left": "auto",
    "margin-right": "auto",
    "width": "29%",
}

#Här gör jag sidebaren med html och gör så att knapparna länkar till mina STATISTIK sidor
sidebar = html.Div(
    [#Under här har jag vad det står i sidebaren så mitt namn och sen en välkommning och förklaring till vad man ska göra med sidan
        html.H2("DJBOLIVER", className="display-4"),
        html.Hr(),
        html.P(
            "Välkommen till DJ Bolivers covid Sida, här kan du se lite statistik angående COVID-19 SARS VIRUS2", className="lead"
        ),
        #Här är själva navigerinsdelen av sidebaren med knappar och annat
        dbc.Nav(
            [#Här under fixar jag så att knapparna länkar till korrekt sida
                dbc.NavLink("Hem", href="/hem", active="exact"),
                dbc.NavLink("Totala Fall Baserat På Region", href="/totalcasesbyregion", active="exact"),
                dbc.NavLink("Hela Nationens Dagliga Fall Som Slutat Med Inläggning på intensivvård", href="/nationaldaliyicuadmissions", active="exact"),
                dbc.NavLink("Köns Statistik", href="/konsstatistik", active="exact"),
            ],  
            vertical=True,
            pills=True,
        ),
    ],
    #Här sätter jag att stylen ska vara en style som jag tidigare definerat.
    style=SIDEBAR_STYLE,
)

#Sätter content variablen
content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

#Här är min app layout
app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
],)

#Här skapar jag statistiken med Plotly Express (PX) och sätter temat (Plotly Dark) och sedan vilken typ av statistik visnings metod (scatter eller bar osv)
#just denna är för regional total cases så totala fall per region
for template in ["plotly_dark"]:
    regionaltotalgraph = px.scatter(regionentotaldf, x="Cases_per_100k_Pop", y="Total_Cases",
                                size="Total_Cases", color="Total_Cases", size_max=55,
                                hover_name="Region", log_x=True,
                                template=template, title="Totala Fall Baserat På Region")

#Här skapar jag statistiken med Plotly Express (PX) och sätter temat (Plotly Dark) och sedan vilken typ av statistik visnings metod (scatter eller bar osv)
#just denna är nationens totala ICU admission.
for template in ["plotly_dark"]:
    nationaldailyicuadmissionsgraph = px.bar(nationaldailyicuadmissionsdf, x="Date", y="National_Daily_ICU_Admissions",
            title="National Daily ICU Admissions", template=template,)

#Här gör jag ett cirkel diagram med plotly express och sätter in värdena samt temat
for template in ["plotly_dark"]:
    genderdatagraphtotcases1 = px.pie(genderdatadf, values="Total_Cases", names="Gender", template=template,)

#Här gör jag ett cirkel diagram med plotly express och sätter in värdena samt temat
for template in ["plotly_dark"]:
    genderdatagraphtoticu2 = px.pie(genderdatadf, values="Total_ICU_Admissions", names="Gender", template=template,)

#Här gör jag ett cirkel diagram med plotly express och sätter in värdena samt temat
for template in ["plotly_dark"]:
    genderdatagraphtotded3 = px.pie(genderdatadf, values="Total_Deaths", names="Gender", template=template,)

#
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)

#Här gör jaf funktionen render page som har en if o några elif för att rendera rätt sida beroende på vilken url som är relevant
def render_page_content(pathname):
#IFall urlen är /hem så ska den displaya detta
    if pathname == "/hem":
        #Här returnar jag en simpel sida med en H1 html med lite välkomst text
        return [
                html.H1("WELCOME TO DJ BOLIVER COVID",
                        style={"textAlign":"center"}),
                
                html.H2(
    #Jag har också lagt in ett "card" här som var ett snabbt, snyggt och smidigt sätt att få in en bild på sidan (eller gif i detta fallet.)
                dbc.Card(
    [
        #Här länkar jag cardimage till min första gif url
        dbc.CardImg(src="https://media2.giphy.com/media/FO8CZ01HoTCA5ahQQq/giphy.gif?cid=ecf05e47ks3hjjkxhojh9rq8warbe3898jxgthd176kpi8in&rid=giphy.gif&ct=g", top=True),
    
    ],
    #Här sätter jag stylen som då är en av dem jag tidigare i KOden definerat
    style=(GIFHEMSTYLE),
)
        )
                ]

#IFall urlen är /totalcasesbyregion så ska den displaya detta
    elif pathname == "/totalcasesbyregion":
        #Här skapar jag en row, detta var till en början för dem sidorna som hade lite mer komplicerat innehål då jag inte bara kunder returna en H1 och en graph under men började blanda lite och ha detta samt endast return.
        row = html.Div(
            [
                #I rowen har jag mitt content på just denna sidan så HEAdern samt graphen
                html.H1("Totala Fall Baserat På Region",
                        style={"textAlign":"center"}),
                #Här är graphen
                dcc.Graph(figure=regionaltotalgraph),
                #Här är en av flera gifs som är under statisstiken för att sprida viktig information om covid 19 och för att fylla tomrummet under statistiken
                dbc.CardImg(src="https://media4.giphy.com/media/Qu1fT51CG14ksIkASL/giphy.gif?cid=790b761158eb46fafb1f823a8fddf87d4511526bce2ed6de&rid=giphy.gif&ct=g", top=True, style=GIFSTATSTYLE),
            ],

            )
        return row

#IFall urlen är /nationaldaliyicuadmissions så ska den displaya detta
    elif pathname == "/nationaldaliyicuadmissions":
        return [
            #I returnen har jag mitt content på just denna sidan så HEAdern samt graphen
                html.H1("Hela Nationens Dagliga Fall Som Slutat Med Inläggning på intensivvård",
                        style={"textAlign":"center"}),
                        #Här är graphen
                dcc.Graph(figure=nationaldailyicuadmissionsgraph),
                #Här är en av flera gifs som är under statisstiken för att sprida viktig information om covid 19 och för att fylla tomrummet under statistiken
                dbc.CardImg(src="https://media0.giphy.com/media/SsNnE066ZyWmeNLtyJ/giphy.gif?cid=790b7611776536b529d4b825ef57780b78741d33d8c04873&rid=giphy.gif&ct=g", top=True, style=GIFSTATSTYLE),
                ]

#IFall urlen är /konsstatistik så ska den displaya detta
    elif pathname == "/konsstatistik":
        #Här skapar jag en row, detta var för dem sidorna som hade lite mer komplicerat innehål då jag inte bara kunder returna en H1 och en graph under
        row = html.Div(
            [
                #Först har jag min header samt lite styling under
                dbc.Row(dbc.Col(html.Div(html.H1("Hur Covid har påverkat olika Kön",
                        style={"textAlign":"center"})))),
                dbc.Row(
                    [#i headern skapade jag en row och fyllde den med 3 columns och varje column innehåller en cirkel gRAph som jag tidigare skapat, jag blev också tvungen att säta with till 4,5 på alla för att göra det snyggt
                        dbc.Col(html.Div(dcc.Graph(figure=genderdatagraphtotcases1)), width=4.5),
                        dbc.Col(html.Div(dcc.Graph(figure=genderdatagraphtoticu2)), width=4.5),
                        dbc.Col(html.Div(dcc.Graph(figure=genderdatagraphtotded3)), width=4.5),
                    ]),
                dbc.Row(
                    [#Blev här tvungen att skapa en till row och förklara vad alla cirkeldiagrammen visade då det inte stod i cirkelgrammen själva om man inte höll musen över dem
                    #så skapade en row med 3 columns och fyllde dem med text som jag sedan alignade t centret, texten är då vad cirkelgraphsen visar.
                        dbc.Col(html.Div(html.H1("🠑TOTALA FALL🠑", style={"textAlign":"center"}))),
                        dbc.Col(html.Div(html.H1("🠑TOTALA INTENSIVVÅRDS🠑 INLÄGGNINGAR", style={"textAlign":"center"}))),
                        dbc.Col(html.Div(html.H1("🠑TOTALA DÖDSFALL🠑", style={"textAlign":"center"})))
                    ]
                    ),#Sedan avslutar jag alla sidor med en viktigt GIF
                dbc.Row([
                    dbc.CardImg(src="https://media1.tenor.com/images/fea45755ed5aaf6d2c8805f8b9de6fc2/tenor.gif?itemid=17867093", style=GIFSTATSTYLE),
                    ])
                
            ]
        )
        return row

    # om anändaren försöker nå en sida som inte existerar displayar den en sida med 404 error.
    return dbc.Jumbotron(
        [
            html.H1("404: Hittades Ej!", className="text-danger"),
            html.Hr(),
            html.P(f"urlen {pathname} existerar ej!"),
        ]
    )


#När programmet startas kör den locala servern på port 3000
if __name__=="__main__":
    app.run_server(debug=True, port=3000)

