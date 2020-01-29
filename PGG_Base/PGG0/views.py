from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class Contribution(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.calculate_total_contribution()
        for p in self.group.get_players():
            p.calculate_payoff()


class SummaryPage(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        total_payoff = 0
        for r in self.player.in_all_rounds():
            total_payoff += r.payoff
        return {'total_payoff': total_payoff}


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        total_payoff = 0
        for r in self.player.in_all_rounds():
            total_payoff += r.payoff
        return {'total_payoff': total_payoff}

    def before_next_page(self):
        total_payoff = 0
        for r in self.player.in_all_rounds():
            total_payoff += r.payoff
        self.participant.vars['total_payoff_PGG0'] = total_payoff
        self.participant.vars['PGG_number'] = 0
        self.participant.vars['player_role'] = "manager" if self.player.role() == "manager" else "peer"


class NextApp(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def before_next_page(self):
        total_payoff = 0
        for r in self.player.in_all_rounds():
            total_payoff += r.payoff
        self.participant.vars['total_payoff_PGG0'] = total_payoff


page_sequence = [
    Instructions,
    Contribution,
    ResultsWaitPage,
    #SummaryPage,
    Results
    #NextApp
]
