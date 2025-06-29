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
                dst=("flow", "node_pizza_recipe"),
                cnd=cnd.Regexp(r"pizza.*recipe|recipe.*pizza")
            ),
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
                dst=("flow", "node_regex_test"),
                cnd=cnd.Regexp("pineapple$"), # Regexp is literally just the regex pattern... using python regex
            ),
            Tr(
                dst=("flow", "node_pineapple_pizza"),
                cnd=cnd.Regexp("^pineapple") # Regexp is literally just the regex pattern... using python regex
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
        "node_default": {RESPONSE: "Hello, I'm a pizza bot. I can help you describe your pizza. What is the name of the pizza?"},
        "node_pizza_recipe": {RESPONSE: "Definetely no pineapples on the pizza. What is the name of the pizza?"},
        "node_pineapple_pizza": {RESPONSE: "Pineapple pizza is not a pizza. The Italian mobs would be knocking on your door soon. Goodbye. :)"},
        "node_cooking_instructions": {RESPONSE: "What are the cooking instructions for the pizza?"},
        "node_ingredients": {RESPONSE: "You will need the following ingredients: flour, dough, sauce, cheese, and toppings for this pizza."},
        "node_time_instructions": {RESPONSE: "What are the time instructions for the pizza?"},
        "node_pizza_types": {RESPONSE: "What are the types of pizza?"},
        "node_ok": {RESPONSE: "OK PIZZA DESCRIPTION, I'M SENDING IT TO THE KITCHEN"},
        "node_regex_test": {RESPONSE: "I'm sorry, I don't understand. Please try again."},
    },
}

# initialize the pipeline (needed to run the script)
pipeline = Pipeline(script, start_label=("flow", "node_default"))


pipeline.run()