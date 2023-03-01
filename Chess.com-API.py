from chessdotcom import get_leaderboards, get_player_stats, get_player_game_archives
import pprint
import requests
import chess
import chess.engine

	
printer = pprint.PrettyPrinter()

def print_leaderboards():
	data = get_leaderboards().json
	categories = data.keys()

	for category in categories:
		print('Category:', category)
		for idx, entry in enumerate(data[category]):
			print(f'Rank: {idx + 1} | Username: {entry["username"]} | Rating: {entry["score"]}')


def get_player_rating(username):
	data = get_player_stats(username).json
	categories = ['chess_blitz', 'chess_rapid', 'chess_bullet']
	for category in categories:
		print('Category:', category)
		print(f'Current: {data[category]["last"]["rating"]}')
		print(f'Best: {data[category]["best"]["rating"]}')
		print(f'Best: {data[category]["record"]}')

def get_most_recent_game(username):
	data = get_player_game_archives(username).json
	url = data['archives'][-1]
	games = requests.get(url).json()
	game = games['games'][-1]
	printer.pprint(game)

def get_best_move(board):
    # Use a chess engine to evaluate the board position and suggest a move
    engine = chess.engine.SimpleEngine.popen_uci("/path/to/stockfish")
    result = engine.play(board, chess.engine.Limit(time=2.0))
    engine.quit()

    return result.move

get_most_recent_game('timruscica')