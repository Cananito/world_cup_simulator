#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// TODO: Make it so each year's data is either loaded and parsed or #included.

// TODO: Delete Python programs, but keep their simulations.

// Elo ratings: https://www.eloratings.net/
// 2026 Wiki: https://en.wikipedia.org/wiki/2026_FIFA_World_Cup
// Regulations PDF: https://digitalhub.fifa.com/m/636f5c9c6f29771f/original/FWC2026_regulations_EN.pdf

#define COUNTRY_COUNT 48
#define GROUP_COUNT 12

struct Country {
  char name[20];
  uint16_t elo_rating;
  // TODO: Group stage identifier?
};

struct Group {
  char name[8];
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
  .name = "Algeria",
  .elo_rating = 0,
};
struct Country const argentina = {
  .name = "Argentina",
  .elo_rating = 0,
};
struct Country const australia = {
  .name = "Australia",
  .elo_rating = 0,
};
struct Country const austria = {
  .name = "Austria",
  .elo_rating = 0,
};
struct Country const belgium = {
  .name = "Belgium",
  .elo_rating = 0,
};
struct Country const brazil = {
  .name = "Brazil",
  .elo_rating = 0,
};
struct Country const canada = {
  .name = "Canada",
  .elo_rating = 0,
};
struct Country const cape_verde = {
  .name = "Cape Verde",
  .elo_rating = 0,
};
struct Country const colombia = {
  .name = "Colombia",
  .elo_rating = 0,
};
struct Country const croatia = {
  .name = "Croatia",
  .elo_rating = 0,
};
struct Country const curacao = {
  .name = "Curacao",
  .elo_rating = 0,
};
struct Country const ecuador = {
  .name = "Ecuador",
  .elo_rating = 0,
};
struct Country const egypt = {
  .name = "Egypt",
  .elo_rating = 0,
};
struct Country const england = {
  .name = "England",
  .elo_rating = 0,
};
struct Country const france = {
  .name = "France",
  .elo_rating = 0,
};
struct Country const germany = {
  .name = "Germany",
  .elo_rating = 0,
};
struct Country const ghana = {
  .name = "Ghana",
  .elo_rating = 0,
};
struct Country const haiti = {
  .name = "Haiti",
  .elo_rating = 0,
};
struct Country const iran = {
  .name = "Iran",
  .elo_rating = 0,
};
struct Country const ivory_coast = {
  .name = "Ivory Coast",
  .elo_rating = 0,
};
struct Country const japan = {
  .name = "Japan",
  .elo_rating = 0,
};
struct Country const jordan = {
  .name = "Jordan",
  .elo_rating = 0,
};
struct Country const mexico = {
  .name = "Mexico",
  .elo_rating = 0,
};
struct Country const moroco = {
  .name = "Moroco",
  .elo_rating = 0,
};
struct Country const netherlands = {
  .name = "Netherlands",
  .elo_rating = 0,
};
struct Country const new_zeland = {
  .name = "New Zeland",
  .elo_rating = 0,
};
struct Country const norway = {
  .name = "Norway",
  .elo_rating = 0,
};
struct Country const panama = {
  .name = "Panama",
  .elo_rating = 0,
};
struct Country const paraguay = {
  .name = "Paraguay",
  .elo_rating = 0,
};
struct Country const portugal = {
  .name = "Portugal",
  .elo_rating = 0,
};
struct Country const qatar = {
  .name = "Qatar",
  .elo_rating = 0,
};
struct Country const saudi_arabia = {
  .name = "Saudi Arabia",
  .elo_rating = 0,
};
struct Country const scotland = {
  .name = "Scotland",
  .elo_rating = 0,
};
struct Country const senegal = {
  .name = "Senegal",
  .elo_rating = 0,
};
struct Country const south_africa = {
  .name = "South Africa",
  .elo_rating = 0,
};
struct Country const south_korea = {
  .name = "South Korea",
  .elo_rating = 0,
};
struct Country const spain = {
  .name = "Spain",
  .elo_rating = 0,
};
struct Country const switzerland = {
  .name = "Switzerland",
  .elo_rating = 0,
};
struct Country const tunisia = {
  .name = "Tunisia",
  .elo_rating = 0,
};
struct Country const uruguay = {
  .name = "Uruguay",
  .elo_rating = 0,
};
struct Country const usa = {
  .name = "USA",
  .elo_rating = 0,
};
struct Country const uzbekistan = {
  .name = "Uzbekistan",
  .elo_rating = 0,
};
// { .name = "<UEFA Path A winner>", .elo_rating = 0 };
// { .name = "<UEFA Path B winner>", .elo_rating = 0 };
// { .name = "<UEFA Path C winner>", .elo_rating = 0 };
// { .name = "<UEFA Path D winner>", .elo_rating = 0 };
// { .name = "<IC Path 1 winner>", .elo_rating = 0 };
// { .name = "<IC Path 2 winner>", .elo_rating = 0 },

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

struct Group const group_a = {
  .name = "Group A",
};

struct Group const group_b = {
  .name = "Group B",
};

struct Group const group_c = {
  .name = "Group C",
};

struct Group const group_d = {
  .name = "Group D",
};

struct Group const group_e = {
  .name = "Group E",
};

struct Group const group_f = {
  .name = "Group F",
};

struct Group const group_g = {
  .name = "Group G",
};

struct Group const group_h = {
  .name = "Group H",
};

struct Group const group_i = {
  .name = "Group I",
};

struct Group const group_j = {
  .name = "Group J",
};

struct Group const group_k = {
  .name = "Group K",
};

struct Group const group_l = {
  .name = "Group L",
};

struct Group const* groups[GROUP_COUNT] = {
  &group_a,
  &group_b,
  &group_c,
  &group_d,
  &group_e,
  &group_f,
  &group_g,
  &group_h,
  &group_i,
  &group_j,
  &group_k,
  &group_l,
};

static void run_simulation(struct Simulation* simulation,
                           struct CountryAccumulatedPlacements* cap_array) {
  // TODO: Implement!

  simulation->matches[103] = (struct Match){
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

static void print_group_stage_placement_percentages() {
  for (uint8_t i = 0; i < GROUP_COUNT; i++) {
    struct Group const* group = groups[i];
    printf("%s\n", group->name);
    // TODO: Print the table, sorted by most winner.
  }
}

static void print_placement_percentages(
    struct CountryAccumulatedPlacements *cap_array,
    uint32_t simulations_count) {
  printf("      Country    48th    32nd    16th     8th     4th     3rd     "
         "2nd     1st\n");
  for (uint16_t i = 0; i < COUNTRY_COUNT; i++) {
    struct CountryAccumulatedPlacements country_accumulated_placements =
        cap_array[i];
    printf("%13s %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f\n",
           country_accumulated_placements.country->name,
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

  // TODO: Sort cap_array so the most winner is printed first.

  printf("> Group stage results\n");
  printf("\n");
  print_group_stage_placement_percentages();
  printf("\n");
  printf("\n");
  printf("> Winning probabilities\n");
  printf("\n");
  print_placement_percentages(cap_array, simulations_count);

  return 0;
}
