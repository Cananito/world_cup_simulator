#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// TODO: Make it so each year's data is either loaded and parsed or #included.

// TODO: Delete Python programs, but keep their simulations.

// Elo ratings: https://www.eloratings.net/

#define COUNTRY_COUNT 48

struct Country {
  char country_name[20];
  uint16_t elo_rating;
  // TODO: Group stage identifier?
};

struct Match {
  struct Country const* home_team;
  struct Country const* away_team;
  struct Country const* winner;
  int8_t home_goals;
  int8_t away_goals;
};

struct Simulation {
  // (6 games/group * 12 groups) = 72 group stage matches + 32 knockout = 104
  struct Match matches[104];
};

struct GroupStageAccumulatedPlacements {
  struct Country const* country;
  uint16_t fourth_place;
  uint16_t third_place;
  uint16_t second_place;
  uint16_t first_place;
};

struct CountryAccumulatedPlacements {
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

struct Country const algeria = {
  .country_name = "Algeria",
  .elo_rating = 0,
};
struct Country const argentina = {
  .country_name = "Argentina",
  .elo_rating = 0,
};
struct Country const australia = {
  .country_name = "Australia",
  .elo_rating = 0,
};
struct Country const austria = {
  .country_name = "Austria",
  .elo_rating = 0,
};
struct Country const belgium = {
  .country_name = "Belgium",
  .elo_rating = 0,
};
struct Country const brazil = {
  .country_name = "Brazil",
  .elo_rating = 0,
};
struct Country const canada = {
  .country_name = "Canada",
  .elo_rating = 0,
};
struct Country const cape_verde = {
  .country_name = "Cape Verde",
  .elo_rating = 0,
};
struct Country const colombia = {
  .country_name = "Colombia",
  .elo_rating = 0,
};
struct Country const croatia = {
  .country_name = "Croatia",
  .elo_rating = 0,
};
struct Country const curacao = {
  .country_name = "Curacao",
  .elo_rating = 0,
};
struct Country const ecuador = {
  .country_name = "Ecuador",
  .elo_rating = 0,
};
struct Country const egypt = {
  .country_name = "Egypt",
  .elo_rating = 0,
};
struct Country const england = {
  .country_name = "England",
  .elo_rating = 0,
};
struct Country const france = {
  .country_name = "France",
  .elo_rating = 0,
};
struct Country const germany = {
  .country_name = "Germany",
  .elo_rating = 0,
};
struct Country const ghana = {
  .country_name = "Ghana",
  .elo_rating = 0,
};
struct Country const haiti = {
  .country_name = "Haiti",
  .elo_rating = 0,
};
struct Country const iran = {
  .country_name = "Iran",
  .elo_rating = 0,
};
struct Country const ivory_coast = {
  .country_name = "Ivory Coast",
  .elo_rating = 0,
};
struct Country const japan = {
  .country_name = "Japan",
  .elo_rating = 0,
};
struct Country const jordan = {
  .country_name = "Jordan",
  .elo_rating = 0,
};
struct Country const mexico = {
  .country_name = "Mexico",
  .elo_rating = 0,
};
struct Country const moroco = {
  .country_name = "Moroco",
  .elo_rating = 0,
};
struct Country const netherlands = {
  .country_name = "Netherlands",
  .elo_rating = 0,
};
struct Country const new_zeland = {
  .country_name = "New Zeland",
  .elo_rating = 0,
};
struct Country const norway = {
  .country_name = "Norway",
  .elo_rating = 0,
};
struct Country const panama = {
  .country_name = "Panama",
  .elo_rating = 0,
};
struct Country const paraguay = {
  .country_name = "Paraguay",
  .elo_rating = 0,
};
struct Country const portugal = {
  .country_name = "Portugal",
  .elo_rating = 0,
};
struct Country const qatar = {
  .country_name = "Qatar",
  .elo_rating = 0,
};
struct Country const saudi_arabia = {
  .country_name = "Saudi Arabia",
  .elo_rating = 0,
};
struct Country const scotland = {
  .country_name = "Scotland",
  .elo_rating = 0,
};
struct Country const senegal = {
  .country_name = "Senegal",
  .elo_rating = 0,
};
struct Country const south_africa = {
  .country_name = "South Africa",
  .elo_rating = 0,
};
struct Country const south_korea = {
  .country_name = "South Korea",
  .elo_rating = 0,
};
struct Country const spain = {
  .country_name = "Spain",
  .elo_rating = 0,
};
struct Country const switzerland = {
  .country_name = "Switzerland",
  .elo_rating = 0,
};
struct Country const tunisia = {
  .country_name = "Tunisia",
  .elo_rating = 0,
};
struct Country const uruguay = {
  .country_name = "Uruguay",
  .elo_rating = 0,
};
struct Country const usa = {
  .country_name = "USA",
  .elo_rating = 0,
};
struct Country const uzbekistan = {
  .country_name = "Uzbekistan",
  .elo_rating = 0,
};
// { .country_name = "<UEFA Path A winner>", .elo_rating = 0 };
// { .country_name = "<UEFA Path B winner>", .elo_rating = 0 };
// { .country_name = "<UEFA Path C winner>", .elo_rating = 0 };
// { .country_name = "<UEFA Path D winner>", .elo_rating = 0 };
// { .country_name = "<IC Path 1 winner>", .elo_rating = 0 };
// { .country_name = "<IC Path 2 winner>", .elo_rating = 0 },

struct Country const* countries[COUNTRY_COUNT] = {
  &australia,
  &algeria,
  &argentina,
  &australia,
  &austria,
  &belgium,
  &brazil,
  &canada,
  &cape_verde,
  &colombia,
  &croatia,
  &curacao,
  &ecuador,
  &egypt,
  &england,
  &france,
  &germany,
  &ghana,
  &haiti,
  &iran,
  &ivory_coast,
  &japan,
  &jordan,
  &mexico,
  &moroco,
  &netherlands,
  &new_zeland,
  &norway,
  &panama,
  &paraguay,
  &portugal,
  &qatar,
  &saudi_arabia,
  &scotland,
  &senegal,
  &south_africa,
  &south_korea,
  &spain,
  &switzerland,
  &tunisia,
  &uruguay,
  &usa,
  &uzbekistan,
};

static void run_simulation(struct Simulation* simulation,
                           struct CountryAccumulatedPlacements* cap_array) {
  // TODO: Implement!

  simulation->matches[67] = (struct Match){
    .home_team = &england,
    .away_team = &usa,
    .home_goals = 7,
    .away_goals = 0,
    .winner = &england,
  };

  for (uint16_t i = 0; i < COUNTRY_COUNT; i++) {
    if (cap_array[i].country == &england) {
      cap_array[i].first_place += 1;
    }
    if (cap_array[i].country == &usa) {
      cap_array[i].second_place += 1;
    }
  }
}

static float percentage_from_total(uint16_t total, uint32_t simulations_count) {
  return (total * 100) / simulations_count;
}

static void print_placement_percentages(struct CountryAccumulatedPlacements *cap_array, uint32_t simulations_count) {
  printf("      Country    48th    32nd    16th     8th     4th     3rd     "
         "2nd     1st\n");
  for (uint16_t i = 0; i < COUNTRY_COUNT; i++) {
    struct CountryAccumulatedPlacements country_accumulated_placements =
        cap_array[i];
    printf("%13s %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f\n",
           country_accumulated_placements.country->country_name,
           percentage_from_total(
               country_accumulated_placements.forty_eight_place,
               simulations_count),
           percentage_from_total(
               country_accumulated_placements.thirty_second_place,
               simulations_count),
           percentage_from_total(
               country_accumulated_placements.sixteenth_place,
               simulations_count),
           percentage_from_total(
               country_accumulated_placements.eith_place,
               simulations_count),
           percentage_from_total(
               country_accumulated_placements.fourth_place,
               simulations_count),
           percentage_from_total(
               country_accumulated_placements.third_place,
               simulations_count),
           percentage_from_total(
               country_accumulated_placements.second_place,
               simulations_count),
           percentage_from_total(
               country_accumulated_placements.first_place,
               simulations_count)
           );
  }
}

int main(void) {
  uint32_t simulations_count = 5; // TODO: Change to 100000.

  // Initialize country accumulated placements array.
  struct CountryAccumulatedPlacements cap_array[COUNTRY_COUNT] = { 0 };
  for (uint16_t i = 0; i < COUNTRY_COUNT; i++) {
    cap_array[i].country = countries[i];
  }

  // Run simulations.
  struct Simulation* all_simulations =
      calloc(simulations_count, sizeof(struct Simulation));
  for (uint32_t i = 0; i < simulations_count; i++) {
    run_simulation(&(all_simulations[i]), cap_array);
  }
  free(all_simulations);

  // TODO: Print group stage placement percentages.

  // TODO: Sort cap_array so the most winner is printed first.

  print_placement_percentages(cap_array, simulations_count);

  return 0;
}
