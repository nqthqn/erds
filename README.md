## Getting started...

 - `python3 -m venv env`
 - `source env/bin/activate`
 - `pip install -r reqs.txt`
 - `python3 erds/manage.py graph_models --pygraphviz app -I Classroom,Student,Assessment,Image,AssessmentImageGroup,Response,ImageGroup -o erd.png && open erd.png`

## Change template

Edit `env/lib/python3.6/site-packages/django_extensions/templates/django_extensions/graph_models/*.dot`.

You can increase the font sizes, change colors, etc.

**label.dot**
`<FONT FACE="Helvetica Bold" COLOR="Black" POINT-SIZE="20">`

and...


**digraph.dot**
```
node [{% block node_options %}
    fontname = "Helvetica"
    fontsize = 16
    shape = "plaintext"
  {% endblock %}]

  edge [{% block edge_options %}
    fontname = "Helvetica"
    fontsize = 16
  {% endblock %}]
```
