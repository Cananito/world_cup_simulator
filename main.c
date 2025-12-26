#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// TODO: Make it so each year's data is either loaded and parsed or #included.

// TODO: Delete Python programs, but keep their simulations.

// Elo ratings: https://www.eloratings.net/

#define COUNTRY_COUNT 48

struct Country {
  char country_name[20];
};

struct CountryElo {
  struct Country const* country;
  uint16_t elo_rating;
};

struct Match {
  struct Country const* home_team;
  struct Country const* away_team;
  struct Country const* winner;
  int8_t home_goals;
  int8_t away_goals;
};

struct Simulation {
  // (3 games/group * 12 groups) = 36 group stage matches + 32 knockout = 68
  struct Match matches[68];
};

enum Placement {
  FORTYEIGTH_PLACE,
  THIRTYSECOND_PLACE, // Eliminated in round of 32.
  SIXTEENTH_PLACE, // Eliminated in round of 16.
  EITH_PLACE, // Eliminated in quarterfinals.
  FOURTH_PLACE, // Lost third place match.
  THIRD_PLACE, // Won third place match.
  SECOND_PLACE, // Lost final.
  FIRST_PLACE, // Won final.
};

struct CountryPlacements {
  struct Country const* country;
  uint16_t forty_eight_place; // Eliminated in group stage.
  uint16_t thirty_second_place; // Eliminated in round of 32.
  uint16_t sixteenth_place; // Eliminated in round of 16.
  uint16_t eith_place; // Eliminated in quarterfinals.
  uint16_t fourth_place; // Lost third place match.
  uint16_t third_place; // Won third place match.
  uint16_t second_place; // Lost final.
  uint16_t first_place; // Won final.
};

struct Country const algeria = { .country_name = "Algeria" };
struct Country const argentina = { .country_name = "Argentina" };
struct Country const australia = {.country_name = "Australia" };
struct Country const austria = { .country_name = "Austria" };
struct Country const belgium = { .country_name = "Belgium" };
struct Country const brazil = { .country_name = "Brazil" };
struct Country const canada = { .country_name = "Canada" };
struct Country const cape_verde = { .country_name = "Cape Verde" };
struct Country const colombia = { .country_name = "Colombia" };
struct Country const croatia = { .country_name = "Croatia" };
struct Country const curacao = { .country_name = "Curacao" };
struct Country const ecuador = { .country_name = "Ecuador" };
struct Country const egypt = { .country_name = "Egypt" };
struct Country const england = { .country_name = "England" };
struct Country const france = { .country_name = "France" };
struct Country const germany = { .country_name = "Germany" };
struct Country const ghana = { .country_name = "Ghana" };
struct Country const haiti = { .country_name = "Haiti" };
struct Country const iran = { .country_name = "Iran" };
struct Country const ivory_coast = { .country_name = "Ivory Coast" };
struct Country const japan = { .country_name = "Japan" };
struct Country const jordan = { .country_name = "Jordan" };
struct Country const mexico = { .country_name = "Mexico" };
struct Country const moroco = { .country_name = "Moroco" };
struct Country const netherlands = { .country_name = "Netherlands" };
struct Country const new_zeland = { .country_name = "New Zeland" };
struct Country const norway = { .country_name = "Norway" };
struct Country const panama = { .country_name = "Panama" };
struct Country const paraguay = { .country_name = "Paraguay" };
struct Country const portugal = { .country_name = "Portugal" };
struct Country const qatar = { .country_name = "Qatar" };
struct Country const saudi_arabia = { .country_name = "Saudi Arabia" };
struct Country const scotland = { .country_name = "Scotland" };
struct Country const senegal = { .country_name = "Senegal" };
struct Country const south_africa = { .country_name = "South Africa" };
struct Country const south_korea = { .country_name = "South Korea" };
struct Country const spain = { .country_name = "Spain" };
struct Country const switzerland = { .country_name = "Switzerland" };
struct Country const tunisia = { .country_name = "Tunisia" };
struct Country const uruguay = { .country_name = "Uruguay" };
struct Country const usa = { .country_name = "USA" };
struct Country const uzbekistan = { .country_name = "Uzbekistan" };
// { .country_name = "<UEFA Path A winner>" };
// { .country_name = "<UEFA Path B winner>" };
// { .country_name = "<UEFA Path C winner>" };
// { .country_name = "<UEFA Path D winner>" };
// { .country_name = "<IC Path 1 winner>" };
// { .country_name = "<IC Path 2 winner>" },

struct CountryElo country_elos[COUNTRY_COUNT] = {
  { .country = &australia, .elo_rating = 0 },
  { .country = &algeria, .elo_rating = 0 },
  { .country = &argentina, .elo_rating = 0 },
  { .country = &australia, .elo_rating = 0 },
  { .country = &austria, .elo_rating = 0 },
  { .country = &belgium, .elo_rating = 0 },
  { .country = &brazil, .elo_rating = 0 },
  { .country = &canada, .elo_rating = 0 },
  { .country = &cape_verde, .elo_rating = 0 },
  { .country = &colombia, .elo_rating = 0 },
  { .country = &croatia, .elo_rating = 0 },
  { .country = &curacao, .elo_rating = 0 },
  { .country = &ecuador, .elo_rating = 0 },
  { .country = &egypt, .elo_rating = 0 },
  { .country = &england, .elo_rating = 0 },
  { .country = &france, .elo_rating = 0 },
  { .country = &germany, .elo_rating = 0 },
  { .country = &ghana, .elo_rating = 0 },
  { .country = &haiti, .elo_rating = 0 },
  { .country = &iran, .elo_rating = 0 },
  { .country = &ivory_coast, .elo_rating = 0 },
  { .country = &japan, .elo_rating = 0 },
  { .country = &jordan, .elo_rating = 0 },
  { .country = &mexico, .elo_rating = 0 },
  { .country = &moroco, .elo_rating = 0 },
  { .country = &netherlands, .elo_rating = 0 },
  { .country = &new_zeland, .elo_rating = 0 },
  { .country = &norway, .elo_rating = 0 },
  { .country = &panama, .elo_rating = 0 },
  { .country = &paraguay, .elo_rating = 0 },
  { .country = &portugal, .elo_rating = 0 },
  { .country = &qatar, .elo_rating = 0 },
  { .country = &saudi_arabia, .elo_rating = 0 },
  { .country = &scotland, .elo_rating = 0 },
  { .country = &senegal, .elo_rating = 0 },
  { .country = &south_africa, .elo_rating = 0 },
  { .country = &south_korea, .elo_rating = 0 },
  { .country = &spain, .elo_rating = 0 },
  { .country = &switzerland, .elo_rating = 0 },
  { .country = &tunisia, .elo_rating = 0 },
  { .country = &uruguay, .elo_rating = 0 },
  { .country = &usa, .elo_rating = 0 },
  { .country = &uzbekistan, .elo_rating = 0 },
};

static void run_simulation(struct Simulation* simulation, struct CountryPlacements* country_placements) {
  // TODO: Implement!

  simulation->matches[67] = (struct Match){
    .home_team = &england,
    .away_team = &usa,
    .home_goals = 7,
    .away_goals = 0,
    .winner = &england,
  };

  for (uint16_t i = 0; i < COUNTRY_COUNT; i++) {
    if (country_placements[i].country == &england) {
      country_placements[i].first_place += 1;
    }
    if (country_placements[i].country == &usa) {
      country_placements[i].second_place += 1;
    }
  }
}

int main(void) {
  uint32_t simulations_count = 5; // TODO: Change to 100000.

  // Initialize country placements.
  struct CountryPlacements country_placements[COUNTRY_COUNT] = { 0 };
  for (uint16_t i = 0; i < COUNTRY_COUNT; i++) {
    country_placements[i].country = country_elos[i].country;
  }

  // Run simulations.
  struct Simulation* all_simulations =
      calloc(simulations_count, sizeof(struct Simulation));
  for (uint32_t i = 0; i < simulations_count; i++) {
    run_simulation(&(all_simulations[i]), country_placements);
  }
  free(all_simulations);

  // TODO: Calculate averages and print.
  printf("      Country   48th   32nd   16th    8th    4th    3rd    2nd    1st\n");
  for (uint16_t i = 0; i < COUNTRY_COUNT; i++) {
    struct CountryPlacements country_placement = country_placements[i];
    printf("%13s %6d %6d %6d %6d %6d %6d %6d %6d\n",
           country_placement.country->country_name,
           country_placement.forty_eight_place,
           country_placement.thirty_second_place,
           country_placement.sixteenth_place,
           country_placement.eith_place,
           country_placement.fourth_place,
           country_placement.third_place,
           country_placement.second_place,
           country_placement.first_place
           );
  }

  return 0;
}
