import random as rnd
import pfc


def test_user_choice(mocker):
    mocker.patch('pfc.input', return_value="1")
    expected_value = ["1", "2", "3"]
    assert pfc.user_choice() in expected_value


def test_compare_choice():
    answer = rnd.randint(1, 3)
    ia_choice = rnd.randint(1, 3)
    expected_value = [1, 0, -1]
    assert pfc.compare_choices(answer, ia_choice) in expected_value


def test_compare_choice_with_wrong_entry():
    answer = 4
    ia_choice = rnd.randint(1, 3)
    expected_value = 0
    assert pfc.compare_choices(answer, ia_choice) == expected_value


def test_game_result_ia_wins(mocker):
    user_score = 2
    ia_score = 1
    winner = -1
    mocker.patch.object(pfc, 'phrases_player_wins', 'Joueur gagne')
    mocker.patch.object(pfc, 'phrases_ia_wins', 'IA gagne')
    expected_value = (2, 2)
    assert pfc.game_result(user_score, ia_score, winner) == expected_value


def test_game_result_player_wins(mocker):
    user_score = 2
    ia_score = 1
    winner = 1
    mocker.patch.object(pfc, 'phrases_player_wins', 'Joueur gagne')
    mocker.patch.object(pfc, 'phrases_ia_wins', 'IA gagne')
    expected_value = (3, 1)
    assert pfc.game_result(user_score, ia_score, winner) == expected_value


def test_game_result_draw(mocker):
    user_score = 2
    ia_score = 1
    winner = 0
    mocker.patch.object(pfc, 'phrases_player_wins', 'Joueur gagne')
    mocker.patch.object(pfc, 'phrases_ia_wins', 'IA gagne')
    expected_value = (2, 1)
    assert pfc.game_result(user_score, ia_score, winner) == expected_value


def test_game_result_wrong_entry(mocker):
    user_score = 2
    ia_score = 1
    winner = 4
    mocker.patch.object(pfc, 'phrases_player_wins', 'Joueur gagne')
    mocker.patch.object(pfc, 'phrases_ia_wins', 'IA gagne')
    expected_value = (2, 1)
    assert pfc.game_result(user_score, ia_score, winner) == expected_value


def test_new_game(mocker):
    user_score = 2
    ia_score = 1
    mocker.patch('pfc.user_choice', return_value=2)
    mocker.patch('pfc.compare_choices', return_value=1)
    mocker.patch('pfc.game_result', return_value=(3, 1))
    expected_value = (3, 1)
    assert pfc.new_game(user_score, ia_score) == expected_value


def test_new_game_with_wrong_entry(mocker):
    user_score = 2
    ia_score = 1
    mocker.patch('pfc.user_choice', return_value='lézard')
    expected_value = (2, 1)
    assert pfc.new_game(user_score, ia_score) == expected_value
