import argparse
import itertools
import random

PROTEIN = ["chicken", "beef", "pork", "fish"]
CARBS = ["rice", "pasta", "potatoes"]
VEGGIES = ["green beans", "peas and carrots", "asian veggies", "corn and bell peppers"]

PROTEIN_MAP = {
    "chicken": [
        "Chicken with pan sauce",
        "Grilled fire sauce chicken",
        "Grilled chicken",
        "Shredded buffalo chicken",
        "Teriyaki chicken",
    ],
    "beef": ["Galbi braised beef", "Steak", "Carne asada"],
    "pork": ["pulled pork", "spicy pork"],
    "fish": ["salmon", "canned tuna"],
    "shrimp": ["shrimp"],
}
CARBS_MAP = {
    "rice": ["white rice", "fried rice"],
    "pasta": ["red sauce pasta w/garlic bread", "white sauce pasta w/garlic bread", "mac and cheese"],
    "potatoes": ["mashed potatoes", "roasted sweet potatoes", "french fries"],
}


def choose_protein_class(num_options=2):
    return random.sample(PROTEIN, num_options)


def choose_protein(protein_classes):
    proteins = []
    for p_class in protein_classes:
        proteins.append(random.choice(PROTEIN_MAP[p_class]))
    return proteins


def choose_carb_class(num_options=2):
    return random.sample(CARBS, num_options)


def choose_carbs(carb_classes):
    carbs = []
    for c_class in carb_classes:
        carbs.append(random.choice(CARBS_MAP[c_class]))
    return carbs


def choose_veggies(num_options=2):
    return random.sample(VEGGIES, num_options)


def generate_random_perms(choice_classes):
    all_perms = list(itertools.product(*choice_classes))
    return random.sample(all_perms, len(all_perms))


parser = argparse.ArgumentParser(description="Meal prep generator")
parser.add_argument("--num_meals", type=int, default=5, help="Number of meals to generate")
parser.add_argument("--num_protein", type=int, default=2, help="Number of protein options to choose from")
parser.add_argument("--num_carbs", type=int, default=2, help="Number of carb options to choose from")
parser.add_argument("--num_veggies", type=int, default=2, help="Number of veggie options to choose from")
args = parser.parse_args()


def main():
    protein_classes = choose_protein_class(args.num_protein)
    protein = choose_protein(protein_classes)
    carb_classes = choose_carb_class(args.num_carbs)
    carbs = choose_carbs(carb_classes)

    veggies = choose_veggies(args.num_veggies)

    print("Protein: ", protein)
    print("Carbs: ", carbs)
    print("Veggies: ", veggies)
    print("\n")

    generate_meals = input("Would you like to generate meals? (y/n): ")
    if generate_meals == "n":
        return
    meals = []
    count = 0
    for p, c, v in generate_random_perms([protein, carbs, veggies]):
        print(f"{p}, {c}, {v}")
        resp = input("Accept meal? (y/n): ")
        if resp == "y":
            count += 1
            meals += [f"{p}, {c}, {v}"]
        if count == args.num_meals:
            print("Meal prep complete\ns")
            meals_formatted = "\n".join(meals)
            print(f"Meals: {meals_formatted}")
            break

    return


if __name__ == "__main__":
    main()
