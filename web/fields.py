import flask_wtf
from widgets import * #http://wtforms.readthedocs.org/en/latest/fields.html

class BreachField(CheckboxButtonField):
    col_md = 2
    col_sm = 4
    col_xs = 12

class Form(flask_wtf.Form):
    match_id = IntegerField('Match ID', buttons=False)
    team_id = IntegerField('Team ID', buttons=False)
    #Auton Section
    auton_start = RadioField('Robot Starting Location',choices=[('Neutral Zone','Neutral Zone'), ('Courtyard','Courtyard')],
                             default='Neutral Zone')
    auton_breach = RadioField('Defense Crossed in Auton', choices=[('0','None'),
                                                                   ('1','Touched'),
                                                                   ('2','Crossed (Mark the defense in the Teleop section)')],
                                                                   default='0')
    auton_score = RadioField('Ball Scored', choices=[('0','None'), ('1','Low Goal'), ('2','High Goal')],
                             default='0')
    #Teleop Section

    #Breaching checkboxes
    lb_breach = BreachField('Low Bar')
    pc_breach = BreachField('Portcullis')
    cf_breach = BreachField('Cheval de Frise')
    mo_breach = BreachField('Moat')
    rp_breach = BreachField('Ramparts')
    db_breach = BreachField('Drawbridge')
    sp_breach = BreachField('Sally Port')
    rw_breach = BreachField('Rock Wall')
    rt_breach = BreachField('Rough Terrain')

    #Other
    breach_count = IntegerField('Number of defenses crossed', default=0,
        col_md=6,
        label_col_md=6,
        col_sm=8,
        label_col_sm=12)
    high_scores = IntegerField('High Goals Scored', default=0, col_sm=6)
    high_misses = IntegerField('High Shots Missed', default=0, col_sm=6)
    low_scores = IntegerField('Low Goals Scored', default=0, col_sm=6)
    fouls = IntegerField('Fouls', default=0, col_sm=6)
    tech_fouls = IntegerField('Tech Fouls', default=0, col_sm=6)

    defense_rating = RadioField('How well did they play defense?', choices=[('0','Did not Defend'), ('1', 'Bad Defense'), ('2', 'Moderate Defense'), ('3', 'Best Defense')], default="0")
    defense_time = RadioField('How much time did they spend on defense?', choices=[('0', 'No Time'), ('1', 'Less than Half'), ('2', 'Most of the Time'), ('3', 'All Match')], default="0")

    hang = CheckboxButtonField('Robot Scaled Tower', col_md=3)
    comments = TextAreaField('', col_lg=12)
