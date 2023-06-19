from django import forms

from game_app.games.models import GameModel


class BaseGameForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = '__all__'


class GameCreateForm(BaseGameForm):
    pass


class GameEditForm(BaseGameForm):
    pass


class GameDeleteForm(BaseGameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disable'] = 'disable'



