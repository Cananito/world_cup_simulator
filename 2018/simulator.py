#!/usr/bin/python
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

# As of Wednesday June 27 2018.
elo = {
    'ARG': 1896, 'AUS': 1713, 'BEL': 2059, 'BRA': 2114,
    'COL': 1939, 'CRC': 1726, 'CRO': 1973, 'DEN': 1896,
    'EGY': 1575, 'ENG': 1914, 'ESP': 2010, 'FRA': 2097,
    'GER': 1964, 'IRN': 1816, 'ISL': 1708, 'JPN': 1699,
    'KOR': 1757, 'KSA': 1588, 'MAR': 1720, 'MEX': 1829,
    'NGA': 1702, 'PAN': 1596, 'PER': 1890, 'POL': 1783,
    'POR': 1940, 'RUS': 1721, 'SEN': 1763, 'SRB': 1772,
    'SUI': 1879, 'SWE': 1866, 'TUN': 1662, 'URU': 1946
}

def winProbability(country1, country2):
  elo1 = elo[country1]
  elo2 = elo[country2]
  return 1.0 / (math.pow(10.0, -(elo1-elo2)/400.0) + 1.0)

gamesGroupA = [
    # {'home':'RUS', 'win': 67, 'draw': 22, 'loss': 11, 'away': 'KSA'},
    {'home':'RUS', 'win':100, 'draw':  0, 'loss':  0, 'away': 'KSA'},
    # {'home':'EGY', 'win': 14, 'draw': 26, 'loss': 60, 'away': 'URU'},
    {'home':'EGY', 'win':  0, 'draw':  0, 'loss':100, 'away': 'URU'},
    # {'home':'RUS', 'win': 67, 'draw': 20, 'loss': 13, 'away': 'EGY'},
    {'home':'RUS', 'win':100, 'draw':  0, 'loss':  0, 'away': 'EGY'},
    # {'home':'URU', 'win': 79, 'draw': 15, 'loss':  6, 'away': 'KSA'},
    {'home':'URU', 'win':100, 'draw':  0, 'loss':  0, 'away': 'KSA'},
    # {'home':'URU', 'win': 44, 'draw': 29, 'loss': 27, 'away': 'RUS'}
    {'home':'URU', 'win':100, 'draw':  0, 'loss':  0, 'away': 'RUS'},
    # {'home':'KSA', 'win': 19, 'draw': 27, 'loss': 54, 'away': 'EGY'},
    {'home':'KSA', 'win':100, 'draw':  0, 'loss':  0, 'away': 'EGY'},
]

gamesGroupB = [
    # {'home':'MAR', 'win': 44, 'draw': 31, 'loss': 25, 'away': 'IRN'},
    {'home':'MAR', 'win':  0, 'draw':  0, 'loss':100, 'away': 'IRN'},
    # {'home':'POR', 'win': 20, 'draw': 29, 'loss': 51, 'away': 'ESP'},
    {'home':'POR', 'win':  0, 'draw':100, 'loss':  0, 'away': 'ESP'},
    # {'home':'POR', 'win': 61, 'draw': 24, 'loss': 15, 'away': 'MAR'},
    {'home':'POR', 'win':100, 'draw':  0, 'loss':  0, 'away': 'MAR'},
    # {'home':'IRN', 'win':  5, 'draw': 14, 'loss': 81, 'away': 'ESP'},
    {'home':'IRN', 'win':  0, 'draw':  0, 'loss':100, 'away': 'ESP'},
    # {'home':'IRN', 'win': 16, 'draw': 28, 'loss': 56, 'away': 'POR'},
    {'home':'IRN', 'win':  0, 'draw':100, 'loss':  0, 'away': 'POR'},
    # {'home':'ESP', 'win': 71, 'draw': 18, 'loss': 11, 'away': 'MAR'}
    {'home':'ESP', 'win':  0, 'draw':100, 'loss':  0, 'away': 'MAR'}
]

gamesGroupC = [
    # {'home':'FRA', 'win': 76, 'draw': 16, 'loss': 18, 'away': 'AUS'},
    {'home':'FRA', 'win':100, 'draw':  0, 'loss':  0, 'away': 'AUS'},
    # {'home':'PER', 'win': 30, 'draw': 30, 'loss': 40, 'away': 'DEN'},
    {'home':'PER', 'win':  0, 'draw':  0, 'loss':1000, 'away': 'DEN'},
    # {'home':'DEN', 'win': 57, 'draw': 25, 'loss': 18, 'away': 'AUS'},
    {'home':'DEN', 'win':  0, 'draw':100, 'loss':  0, 'away': 'AUS'},
    # {'home':'FRA', 'win': 67, 'draw': 20, 'loss': 13, 'away': 'PER'},
    {'home':'FRA', 'win':100, 'draw':  0, 'loss':  0, 'away': 'PER'},
    # {'home':'DEN', 'win': 24, 'draw': 35, 'loss': 41, 'away': 'FRA'},
    {'home':'DEN', 'win':  0, 'draw':100, 'loss':  0, 'away': 'FRA'},
    # {'home':'AUS', 'win': 31, 'draw': 30, 'loss': 39, 'away': 'PER'}
    {'home':'AUS', 'win':  0, 'draw':  0, 'loss':100, 'away': 'PER'}
]

gamesGroupD = [
    # {'home':'ARG', 'win': 70, 'draw': 20, 'loss': 10, 'away': 'ISL'},
    {'home':'ARG', 'win':  0, 'draw':100, 'loss':  0, 'away': 'ISL'},
    # {'home':'CRO', 'win': 57, 'draw': 26, 'loss': 17, 'away': 'NGA'},
    {'home':'CRO', 'win':100, 'draw':  0, 'loss':  0, 'away': 'NGA'},
    # {'home':'ARG', 'win': 49, 'draw': 28, 'loss': 23, 'away': 'CRO'},
    {'home':'ARG', 'win':  0, 'draw':  0, 'loss':100, 'away': 'CRO'},
    # {'home':'NGA', 'win': 38, 'draw': 31, 'loss': 31, 'away': 'ISL'},
    {'home':'NGA', 'win':100, 'draw':  0, 'loss':  0, 'away': 'ISL'},
    # {'home':'NGA', 'win': 14, 'draw': 22, 'loss': 64, 'away': 'ARG'},
    {'home':'NGA', 'win':  0, 'draw':  0, 'loss':100, 'away': 'ARG'},
    # {'home':'ISL', 'win': 27, 'draw': 29, 'loss': 44, 'away': 'CRO'}
    {'home':'ISL', 'win':  0, 'draw':  0, 'loss':100, 'away': 'CRO'}
]

gamesGroupE = [
    # {'home':'BRA', 'win': 68, 'draw': 21, 'loss': 11, 'away': 'SUI'},
    {'home':'BRA', 'win':  0, 'draw':100, 'loss':  0, 'away': 'SUI'},
    # {'home':'CRC', 'win': 20, 'draw': 29, 'loss': 51, 'away': 'SRB'},
    {'home':'CRC', 'win':  0, 'draw':  0, 'loss':100, 'away': 'SRB'},
    # {'home':'SRB', 'win': 31, 'draw': 31, 'loss': 38, 'away': 'SUI'},
    {'home':'SRB', 'win':  0, 'draw':  0, 'loss':100, 'away': 'SUI'},
    # {'home':'BRA', 'win': 81, 'draw': 14, 'loss':  5, 'away': 'CRC'},
    {'home':'BRA', 'win':100, 'draw':  0, 'loss':  0, 'away': 'CRC'},
    # {'home':'SRB', 'win': 13, 'draw': 22, 'loss': 65, 'away': 'BRA'},
    {'home':'SRB', 'win':  0, 'draw':  0, 'loss':100, 'away': 'BRA'},
    # {'home':'SUI', 'win': 54, 'draw': 30, 'loss': 16, 'away': 'CRC'}
    {'home':'SUI', 'win':  0, 'draw':100, 'loss':  0, 'away': 'CRC'}
]

gamesGroupF = [
    # {'home':'GER', 'win': 65, 'draw': 22, 'loss': 13, 'away': 'MEX'},
    {'home':'GER', 'win':  0, 'draw':  0, 'loss':100, 'away': 'MEX'},
    # {'home':'SWE', 'win': 44, 'draw': 30, 'loss': 26, 'away': 'KOR'},
    {'home':'SWE', 'win':100, 'draw':  0, 'loss':  0, 'away': 'KOR'},
    # {'home':'KOR', 'win': 23, 'draw': 26, 'loss': 51, 'away': 'MEX'},
    {'home':'KOR', 'win':  0, 'draw':  0, 'loss':100, 'away': 'MEX'},
    # {'home':'GER', 'win': 68, 'draw': 21, 'loss': 11, 'away': 'SWE'},
    {'home':'GER', 'win':100, 'draw':  0, 'loss':  0, 'away': 'SWE'},
    # {'home':'MEX', 'win': 40, 'draw': 29, 'loss': 31, 'away': 'SWE'},
    {'home':'MEX', 'win':  0, 'draw':  0, 'loss':100, 'away': 'SWE'},
    # {'home':'KOR', 'win':  6, 'draw': 12, 'loss': 82, 'away': 'GER'}
    {'home':'KOR', 'win':100, 'draw':  0, 'loss':  0, 'away': 'GER'}
]

gamesGroupG = [
    # {'home':'BEL', 'win': 85, 'draw': 13, 'loss':  4, 'away': 'PAN'},
    {'home':'BEL', 'win':100, 'draw':  0, 'loss':  0, 'away': 'PAN'},
    # {'home':'TUN', 'win': 11, 'draw': 22, 'loss': 67, 'away': 'ENG'},
    {'home':'TUN', 'win':  0, 'draw':  0, 'loss':100, 'away': 'ENG'},
    # {'home':'BEL', 'win': 71, 'draw': 19, 'loss': 10, 'away': 'TUN'},
    {'home':'BEL', 'win':100, 'draw':  0, 'loss':  0, 'away': 'TUN'},
    # {'home':'ENG', 'win': 78, 'draw': 16, 'loss':  6, 'away': 'PAN'},
    {'home':'ENG', 'win':100, 'draw':  0, 'loss':  0, 'away': 'PAN'},
    # {'home':'ENG', 'win': 34, 'draw': 31, 'loss': 35, 'away': 'BEL'},
    {'home':'ENG', 'win':  0, 'draw':  0, 'loss':100, 'away': 'BEL'},
    # {'home':'PAN', 'win': 24, 'draw': 26, 'loss': 50, 'away': 'TUN'}
    {'home':'PAN', 'win':  0, 'draw':  0, 'loss':100, 'away': 'TUN'}
]

gamesGroupH = [
    # {'home':'COL', 'win': 57, 'draw': 26, 'loss': 17, 'away': 'JPN'},
    {'home':'COL', 'win':  0, 'draw':  0, 'loss':100, 'away': 'JPN'},
    # {'home':'POL', 'win': 41, 'draw': 30, 'loss': 29, 'away': 'SEN'},
    {'home':'POL', 'win':  0, 'draw':  0, 'loss':100, 'away': 'SEN'},
    # {'home':'JPN', 'win': 29, 'draw': 29, 'loss': 42, 'away': 'SEN'},
    {'home':'JPN', 'win':  0, 'draw':100, 'loss':  0, 'away': 'SEN'},
    # {'home':'POL', 'win': 29, 'draw': 29, 'loss': 42, 'away': 'COL'},
    {'home':'POL', 'win':  0, 'draw':  0, 'loss':100, 'away': 'COL'},
    # {'home':'SEN', 'win': 26, 'draw': 28, 'loss': 46, 'away': 'COL'},
    {'home':'SEN', 'win':  0, 'draw':  0, 'loss':100, 'away': 'COL'},
    # {'home':'JPN', 'win': 29, 'draw': 29, 'loss': 42, 'away': 'POL'}
    {'home':'JPN', 'win':  0, 'draw':  0, 'loss':100, 'away': 'POL'}
]

groupStage = [
    {'name': 'A', 'games': gamesGroupA, 'final': {'URU':1, 'RUS':2}},
    {'name': 'B', 'games': gamesGroupB, 'final': {'ESP':1, 'POR':2}},
    {'name': 'C', 'games': gamesGroupC, 'final': {'FRA':1, 'DEN':2}},
    {'name': 'D', 'games': gamesGroupD, 'final': {'CRO':1, 'ARG':2}},
    {'name': 'E', 'games': gamesGroupE, 'final': {'BRA':1, 'SUI':2}},
    {'name': 'F', 'games': gamesGroupF, 'final': {'SWE':1, 'MEX':2}},
    {'name': 'G', 'games': gamesGroupG, 'final': {'BEL':1, 'ENG':2}},
    {'name': 'H', 'games': gamesGroupH, 'final': {'COL':1, 'JPN':2}}
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

  for country, pos in final.iteritems():
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
  winner[49], loser[49] = (groupResults['1A'], groupResults['2B']) # Uruguay beats Portugal
  # winner[50], loser[50] = knockout(groupResults['1C'], groupResults['2D'])
  winner[50], loser[50] = (groupResults['1C'], groupResults['2D']) # France beats Argentina.
  # winner[51], loser[51] = knockout(groupResults['1B'], groupResults['2A'])
  winner[51], loser[51] = (groupResults['2A'], groupResults['1B']) # Russia beats Spain.
  # winner[52], loser[52] = knockout(groupResults['1D'], groupResults['2C'])
  winner[52], loser[52] = (groupResults['1D'], groupResults['2C']) # Croatia beats Denmark.
  # winner[53], loser[53] = knockout(groupResults['1E'], groupResults['2F'])
  winner[53], loser[53] = (groupResults['1E'], groupResults['2F']) # Brazil beats Mexico.
  # winner[54], loser[54] = knockout(groupResults['1G'], groupResults['2H'])
  winner[54], loser[54] = (groupResults['1G'], groupResults['2H']) # Belgium beats Japan.
  # winner[55], loser[55] = knockout(groupResults['1F'], groupResults['2E'])
  winner[55], loser[55] = (groupResults['1F'], groupResults['2E']) # Sweden beats Switzerland
  # winner[56], loser[56] = knockout(groupResults['1H'], groupResults['2G'])
  winner[56], loser[56] = (groupResults['2G'], groupResults['1H']) # England beats Colombia

  # Quarter-Finals
  # winner[57], loser[57] = knockout(winner[49], winner[50])
  winner[57], loser[57] = (winner[50], winner[49]) # France beats Uruguay.
  # winner[58], loser[58] = knockout(winner[53], winner[54])
  winner[58], loser[58] = (winner[54], winner[53]) # Belgium beats Brazil.
  # winner[59], loser[59] = knockout(winner[51], winner[52])
  winner[59], loser[59] = (winner[52], winner[51]) # Croatia beats Russia.
  # winner[60], loser[60] = knockout(winner[55], winner[56])
  winner[60], loser[60] = (winner[56], winner[55]) # England beat Sweden

  # Semi-finals
  # winner[61], loser[61] = knockout(winner[57], winner[58])
  winner[61], loser[61] = (winner[57], winner[58]) # France beats Belgium.
  # winner[62], loser[62] = knockout(winner[59], winner[60])
  winner[62], loser[62] = (winner[59], winner[60]) # Croatia beats England.

  # Final
  # winner[63], loser[63] = knockout(loser[61], loser[62])
  winner[63], loser[63] = (loser[61], loser[62]) # Belgium beats England.
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


print 'Group Stage Results\n'

groupProbabilities = {}
for group in groupStage:
  simulatedPlacements = simulateGroupGames(group['games'], group['final'],  numSimulations)
  groupName = group['name']
  print 'GROUP {name}'.format(name=groupName)

  slot1 = '1{name}'.format(name=groupName)
  slot2 = '2{name}'.format(name=groupName)
  groupProbabilities[slot1] = []
  groupProbabilities[slot2] = []

  pts = calculatePoints(group['games'])

  for country, placement in sorted(simulatedPlacements.iteritems(), key=operator.itemgetter(1), reverse=True):
    placement = simulatedPlacements[country]
    print '  {country} {pts}   1st {a:5.1f}   2nd {b:5.1f}   3rd {c:5.1f}   4th  {d:5.1f}   => {e:5.1f}'.format(
        country=country,
        pts=int(pts[country]),
        a=100.0*placement[1]/numSimulations,
        b=100.0*placement[2]/numSimulations,
        c=100.0*placement[3]/numSimulations,
        d=100.0*placement[4]/numSimulations,
        e=100.0*(placement[1]+placement[2])/numSimulations)
    groupProbabilities[slot1].append((country, float(placement[1])/numSimulations))
    groupProbabilities[slot2].append((country, float(placement[2])/numSimulations))
  print ''

# Let's simulate the knockout phase.
firstPlace = {}
secondPlace = {}
thirdPlace = {}
eliminated = {
    'ARG': [0,0,0,0,0,0], 'AUS': [0,0,0,0,0,0], 'BEL': [0,0,0,0,0,0], 'BRA': [0,0,0,0,0,0],
    'COL': [0,0,0,0,0,0], 'CRC': [0,0,0,0,0,0], 'CRO': [0,0,0,0,0,0], 'DEN': [0,0,0,0,0,0],
    'EGY': [0,0,0,0,0,0], 'ENG': [0,0,0,0,0,0], 'ESP': [0,0,0,0,0,0], 'FRA': [0,0,0,0,0,0],
    'GER': [0,0,0,0,0,0], 'IRN': [0,0,0,0,0,0], 'ISL': [0,0,0,0,0,0], 'JPN': [0,0,0,0,0,0],
    'KOR': [0,0,0,0,0,0], 'KSA': [0,0,0,0,0,0], 'MAR': [0,0,0,0,0,0], 'MEX': [0,0,0,0,0,0],
    'NGA': [0,0,0,0,0,0], 'PAN': [0,0,0,0,0,0], 'PER': [0,0,0,0,0,0], 'POL': [0,0,0,0,0,0],
    'POR': [0,0,0,0,0,0], 'RUS': [0,0,0,0,0,0], 'SEN': [0,0,0,0,0,0], 'SRB': [0,0,0,0,0,0],
    'SUI': [0,0,0,0,0,0], 'SWE': [0,0,0,0,0,0], 'TUN': [0,0,0,0,0,0], 'URU': [0,0,0,0,0,0]
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


print ''
print 'Elimination Probabilities\n'
print '         group     16      8      4    2nd    1st'
for country, placement in sorted(eliminated.iteritems()):
  placement[0] = numSimulations - int(math.fsum(placement))
  print ' ', country, ' ', ' '.join(map(lambda n: '{0:5.1f}%'.format(100.0*n/numSimulations), placement))
print

def formatBest(category, results):
  sortedBest = ''
  col = 0
  for country, wins in sorted(results.iteritems(),
                              key=operator.itemgetter(1), reverse=True):
    if col % 5 == 0:
      sortedBest += '\n'
    col += 1
    sortedBest += '  {country} {p:5.1f}'.format(country=country,
                                               p=(100.0*wins/numSimulations))

  return '{cat}:\n{best}\n'.format(cat=category, best=sortedBest)

print ''
print 'Winning Probabilities\n'
print formatBest('1st', firstPlace)
print formatBest('2nd', secondPlace)
print formatBest('3rd', thirdPlace)
