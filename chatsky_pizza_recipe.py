from chatsky import (
    GLOBAL,
    TRANSITIONS,
    RESPONSE,
    Pipeline,
    conditions as cnd,
    Transition as Tr,
)


script = {
    GLOBAL: {
        TRANSITIONS: [
            Tr(
                dst=("flow", "node_cooking_instructions"),
                cnd=cnd.Regexp(r"(bake|cook|preheat).*\d+.*(degrees|fahrenheit|celsius)")
            ),
            Tr(
                dst=("flow", "node_ingredients"),
                cnd=cnd.Regexp(r"(flour|dough|sauce|cheese|toppings?|ingredients?)")
            ),
            Tr(
                dst=("flow", "node_time_instructions"),
                cnd=cnd.Regexp(r"\d+\s*(minutes?|mins?|hours?)")
            ),
            Tr(
                dst=("flow", "node_pizza_types"),
                cnd=cnd.Regexp(r"(margherita|pepperoni|hawaiian|quattro|diavola)")
            ),
            Tr(
                dst=("flow", "node_pepperoni_recipe"),
                cnd=cnd.Regexp(r"pepperoni.*recipe|recipe.*pepperoni")
            ),
            Tr(
                dst=("flow", "node_margherita_recipe"),
                cnd=cnd.Regexp(r"margherita.*recipe|recipe.*margherita")
            ),
            Tr(
                dst=("flow", "node_hawaiian_recipe"),
                cnd=cnd.Regexp(r"hawaiian.*recipe|recipe.*hawaiian")
            ),
            Tr(
                dst=("flow", "node_quattro_recipe"),
                cnd=cnd.Regexp(r"quattro.*recipe|recipe.*quattro")
            ),
            Tr(
                dst=("flow", "node_diavola_recipe"),
                cnd=cnd.Regexp(r"diavola.*recipe|recipe.*diavola")
            ),
            Tr(
                dst=("flow", "node_pineapple_pizza"),
                cnd=cnd.Regexp(r"pineapple") # Regexp is literally just the regex pattern... using python regex
            ),
            Tr(
                dst=("flow", "node_ok"),
                cnd=cnd.ExactMatch("OK"),
            ),
            Tr(
                dst=("flow", "node_default")
            ),
        ]
    },
    "flow":{
        "node_default": {RESPONSE: "Hello, I'm a pizza bot. I can help you with pizza recipes! Ask me about pepperoni, margherita, hawaiian, quattro stagioni, or diavola pizza recipes."},
        "node_pineapple_pizza": {RESPONSE: "Pineapple pizza is not a pizza. The Italian mobs would be knocking on your door soon. Goodbye. :)"},
        "node_cooking_instructions": {RESPONSE: "What are the cooking instructions for the pizza?"},
        "node_ingredients": {RESPONSE: "You will need the following ingredients: flour, dough, sauce, cheese, and toppings for this pizza."},
        "node_time_instructions": {RESPONSE: "What are the time instructions for the pizza?"},
        "node_pizza_types_pepperoni": {RESPONSE: "What are the types of pizza?"},
        "node_pizza_types_margherita": {RESPONSE: "What are the types of pizza?"},
        "node_pizza_types_hawaiian": {RESPONSE: "What are the types of pizza?"},
        "node_pizza_types_quattro": {RESPONSE: "What are the types of pizza?"},
        "node_pizza_types_diavola": {RESPONSE: "What are the types of pizza?"},
        "node_pepperoni_recipe": {RESPONSE: """🍕 PEPPERONI PIZZA RECIPE 🍕

INGREDIENTS:
For the Dough:
• 3 1/2 cups all-purpose flour
• 1 tsp salt
• 1 tsp sugar
• 2 1/4 tsp active dry yeast
• 1 1/3 cups warm water (110°F)
• 2 tbsp olive oil

For the Sauce:
• 1 can (14 oz) crushed tomatoes
• 2 tbsp tomato paste
• 2 cloves garlic, minced
• 1 tsp dried oregano
• 1 tsp dried basil
• 1/2 tsp salt
• 1/4 tsp black pepper
• 1 tbsp olive oil

For the Toppings:
• 8 oz mozzarella cheese, shredded
• 6 oz pepperoni slices
• 1/4 cup grated Parmesan cheese
• 1 tbsp olive oil (for brushing)

INSTRUCTIONS:
1. Make the Dough:
   - Mix flour, salt, and sugar in a large bowl
   - Dissolve yeast in warm water, let stand 5 minutes
   - Add yeast mixture and olive oil to flour, knead 10 minutes
   - Place in greased bowl, cover, let rise 1 hour

2. Make the Sauce:
   - Heat olive oil, sauté garlic 30 seconds
   - Add tomatoes, paste, herbs, salt, pepper
   - Simmer 15 minutes, let cool

3. Assemble Pizza:
   - Preheat oven to 450°F (230°C)
   - Roll dough to 14-inch circle
   - Spread sauce, add cheese, arrange pepperoni
   - Brush edges with olive oil

4. Bake:
   - Bake 12-15 minutes until crust is golden
   - Let rest 5 minutes before slicing

Enjoy your homemade pepperoni pizza! 🍕"""},
        "node_margherita_recipe": {RESPONSE: """🍕 MARGHERITA PIZZA RECIPE 🍕

INGREDIENTS:
For the Dough:
• 3 1/2 cups all-purpose flour
• 1 tsp salt
• 1 tsp sugar
• 2 1/4 tsp active dry yeast
• 1 1/3 cups warm water (110°F)
• 2 tbsp olive oil

For the Sauce:
• 1 can (14 oz) San Marzano tomatoes, crushed
• 2 cloves garlic, minced
• 1/4 cup fresh basil leaves, torn
• 1/2 tsp salt
• 1/4 tsp black pepper
• 2 tbsp olive oil

For the Toppings:
• 8 oz fresh mozzarella, sliced
• 1/2 cup fresh basil leaves
• 1/4 cup grated Parmesan cheese
• 2 tbsp olive oil (for drizzling)
• Sea salt to taste

INSTRUCTIONS:
1. Make the Dough:
   - Mix flour, salt, and sugar in a large bowl
   - Dissolve yeast in warm water, let stand 5 minutes
   - Add yeast mixture and olive oil to flour, knead 10 minutes
   - Place in greased bowl, cover, let rise 1 hour

2. Make the Sauce:
   - Heat olive oil, sauté garlic 30 seconds
   - Add crushed tomatoes, salt, pepper
   - Simmer 10 minutes, add basil, let cool

3. Assemble Pizza:
   - Preheat oven to 500°F (260°C) with pizza stone
   - Roll dough to 14-inch circle
   - Spread thin layer of sauce
   - Add mozzarella slices, torn basil
   - Drizzle with olive oil

4. Bake:
   - Bake 8-10 minutes until cheese bubbles
   - Add fresh basil after baking
   - Drizzle with olive oil and sea salt

Classic Italian Margherita! 🇮🇹"""},
        "node_hawaiian_recipe": {RESPONSE: """🍕 HAWAIIAN PIZZA RECIPE 🍕

INGREDIENTS:
For the Dough:
• 3 1/2 cups all-purpose flour
• 1 tsp salt
• 1 tsp sugar
• 2 1/4 tsp active dry yeast
• 1 1/3 cups warm water (110°F)
• 2 tbsp olive oil

For the Sauce:
• 1 can (14 oz) crushed tomatoes
• 2 tbsp tomato paste
• 2 cloves garlic, minced
• 1 tsp dried oregano
• 1/2 tsp salt
• 1/4 tsp black pepper
• 1 tbsp olive oil

For the Toppings:
• 8 oz mozzarella cheese, shredded
• 6 oz ham, diced or sliced
• 1 cup fresh pineapple, diced
• 1/4 cup grated Parmesan cheese
• 1 tbsp olive oil (for brushing)
• 1/4 cup red onion, thinly sliced (optional)

INSTRUCTIONS:
1. Make the Dough:
   - Mix flour, salt, and sugar in a large bowl
   - Dissolve yeast in warm water, let stand 5 minutes
   - Add yeast mixture and olive oil to flour, knead 10 minutes
   - Place in greased bowl, cover, let rise 1 hour

2. Make the Sauce:
   - Heat olive oil, sauté garlic 30 seconds
   - Add tomatoes, paste, herbs, salt, pepper
   - Simmer 15 minutes, let cool

3. Assemble Pizza:
   - Preheat oven to 450°F (230°C)
   - Roll dough to 14-inch circle
   - Spread sauce, add mozzarella
   - Arrange ham and pineapple evenly
   - Add red onion if desired
   - Brush edges with olive oil

4. Bake:
   - Bake 12-15 minutes until crust is golden
   - Let rest 5 minutes before slicing

Sweet and savory Hawaiian pizza! 🍍"""},
        "node_quattro_recipe": {RESPONSE: """🍕 QUATTRO STAGIONI PIZZA RECIPE 🍕

INGREDIENTS:
For the Dough:
• 3 1/2 cups all-purpose flour
• 1 tsp salt
• 1 tsp sugar
• 2 1/4 tsp active dry yeast
• 1 1/3 cups warm water (110°F)
• 2 tbsp olive oil

For the Sauce:
• 1 can (14 oz) crushed tomatoes
• 2 tbsp tomato paste
• 2 cloves garlic, minced
• 1 tsp dried oregano
• 1 tsp dried basil
• 1/2 tsp salt
• 1/4 tsp black pepper
• 1 tbsp olive oil

For the Toppings (divided into 4 sections):
• 8 oz mozzarella cheese, shredded
• 1/4 cup grated Parmesan cheese

Spring Section:
• 1/2 cup artichoke hearts, quartered
• 1/4 cup fresh peas

Summer Section:
• 1/2 cup cherry tomatoes, halved
• 1/4 cup fresh basil leaves

Autumn Section:
• 1/2 cup mushrooms, sliced
• 1/4 cup prosciutto, torn

Winter Section:
• 1/2 cup black olives, pitted
• 1/4 cup anchovies (optional)

INSTRUCTIONS:
1. Make the Dough:
   - Mix flour, salt, and sugar in a large bowl
   - Dissolve yeast in warm water, let stand 5 minutes
   - Add yeast mixture and olive oil to flour, knead 10 minutes
   - Place in greased bowl, cover, let rise 1 hour

2. Make the Sauce:
   - Heat olive oil, sauté garlic 30 seconds
   - Add tomatoes, paste, herbs, salt, pepper
   - Simmer 15 minutes, let cool

3. Assemble Pizza:
   - Preheat oven to 450°F (230°C)
   - Roll dough to 14-inch circle
   - Spread sauce and cheese over entire pizza
   - Divide pizza into 4 equal sections
   - Add toppings to each section:
     * Spring: artichokes and peas
     * Summer: tomatoes and basil
     * Autumn: mushrooms and prosciutto
     * Winter: olives and anchovies

4. Bake:
   - Bake 12-15 minutes until crust is golden
   - Let rest 5 minutes before slicing

Four seasons in one pizza! 🌸🌞🍂❄️"""},
        "node_diavola_recipe": {RESPONSE: """🍕 DIAVOLA PIZZA RECIPE 🍕

INGREDIENTS:
For the Dough:
• 3 1/2 cups all-purpose flour
• 1 tsp salt
• 1 tsp sugar
• 2 1/4 tsp active dry yeast
• 1 1/3 cups warm water (110°F)
• 2 tbsp olive oil

For the Sauce:
• 1 can (14 oz) crushed tomatoes
• 2 tbsp tomato paste
• 2 cloves garlic, minced
• 1 tsp dried oregano
• 1/2 tsp red pepper flakes
• 1/2 tsp salt
• 1/4 tsp black pepper
• 1 tbsp olive oil

For the Toppings:
• 8 oz mozzarella cheese, shredded
• 6 oz spicy salami or pepperoni
• 1/4 cup grated Parmesan cheese
• 1/4 cup red onion, thinly sliced
• 1/4 cup black olives, pitted and sliced
• 1-2 fresh red chili peppers, sliced
• 1 tbsp olive oil (for brushing)
• Extra red pepper flakes for serving

INSTRUCTIONS:
1. Make the Dough:
   - Mix flour, salt, and sugar in a large bowl
   - Dissolve yeast in warm water, let stand 5 minutes
   - Add yeast mixture and olive oil to flour, knead 10 minutes
   - Place in greased bowl, cover, let rise 1 hour

2. Make the Spicy Sauce:
   - Heat olive oil, sauté garlic 30 seconds
   - Add tomatoes, paste, herbs, red pepper flakes, salt, pepper
   - Simmer 15 minutes, let cool

3. Assemble Pizza:
   - Preheat oven to 450°F (230°C)
   - Roll dough to 14-inch circle
   - Spread spicy sauce, add mozzarella
   - Arrange salami/pepperoni, red onion, olives
   - Add fresh chili peppers
   - Brush edges with olive oil

4. Bake:
   - Bake 12-15 minutes until crust is golden
   - Let rest 5 minutes before slicing
   - Serve with extra red pepper flakes

Spicy Diavola pizza - the devil's pizza! 🔥"""},
        "node_ok": {RESPONSE: "OK PIZZA DESCRIPTION, I'M SENDING IT TO THE KITCHEN"},
        "node_regex_test": {RESPONSE: "I'm sorry, I don't understand. Please try again."},
    },
}

# initialize the pipeline (needed to run the script)
pipeline = Pipeline(script, start_label=("flow", "node_default"))


pipeline.run()