from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class QuestionnairePart1(Page):
    form_model = 'player'
    form_fields = [
        'gender',
        'age',
        'education'
    ]


class QuestionnairePart2(Page):
    form_model = 'player'
    form_fields = [
        #'question_4a',
        #'question_4b',
        #'question_5a',
        #'question_5',
        #'question_6',
        'question_7',
        'prolificID_Input'
    ]


#class QuestionnairePart3(Page):
#    form_model = 'player'
#    form_fields = [
#        'question_8a',
#        'question_8',
#        'question_9a',
#        'question_9',
#        'question_10a',
#        'question_10',
#        'question_11a',
#        'question_11',
#        'question_12a',
#        'question_12',
#        'question_13'
#    ]


class FinalPage(Page):


    timeout_seconds = 90

    def vars_for_template(self):
        total_payoff_1 = self.participant.vars['total_payoff_PGG0']     # Payoff from first experiment
        # Payoff from second experiment - either if PGG2 or PGG5
        #total_payoff_2 = self.participant.vars['total_payoff_PGG{}'.format(self.participant.vars['PGG_number'])]
        total_payoff_overall = total_payoff_1  # Sum of payoff
        self.player.payoff = total_payoff_overall
        self.participant.payoff = total_payoff_overall
        # Get player payoff plus their participation fee - and convert to currency
        self.participant.payoff_plus_participation_fee = total_payoff_overall.to_real_world_currency(self.session)
        return {
            #'total_payoff_1': total_payoff_1,
            'total_payoff_1': total_payoff_1,
            'total_payoff_overall': total_payoff_overall,
            'total_payment': total_payoff_overall.to_real_world_currency(self.session)
        }

class EndPage(Page):
    pass


page_sequence = [
    QuestionnairePart1,
    QuestionnairePart2,
    FinalPage
    #EndPage,
]
