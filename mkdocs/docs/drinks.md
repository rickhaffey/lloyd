# Drinks

## Refrerences

* [IBA Official Cocktails](https://iba-world.com/cocktails/)
  * Three Categories:
    * [Unforgettables](https://iba-world.com/cocktails/official-cocktails/unforgettable/)
    * [Contemporary Classics](https://iba-world.com/cocktails/official-cocktails/contemporary-classics/)
    * [New Era Drinks](https://iba-world.com/cocktails/official-cocktails/new-era-drinks/)
  * [IBA Official Cocktails - Wikipedia](https://en.wikipedia.org/wiki/List_of_IBA_official_cocktails)
* [Difford's Guide](https://www.diffordsguide.com/cocktails)
* [Bartending Terminology - Wikipedia](https://en.wikipedia.org/wiki/Bartending_terminology)

## Bar Menu Categories

When creating a bar menu, drinks can be categorized to help customers navigate their choices. Here are some common categories used in bar menus:

* **Beer and Cider**: A selection of beers, ales, stouts, and ciders available on tap or in bottles.
* **Wine**: A curated selection of wines, often categorized by type (red, white, rosé) or region.
* **Spirits and Liqueurs**: A list of available spirits, categorized by type (vodka, gin, rum, tequila, whiskey, etc.).
  * **Shots and Shooters**: A selection of quick, small drinks typically served in shot glasses.
* **Cocktails**: A variety of mixed drinks, often categorized by style or base spirit
  * **Signature Cocktails**: Unique drinks created by the bar, often featuring house-made ingredients.
  * **Classics**: Well-known cocktails that are timeless favorites, such as the Martini, Old Fashioned, and Margarita.
  * **Seasonal Specials**: Drinks that highlight seasonal ingredients or themes, such as summer fruit cocktails or winter warmers.
* **Sake and Soju**: A selection of Japanese sake and Korean soju, often served chilled or warm.
* **Tasting Flights**: A selection of small servings of different drinks, such as whiskey or craft beer, allowing customers to sample a variety.
* **Non-Alcoholic**: Mocktails and other non-alcoholic beverages for those who prefer not to drink alcohol.





## Ways to Categorize Drinks

Drinks can be categorized in various ways based on their characteristics, ingredients, preparation methods, and
serving styles. Here are some common ways to categorize drinks:

### 1. **By Type of Drink**

* **Alcoholic vs. Non-alcoholic:** Cocktails, beer, wine, spirits vs. mocktails, soft drinks, water.
* **Base Spirit:** Vodka, gin, rum, tequila, whiskey, brandy.
* **Beer Types:** Lager, ale, stout, porter, IPA.
* **Wine Types:** Red, white, rosé, sparkling.

### 2. **By Preparation Method**

* **Straight:** Served neat or on the rocks (without mixers).
* **Mixed:** Cocktails made with one or more spirits plus mixers.
* **Shaken/Blended:** Cocktails that are shaken with ice or blended (frozen drinks).
* **Layered:** Drinks served in distinct layers of different densities.

### 3. **By Flavor Profile**

* **Sweet, sour, bitter, spicy, smoky, fruity, herbal, creamy.**
* **Dry vs. Sweet:** Especially for wines and cocktails.

### 4. **By Occasion or Serving Style**

* **Shots:** Small, quick drinks.
* **Highballs:** Spirit plus a large portion of mixer, served in tall glass.
* **Lowballs:** Spirit plus a small amount of mixer, served in short glass.
* **Sippers:** Slow-sipping drinks like aged whiskey or fortified wines.

### 5. **By Alcohol Content**

* **Low alcohol:** Beer, wine, light cocktails.
* **High alcohol:** Straight spirits, fortified wines, strong cocktails.
* **Non-alcoholic:** Mocktails, soft drinks, juices.

### 6. **By Popularity or Demand**

* **Signature cocktails:** Bar’s specialty drinks.
* **Classics:** Well-known recipes like Margarita, Martini, Old Fashioned.
* **Trendy:** New or seasonal drinks.

### 7. **By Glassware**

* Martini glass, highball glass, rocks glass, pint glass, shot glass, wine glass, etc.

### 8. **By Price or Quality**

* **Premium vs. standard spirits.**
* **Craft or artisanal vs. mass-produced.**



## Drink / Drink Recipe Schema

Example (still WIP):

```json
{
  "name": "Mojito",
  "category": "Cocktail",
  "ingredients": [
    {
      "name": "White Rum",
      "amount": "50 ml"
    },
    {
      "name": "Fresh Lime Juice",
      "amount": "30 ml"
    },
    {
      "name": "Sugar Syrup",
      "amount": "2 tsp"
    },
    {
      "name": "Fresh Mint Leaves",
      "amount": "10 leaves"
    },
    {
      "name": "Soda Water",
      "amount": "to top up"
    }
  ],
  "garnish": [
    {
      "name": "Mint Sprig"
    },
    {
      "name": "Lime Wedge"
    }
  ],
  "glassware": {
    "type": "Highball Glass"
  },
  "instructions": [
    "Muddle mint leaves and sugar syrup in the glass.",
    "Add lime juice and rum, then fill with ice.",
    "Top up with soda water and stir gently.",
    "Garnish with a mint sprig and lime wedge."
  ]
}
```
