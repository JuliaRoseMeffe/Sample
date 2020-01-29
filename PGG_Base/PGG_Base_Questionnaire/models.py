from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'JRM'

doc = """
Questionnaire and final summary of total earnings
"""


class Constants(BaseConstants):
    name_in_url = 'PGG_Base_Questionnaire'
    players_per_group = 4
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Questionnaire part 1
    # What is your gender?
    gender = models.StringField(
        choices=['Female', 'Male'],
        widget=widgets.RadioSelect,
        label=""
    )

    # What is your age?
    age = models.IntegerField(
        min=1,
        label=""
    )

    # Your highest education
    education = models.StringField(
        choices=['Qualifications for University Entrance', 'Bachelor', 'Master', 'Doctor', 'Other'],
        widget=widgets.RadioSelect,
        label=""
    )

    # Questionnaire part 2
    question_4a = models.StringField(
        choices=['Yes','No'],
        widget=widgets.RadioSelect,
        label=""
    )
    question_4b = models.LongStringField(label="")
    question_5a = models.StringField(
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect,
        label=""
    )
    question_5 = models.LongStringField(label="")
    question_6a = models.StringField(
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect,
        label=""
    )
    question_6 = models.LongStringField(label="")
    question_7 = models.LongStringField(label="")

    # Questionnaire part 3
    question_8a = models.StringField(
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect,
        label=""
    )
    question_8x = models.StringField(
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect,
        label=""
    )
    question_8 = models.LongStringField(label="")
    question_9a = models.StringField(
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect,
        label=""
    )
    question_9x = models.StringField(
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect,
        label=""
    )
    question_9 = models.LongStringField(label="")
    question_10a = models.StringField(
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect,
        label=""
    )
    question_10 = models.LongStringField(label="")


    question_11a = models.StringField(
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect,
        label=""
    )
    question_11 = models.LongStringField(label="")
    question_12a = models.StringField(
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect,
        label=""
    )
    question_12 = models.LongStringField(label="")

    prolificID_Input = models.StringField(label="")