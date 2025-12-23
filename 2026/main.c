#include <stdio.h>
#include <stdint.h>

// Elo ratings: https://www.eloratings.net/

struct Country {
  char country_name[20];
};

struct CountryElo {
  struct Country country;
  uint16_t elo_rating;
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

struct CountryElo country_elos[48] = {
  { .country = australia, .elo_rating = 0 },
  { .country = algeria, .elo_rating = 0 },
  { .country = argentina, .elo_rating = 0 },
  { .country = australia, .elo_rating = 0 },
  { .country = austria, .elo_rating = 0 },
  { .country = belgium, .elo_rating = 0 },
  { .country = brazil, .elo_rating = 0 },
  { .country = canada, .elo_rating = 0 },
  { .country = cape_verde, .elo_rating = 0 },
  { .country = colombia, .elo_rating = 0 },
  { .country = croatia, .elo_rating = 0 },
  { .country = curacao, .elo_rating = 0 },
  { .country = ecuador, .elo_rating = 0 },
  { .country = egypt, .elo_rating = 0 },
  { .country = england, .elo_rating = 0 },
  { .country = france, .elo_rating = 0 },
  { .country = germany, .elo_rating = 0 },
  { .country = ghana, .elo_rating = 0 },
  { .country = haiti, .elo_rating = 0 },
  { .country = iran, .elo_rating = 0 },
  { .country = ivory_coast, .elo_rating = 0 },
  { .country = japan, .elo_rating = 0 },
  { .country = jordan, .elo_rating = 0 },
  { .country = mexico, .elo_rating = 0 },
  { .country = moroco, .elo_rating = 0 },
  { .country = netherlands, .elo_rating = 0 },
  { .country = new_zeland, .elo_rating = 0 },
  { .country = norway, .elo_rating = 0 },
  { .country = panama, .elo_rating = 0 },
  { .country = paraguay, .elo_rating = 0 },
  { .country = portugal, .elo_rating = 0 },
  { .country = qatar, .elo_rating = 0 },
  { .country = saudi_arabia, .elo_rating = 0 },
  { .country = scotland, .elo_rating = 0 },
  { .country = senegal, .elo_rating = 0 },
  { .country = south_africa, .elo_rating = 0 },
  { .country = south_korea, .elo_rating = 0 },
  { .country = spain, .elo_rating = 0 },
  { .country = switzerland, .elo_rating = 0 },
  { .country = tunisia, .elo_rating = 0 },
  { .country = uruguay, .elo_rating = 0 },
  { .country = usa, .elo_rating = 0 },
  { .country = uzbekistan, .elo_rating = 0 },
};

int main(void) {
  printf("Coming soon...\n");
  return 0;
}
