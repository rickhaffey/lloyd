# User Story Mapping

* [The New User Story Backlog is a Map (User Story Mapping Summary) - Jeff Patton](https://jpattonassociates.com/the-new-backlog/)
* [Story Mapping Quick Reference](https://jpattonassociates.com/wp-content/uploads/2015/03/story_mapping.pdf)
* [Story Essentials Quick Reference](https://jeffpatton.wpengine.com/wp-content/uploads/2015/03/story_essentials_quickref.pdf)
* [Five common mistakes teams make when User Story Mapping - Jeff Patton (youtube)](https://www.youtube.com/watch?v=0W9g-D3oTm8)
  * [associated slide deck](https://miro.com/app/board/uXjVNfrRMxI=/)


## Story Map Components

### Users

* type of person doing something to achieve a goal
* include lightweight persona sketches to describe the user

### Goal Levels

* **summary**: many tasks done in support of a bigger goal; 10k foot view
* **functional**: a task that one would expect to finish in a single session; sea-level view
* **sub-functional**: a task that is part of a functional goal, but not a goal in itself; below sea-level view

### Backbone

* activities and tasks at a higher goal level that give the map structure
* arranged in a narrative flow

### Narrative Flow

* left-to-right axis in the map
* organized in the order you’d tell the story about your user to someone else
* any _specific_ user might not follow the exact same path, but the general flow is the same

### Activities

* organize tasks done by similar users at similar times to reach a goal
* at the _summary_ goal level

### User Tasks

* short verb phrases
* basic building blocks of the map
* template: `<verb> a <noun>`
  * e.g. "create a user story", "review a design", "test a feature"
* at the _functional_ or _sub-functional_ goal level

### Details

* top-to-bottom axis in the map
* activities and high level tasks at the top
* subtasks, alternatives, exceptions, and details as you move down the map

### Release Slices

* horizontal slices across the map
* identify smallest set of tasks that allow users to reach a goal
* can identify small experiments, mvp releases, etc.
* identify the target outcomes in a card to the left of the slice

## Mapping Process

### Map Now & Later

Story maps can be used to understand current state and to image future state.

Use a map to describe the world as it is today.  Include the following callouts:
* what works well
* pain points

Use the map of current state, along with a breakout of details, observations, and solution ideas, to create a story map
for later that describes what the product will offer users in the future.

### Mapping Steps

1. **Frame**
   * create a short product or feature brief
   * frame and constrain
   * **what**: the product, feature, or problem to be solved
   * **who**: the users and their goals
   * **why**: the value to the users and the business
2. **Map the Big Picture**
   * focus on getting the whole story
   * "mile wide, inch deep"
   * activities and high-level user tasks
   * focus on user type most critical to product's success
3. **Explore**
   * break down the big picture into smaller tasks
   * think "blue sky" - possibilities; "wouldn't it be cool if..."
   * think of everything that could go wrong - exceptions
   * think of variations; "what else might users do?"
   * identify additional user types: "what might other users do?"
   * add in other product details:
     * proposed UI elements
     * business rules
     * data elements
     * etc.
   * don't worry about in/out of scope at this point (will filter later)
4. **Slice out Viable Releases**
   * slice map into holistic product releases
   * these form an incremental delivery roadmap; each release is an mvp release
   * for each release name the target outcomes and impact
   * for each release identify product success metrics
5. **Slice out a Development Strategy**
   * slice the first release of your map into 3 or more delivery phases
     * allows team to learn fast and avoid risk
     * phase 1: "opening": build a functional "walking skeleton"; simplest possible functional version of the product; validate performance and scalability
     * phase 2: "mid-game": complete all major functionality; expand/enrich existing functionality
     * phase 3: "end-game": polish, refine, and optimize; add in any remaining features; continually assess release readiness
   * plan the work necessary to deliver the first release
   * workshop stories with development team; work through details and agreement on acceptance criteria
   * plan development and testing
   * build and verify the first release
6. **Iterate**
