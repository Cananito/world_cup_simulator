#!/usr/bin/python3
# WRITTEN BY Eric Le Saux (elesaux@)
#
# Using Google's predictions when you enter in search:
# "fifa world cup <country1> <country2>
#
# We simulate the outcome of group C.
#
# HOME WIN DRAW LOSS AWAY
# FRA   76   16   18  AUS
# PER   30   30   40  DEN
# FRA   67   20   13  PER
# DEN   57   25   18  AUS
# DEN   16   26   58  FRA
# AUS   26   29   45  PER

import math
import operator
import random
import sys

elo = {
    'ARG': 2118,
    'AUS': 1779,
    'BEL': 1948,
    'BRA': 2137,
    'CAM': 1679,
    'CAN': 1712,
    'CRC': 1737,
    'CRO': 1945,
    'DEN': 1883,
    'ECU': 1842,
    'ENG': 1969,
    'ESP': 2007,
    'FRA': 1993,
    'GER': 1956,
    'GHA': 1596,
    'HOL': 2068,
    'IRN': 1779,
    'JPN': 1841,
    'KOR': 1801,
    'MEX': 1813,
    'MOR': 1871,
    'POL': 1827,
    'POR': 1993,
    'QAT': 1578,
    'SAU': 1643,
    'SEN': 1773,
    'SRB': 1835,
    'SWI': 1928,
    'TUN': 1747,
    'URU': 1905,
    'USA': 1819,
    'WAL': 1717,
}

def winProbability(country1, country2):
  elo1 = elo[country1]
  elo2 = elo[country2]
  return 1.0 / (math.pow(10.0, -(elo1-elo2)/400.0) + 1.0)

gamesGroupA = [
    # {'home': 'QAT', 'win': 0, 'draw': 0, 'loss': 100, 'away': 'ECU'},
    {'home': 'QAT', 'win': 0, 'draw': 0, 'loss': 100, 'away': 'ECU'},
    # {'home': 'SEN', 'win': 15, 'draw': 23, 'loss': 62, 'away': 'HOL'},
    {'home': 'SEN', 'win': 0, 'draw': 0, 'loss': 100, 'away': 'HOL'},
    # {'home': 'QAT', 'win': 17, 'draw': 25, 'loss': 58, 'away': 'SEN'},
    {'home': 'QAT', 'win': 0, 'draw': 0, 'loss': 100, 'away': 'SEN'},
    # {'home': 'HOL', 'win': 53, 'draw': 27, 'loss': 20, 'away': 'ECU'},
    {'home': 'HOL', 'win': 0, 'draw': 100, 'loss': 0, 'away': 'ECU'},
    # {'home': 'ECU', 'win': 39, 'draw': 30, 'loss': 31, 'away': 'SEN'},
    {'home': 'ECU', 'win': 0, 'draw': 0, 'loss': 100, 'away': 'SEN'},
    # {'home': 'HOL', 'win': 84, 'draw': 11, 'loss': 5, 'away': 'QAT'},
    {'home': 'HOL', 'win': 100, 'draw': 0, 'loss': 0, 'away': 'QAT'},
]

gamesGroupB = [
    # {'home': 'ENG', 'win': 73, 'draw': 19, 'loss': 8, 'away': 'IRN'},
    {'home': 'ENG', 'win': 100, 'draw': 0, 'loss': 0, 'away': 'IRN'},
    # {'home': 'USA', 'win': 39, 'draw': 31, 'loss': 30, 'away': 'WAL'},
    {'home': 'USA', 'win': 0, 'draw': 100, 'loss': 0, 'away': 'WAL'},
    # {'home': 'WAL', 'win': 45, 'draw': 30, 'loss': 25, 'away': 'IRN'},
    {'home': 'WAL', 'win': 0, 'draw': 0, 'loss': 100, 'away': 'IRN'},
    # {'home': 'ENG', 'win': 62, 'draw': 22, 'loss': 16, 'away': 'USA'},
    {'home': 'ENG', 'win': 0, 'draw': 100, 'loss': 0, 'away': 'USA'},
    # {'home': 'IRN', 'win': 23, 'draw': 27, 'loss': 50, 'away': 'USA'},
    {'home': 'IRN', 'win': 0, 'draw': 0, 'loss': 100, 'away': 'USA'},
    # {'home': 'WAL', 'win': 12, 'draw': 20, 'loss': 68, 'away': 'ENG'},
    {'home': 'WAL', 'win': 0, 'draw': 0, 'loss': 100, 'away': 'ENG'},
]

gamesGroupC = [
    # {'home': 'ARG', 'win': 84, 'draw': 12, 'loss': 4, 'away': 'SAU'},
    {'home': 'ARG', 'win': 0, 'draw': 0, 'loss': 100, 'away': 'SAU'},
    # {'home': 'MEX', 'win': 34, 'draw': 32, 'loss': 34, 'away': 'POL'},
    {'home': 'MEX', 'win': 0, 'draw': 100, 'loss': 0, 'away': 'POL'},
    # {'home': 'POL', 'win': 53, 'draw': 26, 'loss': 21, 'away': 'SAU'},
    {'home': 'POL', 'win': 100, 'draw': 0, 'loss': 0, 'away': 'SAU'},
    # {'home': 'ARG', 'win': 61, 'draw': 24, 'loss': 15, 'away': 'MEX'},
    {'home': 'ARG', 'win': 100, 'draw': 0, 'loss': 0, 'away': 'MEX'},
    # {'home': 'POL', 'win': 13, 'draw': 21, 'loss': 66, 'away': 'ARG'},
    {'home': 'POL', 'win': 0, 'draw': 0, 'loss': 100, 'away': 'ARG'},
    # {'home': 'SAU', 'win': 18, 'draw': 22, 'loss': 60, 'away': 'MEX'},
    {'home': 'SAU', 'win': 0, 'draw': 0, 'loss': 100, 'away': 'MEX'},
]

gamesGroupD = [
    # {'home': 'DEN', 'win': 66, 'draw': 0, 'loss': 12, 'away': 'TUN'},
    {'home': 'DEN', 'win': 0, 'draw': 100, 'loss': 0, 'away': 'TUN'},
    # {'home': 'FRA', 'win': 75, 'draw': 16, 'loss': 9, 'away': 'AUS'},
    {'home': 'FRA', 'win': 100, 'draw': 0, 'loss': 0, 'away': 'AUS'},
    # {'home': 'TUN', 'win': 40, 'draw': 30, 'loss': 30, 'away': 'AUS'},
    {'home': 'TUN', 'win': 0, 'draw': 0, 'loss': 100, 'away': 'AUS'},
    # {'home': 'FRA', 'win': 47, 'draw': 28, 'loss': 25, 'away': 'DEN'},
    {'home': 'FRA', 'win': 100, 'draw': 0, 'loss': 0, 'away': 'DEN'},
    # {'home': 'TUN', 'win': 15, 'draw': 23, 'loss': 62, 'away': 'FRA'},
    {'home': 'TUN', 'win': 100, 'draw': 0, 'loss': 0, 'away': 'FRA'},
    {'home': 'AUS', 'win': 100, 'draw': 0, 'loss': 0, 'away': 'DEN'},
]

gamesGroupE = [
    # {'home': 'GER', 'win': 64, 'draw': 21, 'loss': 15, 'away': 'JPN'},
    {'home': 'GER', 'win': 0, 'draw': 0, 'loss': 100, 'away': 'JPN'},
    # {'home': 'ESP', 'win': 84, 'draw': 12, 'loss': 4, 'away': 'CRC'},
    {'home': 'ESP', 'win': 100, 'draw': 0, 'loss': 0, 'away': 'CRC'},
    # {'home': 'JPN', 'win': 67, 'draw': 21, 'loss': 12, 'away': 'CRC'},
    {'home': 'JPN', 'win': 0, 'draw': 0, 'loss': 100, 'away': 'CRC'},
    # {'home': 'ESP', 'win': 40, 'draw': 26, 'loss': 34, 'away': 'GER'},
    {'home': 'ESP', 'win': 0, 'draw': 100, 'loss': 0, 'away': 'GER'},
    # {'home': 'JPN', 'win': 11, 'draw': 19, 'loss': 70, 'away': 'ESP'},
    {'home': 'JPN', 'win': 100, 'draw': 0, 'loss': 0, 'away': 'ESP'},
    # {'home': 'CRC', 'win': 3, 'draw': 7, 'loss': 90, 'away': 'GER'},
    {'home': 'CRC', 'win': 0, 'draw': 0, 'loss': 100, 'away': 'GER'},
]

gamesGroupF = [
    # {'home': 'MOR', 'win': 24, 'draw': 29, 'loss': 47, 'away': 'CRO'},
    {'home': 'MOR', 'win': 0, 'draw': 100, 'loss': 0, 'away': 'CRO'},
    # {'home': 'BEL', 'win': 63, 'draw': 22, 'loss': 15, 'away': 'CAN'},
    {'home': 'BEL', 'win': 100, 'draw': 0, 'loss': 0, 'away': 'CAN'},
    # {'home': 'BEL', 'win': 48, 'draw': 27, 'loss': 25, 'away': 'MOR'},
    {'home': 'BEL', 'win': 0, 'draw': 0, 'loss': 100, 'away': 'MOR'},
    # {'home': 'CRO', 'win': 43, 'draw': 29, 'loss': 28, 'away': 'CAN'},
    {'home': 'CRO', 'win': 100, 'draw': 0, 'loss': 0, 'away': 'CAN'},
    # {'home': 'CRO', 'win': 35, 'draw': 28, 'loss': 37, 'away': 'BEL'},
    {'home': 'CRO', 'win': 0, 'draw': 100, 'loss': 0, 'away': 'BEL'},
    # {'home': 'CAN', 'win': 26, 'draw': 27, 'loss': 47, 'away': 'MOR'},
    {'home': 'CAN', 'win': 0, 'draw': 0, 'loss': 100, 'away': 'MOR'},
]

gamesGroupG = [
    # {'home': 'SWI', 'win': 56, 'draw': 26, 'loss': 18, 'away': 'CAM'},
    {'home': 'SWI', 'win': 100, 'draw': 0, 'loss': 0, 'away': 'CAM'},
    # {'home': 'BRA', 'win': 66, 'draw': 21, 'loss': 13, 'away': 'SRB'},
    {'home': 'BRA', 'win': 100, 'draw': 0, 'loss': 0, 'away': 'SRB'},
    # {'home': 'CAM', 'win': 19, 'draw': 25, 'loss': 56, 'away': 'SRB'},
    {'home': 'CAM', 'win': 0, 'draw': 100, 'loss': 0, 'away': 'SRB'},
    # {'home': 'BRA', 'win': 70, 'draw': 19, 'loss': 11, 'away': 'SWI'},
    {'home': 'BRA', 'win': 100, 'draw': 0, 'loss': 0, 'away': 'SWI'},
    # {'home': 'SRB', 'win': 38, 'draw': 29, 'loss': 33, 'away': 'SWI'},
    {'home': 'SRB', 'win': 0, 'draw': 0, 'loss': 100, 'away': 'SWI'},
    # {'home': 'CAM', 'win': 8, 'draw': 14, 'loss': 78, 'away': 'BRA'},
    {'home': 'CAM', 'win': 100, 'draw': 0, 'loss': 0, 'away': 'BRA'},
]

gamesGroupH = [
    # {'home': 'URU', 'win': 54, 'draw': 27, 'loss': 19, 'away': 'KOR'},
    {'home': 'URU', 'win': 0, 'draw': 100, 'loss': 0, 'away': 'KOR'},
    # {'home': 'POR', 'win': 70, 'draw': 20, 'loss': 10, 'away': 'GHA'},
    {'home': 'POR', 'win': 100, 'draw': 0, 'loss': 0, 'away': 'GHA'},
    # {'home': 'KOR', 'win': 37, 'draw': 31, 'loss': 32, 'away': 'GHA'},
    {'home': 'KOR', 'win': 0, 'draw': 0, 'loss': 100, 'away': 'GHA'},
    # {'home': 'POR', 'win': 49, 'draw': 28, 'loss': 23, 'away': 'URU'},
    {'home': 'POR', 'win': 100, 'draw': 0, 'loss': 0, 'away': 'URU'},
    # {'home': 'KOR', 'win': 17, 'draw': 23, 'loss': 60, 'away': 'POR'},
    {'home': 'KOR', 'win': 100, 'draw': 0, 'loss': 0, 'away': 'POR'},
    # {'home': 'GHA', 'win': 19, 'draw': 24, 'loss': 57, 'away': 'URU'},
    {'home': 'GHA', 'win': 0, 'draw': 0, 'loss': 100, 'away': 'URU'},
]

groupStage = [
    {'name': 'A', 'games': gamesGroupA, 'final': {'HOL': 1, 'SEN': 2, 'ECU': 3, 'QAT': 4}},
    {'name': 'B', 'games': gamesGroupB, 'final': {'ENG': 1, 'USA': 2, 'IRN': 3, 'WAL': 4}},
    {'name': 'C', 'games': gamesGroupC, 'final': {'ARG': 1, 'POL': 2, 'MEX': 3, 'SAU': 4}},
    {'name': 'D', 'games': gamesGroupD, 'final': {'FRA': 1, 'AUS': 2, 'TUN': 3, 'DEN': 4}},
    {'name': 'E', 'games': gamesGroupE, 'final': {'JPN': 1, 'ESP': 2, 'GER': 3, 'CRC': 4}},
    {'name': 'F', 'games': gamesGroupF, 'final': {'MOR': 1, 'CRO': 2, 'BEL': 3, 'CAN': 4}},
    {'name': 'G', 'games': gamesGroupG, 'final': {'BRA': 1, 'SWI': 2, 'CAM': 3, 'SRB': 4}},
    {'name': 'H', 'games': gamesGroupH, 'final': {'POR': 1, 'KOR': 2, 'URU': 3, 'GHA': 4}}
]

def buildZeroedResults(games):
  zeroedResults = {}
  for game in games:
    zeroedResults[game['home']] = 0
    zeroedResults[game['away']] = 0
  return zeroedResults

def buildZeroedPlacements(games):
  zeroedPlacements = {}
  for game in games:
    zeroedPlacements[game['home']] = {1:0, 2:0, 3:0, 4:0}
    zeroedPlacements[game['away']] = {1:0, 2:0, 3:0, 4:0}
  return zeroedPlacements

def findGame(games, home, away):
  for game in games:
    if ((game['home']==home and game['away']==away) or
        (game['home']==away and game['away']==home)):
      return game
  raise 'Game not found.'

def play(game, results):
  outcome = random.randint(1,100)
  if outcome <= game['win']:
    results[game['home']] += 3
  elif outcome <= (game['win'] + game['draw']):
    results[game['home']] += 1
    results[game['away']] += 1
  else:
    results[game['away']] += 3

def homeScoredMoreGoals(games, home, away):
  game = findGame(games, home, away)
  # If the two teams have drawn, then it's a coin toss.
  if game['draw'] == 100:
    return random.randint(1,100) % 2 == 0
  # Simulate until we have a winner to separate two teams with the same points.
  while True:
    results = {home: 0, away: 0}
    play(game, results)
    if results[home] == 3:
      return True
    elif results[away] == 3:
      return False

def playGames(games):
  results = buildZeroedResults(games)
  for game in games:
    play(game, results)
  return results

def playGroup(games):
  results = playGames(games)
  sorted_results = sorted(results.items(), key=operator.itemgetter(1), reverse=True)
  ordered_results = []
  current = sorted_results.pop(0)
  while sorted_results:
    top = sorted_results.pop(0)
    if current[1] > top[1] or homeScoredMoreGoals(games, current[0], top[0]):
      ordered_results.append(current)
      current = top
    else:
      ordered_results.append(top)
  ordered_results.append(current)
  return ordered_results

def calculatePoints(games):
  pts = {}
  for game in games:
    home = game['home']
    away = game['away']
    if game['win'] == 100:
      pts[home] = pts.get(home, 0) + 3
      pts[away] = pts.get(away, 0) + 0
    elif game['draw'] == 100:
      pts[home] = pts.get(home, 0) + 1
      pts[away] = pts.get(away, 0) + 1
    elif game['loss'] == 100:
      pts[home] = pts.get(home, 0) + 0
      pts[away] = pts.get(away, 0) + 3
    else:
      pts[home] = pts.get(home, 0) + 0
      pts[away] = pts.get(away, 0) + 0
  return pts

def simulateGroupGames(games, final, numSimulations):
  # For each country, we compute the number of times they achieve each group
  # position.

  simulatedPlacements = buildZeroedPlacements(games)

  for sim in range(numSimulations):
    groupResults = playGroup(games)
    simulatedPlacements[groupResults[0][0]][1] += 1
    simulatedPlacements[groupResults[1][0]][2] += 1
    simulatedPlacements[groupResults[2][0]][3] += 1
    simulatedPlacements[groupResults[3][0]][4] += 1

  for country, pos in final.items():
    for p in range(1, 4):
      simulatedPlacements[country][p] = numSimulations if p == pos else 0

  return simulatedPlacements


def knockout(country1, country2):
  probability = winProbability(country1, country2)
  if random.random() < probability:
    return (country1, country2)
  else:
    return (country2, country1)

def simulateKnockoutGames(groupResults):
  winner = {}
  loser = {}

  # Group of 16
  # winner[49], loser[49] = knockout(groupResults['1A'], groupResults['2B'])
  winner[49], loser[49] = (groupResults['1A'], groupResults['2B']) # Netherlands beats USA.
  winner[50], loser[50] = knockout(groupResults['1C'], groupResults['2D'])
  winner[51], loser[51] = knockout(groupResults['1B'], groupResults['2A'])
  winner[52], loser[52] = knockout(groupResults['1D'], groupResults['2C'])
  winner[53], loser[53] = knockout(groupResults['1E'], groupResults['2F'])
  winner[54], loser[54] = knockout(groupResults['1G'], groupResults['2H'])
  winner[55], loser[55] = knockout(groupResults['1F'], groupResults['2E'])
  winner[56], loser[56] = knockout(groupResults['1H'], groupResults['2G'])

  # Quarter-Finals
  winner[57], loser[57] = knockout(winner[49], winner[50])
  winner[58], loser[58] = knockout(winner[53], winner[54])
  winner[59], loser[59] = knockout(winner[51], winner[52])
  winner[60], loser[60] = knockout(winner[55], winner[56])

  # Semi-finals
  winner[61], loser[61] = knockout(winner[57], winner[58])
  winner[62], loser[62] = knockout(winner[59], winner[60])

  # Final
  winner[63], loser[63] = knockout(loser[61], loser[62])
  winner[64], loser[64] = knockout(winner[61], winner[62])

  return (winner, loser)

def chooseGroupWinners(groupProbabilities):
  # This one is tricky.  Based on the group stage probabilities, we can randomly
  # choose the group winner.  But what do we do with the runner up?  Choosing
  # based on the probabilities to make it to the second spot is wrong, because
  # those probabilities are not independent of the actual selected winner.
  #
  # GROUP C
  #  FRA   1st  83.8   2nd  16.2   3rd   0.0   4th   0.0   => 100.0
  #  DEN   1st  16.2   2nd  76.2   3rd   7.5   4th   0.0   =>  92.5
  #  AUS   1st   0.0   2nd   7.5   3rd  47.7   4th  44.8   =>   7.5
  #  PER   1st   0.0   2nd   0.0   3rd  44.8   4th  55.2   =>   0.0
  #
  # If DEN wins the group, FRA MUST be 2nd, since it has 0% to be 3rd or 4th.
  #
  # But let's look at another group:
  #
  # GROUP B
  #  POR   1st  49.6   2nd  39.9   3rd  10.5   4th   0.0   =>  89.5
  #  ESP   1st  47.1   2nd  52.3   3rd   0.6   4th   0.0   =>  99.4
  #  IRN   1st   3.3   2nd   7.8   3rd  88.9   4th   0.0   =>  11.1
  #  MAR   1st   0.0   2nd   0.0   3rd   0.0   4th 100.0   =>   0.0
  #
  # IRN has 3.3% of being first of their group.  If they win their
  # last game against POR, the odds are.
  #
  # GROUP B
  #  ESP   1st  70.1   2nd  25.4   3rd   4.5   4th   0.0   =>  95.5
  #  IRN   1st  29.9   2nd  70.1   3rd   0.0   4th   0.0   => 100.0
  #  POR   1st   0.0   2nd   4.5   3rd  95.5   4th   0.0   =>   4.5
  #  MAR   1st   0.0   2nd   0.0   3rd   0.0   4th 100.0   =>   0.0

  groupWinners = {}
  for group in ['A','B','C','D','E','F','G','H']:
    # Let's select the winner of that group.
    winner_candidates = groupProbabilities['1' + group]
    winner = None
    transferable_probability = {}
    p = random.random()
    for (country, probability) in winner_candidates:
      if winner is None and p <= probability:
        winner = country
      else:
        transferable_probability[country] = probability
        p -= probability
    groupWinners['1' + group] = winner

    # Let's select runner-up of that group.
    runnerup_candidates = []
    for (country, probability) in groupProbabilities['2' +  group]:
      if country != winner:
        runnerup_candidates.append((country, probability + transferable_probability[country]))
    p = random.random()
    for (country, probability) in runnerup_candidates:
      if p <= probability:
        runnerup = country
        break
      p -= probability
    groupWinners['2' + group] = country

  return groupWinners

# Let's simulate all groups.
random.seed()
numSimulations = 1 if len(sys.argv) <= 1 else int(sys.argv[1])


print('Group Stage Results\n')

groupProbabilities = {}
for group in groupStage:
  simulatedPlacements = simulateGroupGames(group['games'], group['final'],  numSimulations)
  groupName = group['name']
  print('GROUP {name}'.format(name=groupName))

  slot1 = '1{name}'.format(name=groupName)
  slot2 = '2{name}'.format(name=groupName)
  groupProbabilities[slot1] = []
  groupProbabilities[slot2] = []

  pts = calculatePoints(group['games'])

  # Sorted by placement (`lambda kv: kv[1]`), comparing 1st places.
  for country, placement in sorted(simulatedPlacements.items(), key=lambda kv: kv[1][1], reverse=True):
    placement = simulatedPlacements[country]
    print('  {country} {pts}   1st {a:5.1f}   2nd {b:5.1f}   3rd {c:5.1f}   4th  {d:5.1f}   => {e:5.1f}'.format(
        country=country,
        pts=int(pts[country]),
        a=100.0*placement[1]/numSimulations,
        b=100.0*placement[2]/numSimulations,
        c=100.0*placement[3]/numSimulations,
        d=100.0*placement[4]/numSimulations,
        e=100.0*(placement[1]+placement[2])/numSimulations))
    groupProbabilities[slot1].append((country, float(placement[1])/numSimulations))
    groupProbabilities[slot2].append((country, float(placement[2])/numSimulations))
  print('')

# Let's simulate the knockout phase.
firstPlace = {}
secondPlace = {}
thirdPlace = {}
eliminated = {
    'ARG': [0,0,0,0,0,0],
    'AUS': [0,0,0,0,0,0],
    'BEL': [0,0,0,0,0,0],
    'BRA': [0,0,0,0,0,0],
    'CAM': [0,0,0,0,0,0],
    'CAN': [0,0,0,0,0,0],
    'CRC': [0,0,0,0,0,0],
    'CRO': [0,0,0,0,0,0],
    'DEN': [0,0,0,0,0,0],
    'ECU': [0,0,0,0,0,0],
    'ENG': [0,0,0,0,0,0],
    'ESP': [0,0,0,0,0,0],
    'FRA': [0,0,0,0,0,0],
    'GER': [0,0,0,0,0,0],
    'GHA': [0,0,0,0,0,0],
    'HOL': [0,0,0,0,0,0],
    'IRN': [0,0,0,0,0,0],
    'JPN': [0,0,0,0,0,0],
    'KOR': [0,0,0,0,0,0],
    'MEX': [0,0,0,0,0,0],
    'MOR': [0,0,0,0,0,0],
    'POL': [0,0,0,0,0,0],
    'POR': [0,0,0,0,0,0],
    'QAT': [0,0,0,0,0,0],
    'SAU': [0,0,0,0,0,0],
    'SEN': [0,0,0,0,0,0],
    'SRB': [0,0,0,0,0,0],
    'SWI': [0,0,0,0,0,0],
    'TUN': [0,0,0,0,0,0],
    'URU': [0,0,0,0,0,0],
    'USA': [0,0,0,0,0,0],
    'WAL': [0,0,0,0,0,0],
}

for _ in range(numSimulations):
  groupWinners = chooseGroupWinners(groupProbabilities)
  winner, loser = simulateKnockoutGames(groupWinners)

  # Group of 16
  eliminated[loser[49]][1] += 1
  eliminated[loser[50]][1] += 1
  eliminated[loser[51]][1] += 1
  eliminated[loser[52]][1] += 1
  eliminated[loser[53]][1] += 1
  eliminated[loser[54]][1] += 1
  eliminated[loser[55]][1] += 1
  eliminated[loser[56]][1] += 1
  # Group of 8 (quarter-finals)
  eliminated[loser[57]][2] += 1
  eliminated[loser[58]][2] += 1
  eliminated[loser[59]][2] += 1
  eliminated[loser[60]][2] += 1
  # Group of 4 (semi-finals)
  eliminated[loser[61]][3] += 1
  eliminated[loser[62]][3] += 1
  # Group of 2 (final - runner up)
  eliminated[loser[64]][4] += 1
  # Group of 1! (cup winner)
  eliminated[winner[64]][5] += 1
  # We ignore 3rd place, already counted as losers of semi-finals.

  firstPlace[winner[64]] = firstPlace.get(winner[64], 0) + 1
  secondPlace[loser[64]] = secondPlace.get(loser[64], 0) + 1
  thirdPlace[winner[63]] = thirdPlace.get(winner[63], 0) + 1


print('')
print('Elimination Probabilities\n')
print('         group     16      8      4    2nd    1st')
for country, placement in sorted(eliminated.items()):
  placement[0] = numSimulations - int(math.fsum(placement))
  print(' ', country, ' ', ' '.join(map(lambda n: '{0:5.1f}%'.format(100.0*n/numSimulations), placement)))
print()

def formatBest(category, results):
  sortedBest = ''
  col = 0
  for country, wins in sorted(results.items(),
                              key=operator.itemgetter(1), reverse=True):
    if col % 5 == 0:
      sortedBest += '\n'
    col += 1
    sortedBest += '  {country} {p:5.1f}'.format(country=country,
                                               p=(100.0*wins/numSimulations))

  return '{cat}:\n{best}\n'.format(cat=category, best=sortedBest)

print('')
print('Winning Probabilities\n')
print(formatBest('1st', firstPlace))
print(formatBest('2nd', secondPlace))
print(formatBest('3rd', thirdPlace))
